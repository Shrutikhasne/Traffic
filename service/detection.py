"""
Vehicle Detection Module
Uses YOLOv8-like detection for traffic analysis
"""

import cv2
import numpy as np
from typing import List, Dict, Tuple

class Vehicle:
    """Represents a detected vehicle"""
    def __init__(self, vehicle_type: str, confidence: float, bbox: Tuple):
        self.vehicle_type = vehicle_type
        self.confidence = confidence
        self.bbox = bbox  # (x, y, width, height)
        self.position = (bbox[0], bbox[1])

class VehicleDetectionModel:
    """
    Main detection model (mock YOLOv8)
    In production, this would load actual YOLOv8 weights
    """

    VEHICLE_CLASSES = {
        0: 'person',
        1: 'bicycle',
        2: 'car',
        3: 'motorcycle',
        4: 'airplane',
        5: 'bus',
        6: 'train',
        7: 'truck',
        8: 'boat',
        11: 'stop sign',
        13: 'bench'
    }

    HEAVY_VEHICLES = ['truck', 'bus', 'train']

    def __init__(self, model_path: str = None):
        """Initialize detector"""
        self.model_path = model_path
        self.confidence_threshold = 0.5
        # In production: self.model = torch.hub.load('ultralytics/yolov8', 'custom', path=model_path)

    def detect(self, frame: np.ndarray) -> List[Vehicle]:
        """
        Detect vehicles in frame
        Mock implementation returns simulated detections
        """
        height, width = frame.shape[:2]
        vehicles = []

        # Simulate 3-5 detections per frame (mock)
        num_detections = np.random.randint(0, 5)

        for _ in range(num_detections):
            vehicle_type = np.random.choice(['car', 'truck', 'bus', 'motorcycle'])
            confidence = np.random.uniform(0.6, 0.99)

            if confidence >= self.confidence_threshold:
                x = np.random.randint(0, max(1, width - 100))
                y = np.random.randint(0, max(1, height - 100))
                w = np.random.randint(50, 150)
                h = np.random.randint(50, 130)

                vehicle = Vehicle(vehicle_type, confidence, (x, y, w, h))
                vehicles.append(vehicle)

        return vehicles

    def is_heavy_vehicle(self, vehicle: Vehicle) -> bool:
        """Check if vehicle is truck or bus"""
        return vehicle.vehicle_type in self.HEAVY_VEHICLES

    def detect_overtaking(self, prev_frame: np.ndarray, curr_frame: np.ndarray) -> Dict:
        """
        Detect overtaking pattern (mock)
        Returns: dict with overtaking detection info
        """
        # Simulate motion detection
        if prev_frame is None:
            return {'detected': False, 'confidence': 0}

        try:
            # Simple frame difference (mock motion detection)
            diff = cv2.absdiff(prev_frame, curr_frame)
            motion_area = np.sum(diff > 30)

            # Normalize to 0-1
            max_motion = prev_frame.shape[0] * prev_frame.shape[1] * 255
            motion_ratio = min(motion_area / max_motion, 1.0)

            # Detect overtaking if significant motion
            overtaking_detected = motion_ratio > 0.15

            return {
                'detected': overtaking_detected,
                'confidence': motion_ratio,
                'motion_ratio': motion_ratio,
                'severity': 'high' if overtaking_detected else 'low'
            }
        except Exception as e:
            print(f"Error in overtaking detection: {e}")
            return {'detected': False, 'confidence': 0}

    def extract_region(self, frame: np.ndarray, vehicle: Vehicle) -> np.ndarray:
        """Extract region of interest for vehicle"""
        x, y, w, h = vehicle.bbox
        return frame[y:y+h, x:x+w]

def analyze_frame(frame: np.ndarray, detector: VehicleDetectionModel) -> Dict:
    """
    Analyze single frame for violations
    """
    vehicles = detector.detect(frame)
    violations = []

    for vehicle in vehicles:
        if detector.is_heavy_vehicle(vehicle):
            # Check for violations specific to heavy vehicles
            violation = {
                'type': f'heavy_vehicle_{vehicle.vehicle_type}',
                'vehicle': vehicle.vehicle_type,
                'confidence': vehicle.confidence,
                'position': vehicle.position,
                'bbox': vehicle.bbox
            }
            violations.append(violation)

    return {
        'vehicles': [v.vehicle_type for v in vehicles],
        'violations': violations,
        'heavy_vehicle_count': sum(1 for v in vehicles if detector.is_heavy_vehicle(v))
    }
