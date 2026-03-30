/**
 * Sample Test Cases & Mock Data
 * Use this for manual testing
 */

// SAMPLE 1: OTP Login Flow
POST /api/auth/send-otp
{
  "phone": "9123456789"
}

Response:
{
  "success": true,
  "message": "OTP sent successfully",
  "phone": "6789"
}

---

// SAMPLE 2: Verify OTP
POST /api/auth/verify-otp
{
  "phone": "9123456789",
  "otp": "123456",
  "name": "Raj Kumar"
}

Response:
{
  "success": true,
  "message": "Login successful",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": "507f1f77bcf86cd799439011",
    "name": "Raj Kumar",
    "phone": "9123456789",
    "role": "user",
    "isPhoneVerified": true
  }
}

---

// SAMPLE 3: Upload Video
POST /api/videos/upload
Headers: Authorization: Bearer <token>
Content-Type: multipart/form-data

Form Data:
- video: [binary file]
- latitude: 19.0760
- longitude: 72.8777
- city: Mumbai
- roadName: Eastern Express Highway
- state: Maharashtra

Response:
{
  "success": true,
  "message": "Video uploaded successfully",
  "video": {
    "id": "507f1f77bcf86cd799439012",
    "fileName": "dashcam_001.mp4",
    "uploadedAt": "2024-03-30T10:30:00.000Z",
    "processingStatus": "pending"
  }
}

---

// SAMPLE 4: Get User Videos
GET /api/videos/my-videos
Headers: Authorization: Bearer <token>

Response:
{
  "success": true,
  "count": 2,
  "videos": [
    {
      "_id": "507f1f77bcf86cd799439012",
      "fileName": "dashcam_001.mp4",
      "fileSize": 104857600,
      "uploadedAt": "2024-03-30T10:30:00.000Z",
      "gpsLocation": {
        "type": "Point",
        "coordinates": [72.8777, 19.0760]
      },
      "processingStatus": "completed",
      "aiAnalysisResult": {
        "violations": [
          {
            "type": "dangerous_overtaking",
            "duration": 2.5,
            "confidence": 0.92,
            "frameSnapshot": "base64_encoded..."
          }
        ],
        "vehiclesDetected": [
          {"type": "truck", "count": 3},
          {"type": "car", "count": 8}
        ],
        "processingTime": 12500
      }
    }
  ]
}

---

// SAMPLE 5: Get Violations
GET /api/violations/my-violations
Headers: Authorization: Bearer <token>

Response:
{
  "success": true,
  "count": 1,
  "violations": [
    {
      "_id": "507f1f77bcf86cd799439013",
      "videoId": "507f1f77bcf86cd799439012",
      "vehicleNumber": "MH-01-AB-1234",
      "vehicleType": "truck",
      "violationType": "overtaking",
      "location": {
        "type": "Point",
        "coordinates": [72.8777, 19.0760]
      },
      "detectionTime": "2024-03-30T10:32:00.000Z",
      "confidence": 92,
      "frameSnapshot": "base64_encoded...",
      "status": "pending_verification"
    }
  ]
}

---

// SAMPLE 6: Verify Vehicle (DigiLocker Mock)
POST /api/vehicles/verify
{
  "registrationNumber": "MH-01-AB-1234"
}

Response:
{
  "success": true,
  "verified": true,
  "message": "Vehicle details verified",
  "vehicle": {
    "_id": "507f1f77bcf86cd799439014",
    "registrationNumber": "MH-01-AB-1234",
    "ownerName": "John Doe",
    "ownerPhone": "9876543210",
    "vehicleType": "Heavy Goods Vehicle",
    "manufacturer": "Tata",
    "model": "LPT 1613",
    "color": "White",
    "registrationDate": "2018-06-15T00:00:00.000Z",
    "registrationExpiryDate": "2025-06-15T00:00:00.000Z",
    "insuranceProvider": "ICICI Lombard",
    "insuranceExpiryDate": "2025-12-31T00:00:00.000Z",
    "pollutionCertificateDate": "2025-03-31T00:00:00.000Z",
    "digiLockerVerified": true,
    "violationCount": 2
  }
}

---

// SAMPLE 7: Create Police Report
POST /api/reports/create
Headers: Authorization: Bearer <token>
{
  "violationId": "507f1f77bcf86cd799439013",
  "policeStation": "Traffic Police, Bandra"
}

Response:
{
  "success": true,
  "message": "Report created",
  "report": {
    "_id": "507f1f77bcf86cd799439015",
    "reportNumber": "RWA-1711861800000-1",
    "vehicleNumber": "MH-01-AB-1234",
    "violationType": "overtaking",
    "status": "draft",
    "policeStation": "Traffic Police, Bandra",
    "createdAt": "2024-03-30T10:30:00.000Z"
  }
}

---

// SAMPLE 8: Submit Report to Police
POST /api/reports/507f1f77bcf86cd799439015/submit
Headers: Authorization: Bearer <token>
{
  "policeOfficer": "Inspector Sharma"
}

Response:
{
  "success": true,
  "message": "Report submitted to police",
  "report": {
    "_id": "507f1f77bcf86cd799439015",
    "reportNumber": "RWA-1711861800000-1",
    "status": "submitted",
    "submittedAt": "2024-03-30T10:35:00.000Z",
    "policeOfficer": "Inspector Sharma"
  }
}

---

// SAMPLE 9: Admin Dashboard
GET /api/admin/dashboard
Headers: Authorization: Bearer <admin_token>

Response:
{
  "success": true,
  "stats": {
    "totalViolations": 45,
    "totalVideos": 28,
    "totalUsers": 150,
    "totalReports": 42,
    "todayViolations": 3,
    "pendingVerification": 5,
    "verifiedViolations": 35,
    "postedToPolice": 38
  }
}

---

// SAMPLE 10: Admin Analytics - Violations Per Day
GET /api/admin/analytics/violations-per-day
Headers: Authorization: Bearer <admin_token>

Response:
{
  "success": true,
  "data": [
    {"_id": "2024-03-01", "count": 2},
    {"_id": "2024-03-02", "count": 5},
    {"_id": "2024-03-03", "count": 3},
    ...
    {"_id": "2024-03-30", "count": 8}
  ]
}

---

// SAMPLE 11: AI Service - Process Video
POST /process
multipart/form-data:
  - file: [binary video]
  - video_id: 507f1f77bcf86cd799439012

Response:
{
  "success": true,
  "violations": [
    {
      "type": "dangerous_overtaking",
      "vehicle_type": "truck",
      "confidence": 0.92,
      "frame_number": 45,
      "timestamp": 1.8,
      "frame_snapshot": "abcd1234..."
    }
  ],
  "vehiclesDetected": [
    {"type": "truck", "count": 3},
    {"type": "car", "count": 8},
    {"type": "bus", "count": 1}
  ],
  "totalFramesProcessed": 300,
  "processingTime": 12.5,
  "timestamp": "2024-03-30T10:35:00.000Z"
}

---

// SAMPLE 12: AI Service - Detect Vehicles
POST /detect-vehicles
{
  "frame": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="
}

Response:
{
  "success": true,
  "detections": [
    {
      "vehicle_type": "truck",
      "confidence": 0.95,
      "bbox": [120, 150, 200, 180]
    },
    {
      "vehicle_type": "car",
      "confidence": 0.88,
      "bbox": [400, 200, 220, 160]
    }
  ],
  "timestamp": "2024-03-30T10:35:00.000Z"
}

---

// SAMPLE 13: Error Response
{
  "success": false,
  "message": "Invalid OTP"
}

// OR

{
  "success": false,
  "message": "Validation error",
  "errors": [
    "Phone number must be 10 digits"
  ]
}
