"""
RoadWatch AI - Flask Microservice for Video Analysis
Detects traffic violations using YOLOv8 and OpenCV
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
try:
    import cv2
except ImportError:
    cv2 = None
import numpy as np
from datetime import datetime
import os
from werkzeug.utils import secure_filename
import logging

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500 MB

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class ViolationDetector:
    """
    Detects traffic violations in video frames
    Uses YOLOv8-like detection (mock implementation)
    """

    def __init__(self):
        self.vehicle_classes = {
            1: 'truck',
            2: 'bus',
            5: 'car',
            3: 'motorcycle',
            6: 'auto'
        }
        # Mock model - in production, load actual YOLOv8 model
        self.model = None
        self.confident_threshold = 0.5

    def detect_vehicles(self, frame):
        """
        Detect vehicles in a frame (mock implementation)
        Returns: list of detections with type and confidence
        """
        # Mock detection
        height, width = frame.shape[:2]
        detections = []

        # Simulate detecting vehicles
        if np.random.random() > 0.7:  # 30% chance of detection
            vehicle_type = np.random.choice(['truck', 'bus', 'car'])
            confidence = np.random.uniform(0.7, 0.99)
            x = np.random.randint(0, width - 100)
            y = np.random.randint(0, height - 100)
            w = np.random.randint(80, 150)
            h = np.random.randint(60, 120)

            detections.append({
                'vehicle_type': vehicle_type,
                'confidence': round(confidence, 2),
                'bbox': [x, y, w, h]
            })

        return detections

    def detect_overtaking(self, frame1, frame2):
        """
        Detect dangerous overtaking pattern (mock)
        """
        # Mock overtaking detection
        if np.random.random() > 0.8:
            return {
                'overtaking_detected': True,
                'confidence': np.random.uniform(0.6, 0.95),
                'vehicle_count': 2,
                'danger_level': 'high'
            }
        return {'overtaking_detected': False, 'confidence': 0}

    def extract_plate_region(self, frame, bbox):
        """
        Extract license plate region from frame (mock)
        """
        x, y, w, h = bbox
        plate_region = frame[y:y+h, x:x+w]
        return plate_region

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'RoadWatch AI Detection Service'
    })

@app.route('/process', methods=['POST'])
def process_video():
    """
    Main endpoint for video processing
    Accepts video file and returns violation analysis
    """
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        video_id = request.form.get('video_id')

        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type'}), 400

        # Save file
        filename = secure_filename(f"{video_id}_{file.filename}")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        logger.info(f"Processing video: {filepath}")

        # Process video
        analysis_result = analyze_video(filepath)

        # Cleanup
        if os.path.exists(filepath):
            os.remove(filepath)

        return jsonify(analysis_result), 200

    except Exception as e:
        logger.error(f"Error processing video: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/detect-vehicles', methods=['POST'])
def detect_vehicles_endpoint():
    """Endpoint for frame-by-frame vehicle detection"""
    try:
        data = request.get_json()
        frame_base64 = data.get('frame')

        if not frame_base64:
            return jsonify({'error': 'No frame provided'}), 400

        # Decode base64 frame
        import base64
        img_data = base64.b64decode(frame_base64)
        nparr = np.frombuffer(img_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Detect vehicles
        detector = ViolationDetector()
        detections = detector.detect_vehicles(frame)

        return jsonify({
            'success': True,
            'detections': detections,
            'timestamp': datetime.now().isoformat()
        }), 200

    except Exception as e:
        logger.error(f"Error detecting vehicles: {str(e)}")
        return jsonify({'error': str(e)}), 500

def analyze_video(video_path, sample_rate=5):
    """
    Analyze video for violations
    Args:
        video_path: Path to video file
        sample_rate: Process every Nth frame
    """
    detector = ViolationDetector()
    violations = []
    vehicle_types = {}
    frame_count = 0
    violation_count = 0

    try:
        cap = cv2.VideoCapture(video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        prev_frame = None

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1

            # Sample frames
            if frame_count % sample_rate != 0:
                continue

            # Detect vehicles
            detections = detector.detect_vehicles(frame)

            for detection in detections:
                vehicle_type = detection['vehicle_type']
                vehicle_types[vehicle_type] = vehicle_types.get(vehicle_type, 0) + 1

                # Check for violations
                if vehicle_type in ['truck', 'bus']:
                    if prev_frame is not None:
                        overtaking = detector.detect_overtaking(prev_frame, frame)

                        if overtaking['overtaking_detected']:
                            frame_snapshot = cv2.imencode('.jpg', frame)[1].tobytes()
                            violations.append({
                                'type': 'dangerous_overtaking',
                                'vehicle_type': vehicle_type,
                                'confidence': min(
                                    detection['confidence'] * overtaking['confidence'],
                                    1.0
                                ),
                                'frame_number': frame_count,
                                'timestamp': frame_count / fps if fps > 0 else 0,
                                'frame_snapshot': frame_snapshot.hex()
                            })
                            violation_count += 1

            prev_frame = frame

            # Limit processing (for demo)
            if frame_count > 300:  # Process first 300 frames only
                break

        cap.release()

        # Prepare response
        processing_time = frame_count / fps if fps > 0 else 0

        return {
            'success': True,
            'violations': violations[:10],  # Return top 10 violations
            'vehiclesDetected': [
                {'type': k, 'count': v}
                for k, v in vehicle_types.items()
            ],
            'totalFramesProcessed': frame_count,
            'totalViolations': violation_count,
            'processingTime': round(processing_time, 2),
            'timestamp': datetime.now().isoformat()
        }

    except Exception as e:
        logger.error(f"Error analyzing video: {str(e)}")
        return {
            'success': False,
            'error': str(e)
        }

@app.route('/ocr/extract-plate', methods=['POST'])
def extract_license_plate():
    """
    Extract license plate from frame (mock implementation)
    """
    try:
        data = request.get_json()
        frame_base64 = data.get('frame')

        if not frame_base64:
            return jsonify({'error': 'No frame provided'}), 400

        # Mock OCR result
        mock_plates = ['MH-01-AB-1234', 'HR-26-GJ-5678', 'DL-12-CD-9999']
        plate = np.random.choice(mock_plates)

        return jsonify({
            'success': True,
            'plate': plate,
            'confidence': np.random.uniform(0.7, 0.99),
            'timestamp': datetime.now().isoformat()
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # For production, use a production WSGI server like Gunicorn
    app.run(host='0.0.0.0', port=5001, debug=True)
