# RoadWatch AI - Full Stack Application

🚗 A comprehensive traffic violation detection system using AI, mobile uploads, and police integration.

## Features

### 1. **User Authentication**
- OTP-based SMS login (phone number)
- JWT token authentication
- Profile management with vehicle and license info
- Role-based access (user, admin, police)

### 2. **Video Management**
- Upload dashcam videos with GPS tagging
- Auto-timestamping and metadata capture
- Video processing queue with status tracking
- Support for multiple video formats

### 3. **AI Violation Detection**
- **YOLOv8-based vehicle detection**
  - Truck, bus, car, motorcycle detection
  - Real-time frame analysis
- **Dangerous overtaking detection**
  - Motion pattern analysis
  - Multi-vehicle tracking
- **License plate extraction** (OCR)
  - Mock Tesseract integration
- **Confidence scoring** for each detection

### 4. **Vehicle Identification**
- DigiLocker API integration (mock)
- Vehicle details verification
- Insurance and pollution certificate validation
- Vehicle violation history tracking
- Blacklist management for repeat offenders

### 5. **Evidence Dashboard**
- Video preview with violation highlights
- Vehicle and driver information
- Location mapping (Google Maps API mock)
- Time and date stamping
- AI confidence percentage display
- Status tracking (Pending → Verified → Sent to Police)

### 6. **Police Report System**
- Generate formal complaint documents
- Attach video evidence
- Vehicle detail compilation
- One-click submission to police stations
- Report number generation and tracking
- Officer assignment

### 7. **Admin Panel**
- Dashboard with KPI metrics
- Pending violation review and verification
- Approve/reject AI detections
- Manual verification override
- Blacklist management
- System analytics

### 8. **Analytics Dashboard**
- Violations per day (30-day trend)
- Vehicle type statistics
- Violation type breakdown
- Traffic hotspots (geospatial)
- Top repeat offenders
- Report status pipeline

### 9. **Real-time Notifications**
- Socket.io integration for live updates
- Video processing status
- Violation alerts
- Report updates

### 10. **Extra Features**
- Offline mode with sync capability
- Video compression before upload
- Notification system
- Data export (JSON)
- Responsive mobile-first design

---

## Tech Stack

### Frontend
- **React.js 18** - UI library
- **Tailwind CSS** - Styling
- **React Router v6** - Navigation
- **Axios** - HTTP client
- **Socket.io Client** - Real-time updates
- **React Icons** - Icon library

### Backend
- **Node.js + Express.js** - API server
- **MongoDB** - Database
- **Mongoose** - ODM
- **JWT** - Authentication
- **Socket.io** - Real-time communication
- **Multer** - File uploads

### AI Service
- **Python 3.9+** - Language
- **Flask** - Web framework
- **OpenCV** - Video processing
- **YOLOv8** (mock) - Object detection
- **NumPy** - Numerical computing

---

## Folder Structure

```
Traffic/
├── client/                    # React Frontend
│   ├── src/
│   │   ├── components/       # Reusable components
│   │   ├── pages/            # Page components
│   │   ├── services/         # API & Auth services
│   │   ├── assets/           # Images, fonts
│   │   ├── App.js
│   │   └── index.js
│   ├── public/
│   ├── package.json
│   └── .env.example
│
├── server/                    # Node.js Backend
│   ├── models/               # MongoDB schemas
│   ├── controllers/          # Business logic
│   ├── routes/               # API endpoints
│   ├── middleware/           # Custom middleware
│   ├── server.js             # Entry point
│   ├── package.json
│   └── .env.example
│
└── ai-service/               # Python Flask
    ├── app.py               # Main Flask app
    ├── detection.py         # YOLOv8 wrapper
    ├── requirements.txt
    └── .env.example
```

---

## Installation & Setup

### Prerequisites
- Node.js 16+ and npm
- Python 3.9+
- MongoDB 5.0+
- Git

### 1. Clone Repository
```bash
cd Traffic
```

### 2. Backend Setup

```bash
cd server

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Edit .env with your configuration
# Important: Add MongoDB URI, JWT secret, API keys

# Start backend
npm start  # Production
npm run dev  # Development with nodemon
```

**Backend runs on:** `http://localhost:5000`

### 3. Frontend Setup

```bash
cd ../client

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Edit .env
REACT_APP_API_URL=http://localhost:5000/api

# Start frontend
npm start
```

**Frontend runs on:** `http://localhost:3000`

### 4. AI Service Setup

```bash
cd ../ai-service

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Start AI service
python app.py
```

**AI Service runs on:** `http://localhost:5001`

---

## API Endpoints

### Authentication
```
POST   /api/auth/send-otp          → Send OTP to phone
POST   /api/auth/verify-otp        → Verify OTP & login
GET    /api/auth/profile           → Get user profile
PUT    /api/auth/profile           → Update profile
```

### Videos
```
POST   /api/videos/upload          → Upload video
GET    /api/videos/my-videos       → Get user's videos
GET    /api/videos/:videoId        → Get video details
GET    /api/videos/hotspots/nearby → Get videos by location
```

### Violations
```
GET    /api/violations/my-violations        → Get user's violations
GET    /api/violations/pending              → Get pending (admin)
PUT    /api/violations/:id/verify           → Verify violation (admin)
GET    /api/violations/stats                → Get statistics
GET    /api/violations/nearby               → Get violations by location
```

### Vehicles
```
POST   /api/vehicles/verify                 → Verify via DigiLocker
GET    /api/vehicles/:registration          → Get vehicle details
GET    /api/vehicles/:registration/violations → Vehicle history
PUT    /api/vehicles/:registration/blacklist → Blacklist vehicle (admin)
GET    /api/vehicles/blacklist/list         → Get blacklisted (admin)
```

### Reports
```
POST   /api/reports/create                  → Create report
POST   /api/reports/:id/submit              → Submit to police
GET    /api/reports/my-reports              → Get user reports
GET    /api/reports/:id                     → Get report details
GET    /api/reports/all                     → Get all (admin/police)
```

### Admin
```
GET    /api/admin/dashboard                      → Dashboard stats
GET    /api/admin/analytics/violations-per-day  → 30-day trend
GET    /api/admin/analytics/vehicle-types       → Vehicle stats
GET    /api/admin/analytics/hotspots            → Top locations
GET    /api/admin/analytics/violation-types     → Type breakdown
GET    /api/admin/analytics/report-status       → Report pipeline
GET    /api/admin/analytics/top-violators       → Repeat offenders
GET    /api/admin/export                        → Export data (JSON)
```

### AI Service
```
GET    /health                    → Health check
POST   /process                   → Process video
POST   /detect-vehicles          → Detect in frame
POST   /ocr/extract-plate        → Extract license plate
```

---

## Sample Test Data

### Demo Login
- Phone: `9123456789` (any 10-digit number)
- OTP: `123456`
- Name: Test User

### Sample Vehicle Number
- `MH-01-AB-1234`
- `HR-26-GJ-5678`
- `DL-12-CD-9999`

### Sample DigiLocker Response
```json
{
  "registrationNumber": "MH-01-AB-1234",
  "ownerName": "John Doe",
  "vehicleType": "Heavy Goods Vehicle",
  "manufacturer": "Tata",
  "model": "LPT 1613",
  "registrationExpiryDate": "2025-06-15",
  "insuranceExpiryDate": "2025-12-31"
}
```

### Sample AI Detection Output
```json
{
  "violations": [
    {
      "type": "dangerous_overtaking",
      "vehicleType": "truck",
      "confidence": 0.92,
      "frameNumber": 45,
      "timestamp": 1.8,
      "frameSnapshot": "base64_encoded_image"
    }
  ],
  "vehiclesDetected": [
    {"type": "truck", "count": 3},
    {"type": "car", "count": 8},
    {"type": "bus", "count": 1}
  ],
  "totalFramesProcessed": 300,
  "processingTime": 12.5
}
```

---

## Features in Detail

### Violation Detection Algorithm
1. **Frame Sampling**: Process every 5th frame for performance
2. **Vehicle Detection**: YOLOv8 identifies vehicle class & position
3. **Classification**: Filter for trucks/buses
4. **Motion Analysis**: Compare consecutive frames for overtaking
5. **Confidence Scoring**: Combine detection & motion confidence
6. **License Plate**: Extract region using bounding box

### DigiLocker Integration (Mock)
- Returns vehicle owner details
- Insurance verification
- Pollution certificate validation
- Response cached for 24 hours

### Admin Verification Workflow
1. AI detects violation with confidence score
2. Admin reviews frame snapshot
3. Can approve (add to police queue) or reject
4. Rejected violations are logged for model improvement

---

## Deployment

### Backend (Heroku/Railway)
```bash
# Set environment variables
# Deploy with MongoDB Atlas

# Deploy command
git push heroku main
```

### Frontend (Vercel/Netlify)
```bash
# Deploy with:
npm run build
# Upload build/ folder
```

### AI Service (EC2/Railway)
```bash
# Use Gunicorn for production
gunicorn -w 4 app:app
```

---

## Security Considerations

✓ JWT authentication for all protected routes
✓ Role-based access control (RBAC)
✓ Password hashing with bcryptjs
✓ CORS enabled for frontend
✓ Input validation on all endpoints
✓ Rate limiting (implement as needed)
✓ File upload restrictions
✓ HTTPS for production

---

## Performance Optimizations

- Video frame sampling (process every 5th frame)
- Image compression before upload
- Database indexing on geospatial queries
- Redis caching (optional)
- CDN for video streaming
- Batch processing for background jobs

---

## Future Enhancements

1. Real YOLOv8 model integration
2. Tesseract OCR for accurate plate reading
3. Multi-language support
4. SMS/WhatsApp notifications
5. Mobile app (React Native)
6. Real-time livestream processing
7. TensorFlow Lite for edge processing
8. Automated fine generation
9. Police department integration API
10. Insurance premium calculation

---

## Support & Documentation

- **Backend Docs**: See `server/README.md`
- **Frontend Docs**: See `client/README.md`
- **AI Service Docs**: See `ai-service/README.md`
- **API Documentation**: Postman collection available

---

## License

MIT License - See LICENSE file

---

## Authors

RoadWatch AI Development Team

Built for traffic safety and violation detection using 🤖 AI & 📱 mobile technology.
