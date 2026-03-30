# RoadWatch AI - Backend Documentation

## Express.js API Server

### Setup Instructions

```bash
npm install
npm run dev
```

### Environment Variables

```env
PORT=5000
MONGODB_URI=mongodb://localhost:27017/roadwatch-ai
JWT_SECRET=your_secret_key
JWT_EXPIRE=7d
DIGILOCKER_API_URL=https://api.digilocker.gov.in
AI_SERVICE_URL=http://localhost:5001
NODE_ENV=development
```

### Database Models

#### User
- Phone (unique)
- Name
- Email
- License details
- Vehicle list
- OTP verification
- Role (user/admin/police)

#### Video
- User reference
- File metadata
- GPS location
- Processing status
- AI analysis results
- Timestamp

#### Violation
- Video reference
- Vehicle number
- Detection confidence
- Location
- Vehicle & violation type
- Admin verification status

#### Vehicle
- Registration number
- Owner details
- Insurance info
- DigiLocker verification
- Violation history
- Blacklist status

#### Report
- Violation reference
- Police station
- Report status
- Evidence links
- Case number

### Key Controllers

**authController.js**
- OTP generation & verification
- Profile management
- Token generation

**videoController.js**
- Video uploading
- Status tracking
- AI service integration

**violationController.js**
- Violation listing
- Admin verification
- Statistics generation

**vehicleController.js**
- DigiLocker verification
- Vehicle history
- Blacklist management

**reportController.js**
- Report generation
- Police submission
- Tracking

**adminController.js**
- Dashboard analytics
- Data export
- Hotspot analysis

### Middleware

**authMiddleware.js**
- JWT verification
- Role checking (admin/police)

**errorHandler.js**
- Centralized error handling
- Consistent error responses

### Real-time Features (Socket.io)

- Video processing status updates
- Violation alerts
- New report notifications
- Admin alerts

---

## Testing

```bash
# Using Postman or Thunder Client

# 1. Send OTP
POST /api/auth/send-otp
{
  "phone": "9123456789"
}

# 2. Verify OTP
POST /api/auth/verify-otp
{
  "phone": "9123456789",
  "otp": "123456",
  "name": "John Doe"
}

# 3. Upload Video
POST /api/videos/upload
Headers: Authorization: Bearer <token>
Form-Data:
  - video: <file>
  - latitude: 19.0760
  - longitude: 72.8777

# 4. Get Violations
GET /api/violations/my-violations
Headers: Authorization: Bearer <token>
```

---

## Common Issues

**MongoDB Connection Error**
- Ensure MongoDB is running (`mongod`)
- Check connection string in .env

**CORS Issues**
- Update frontend URL in CORS config
- Allow credentials if needed

**File Upload Fails**
- Check `uploads/videos` directory exists
- Verify file size limits
- Check disk space

---

## Production Deployment

```bash
# Install production dependencies
NODE_ENV=production npm install

# Use PM2 for process management
npm install -g pm2
pm2 start server.js

# Set up reverse proxy (Nginx)
# Configure SSL/TLS certificates
# Set up database backups
```

---

## API Response Format

### Success Response
```json
{
  "success": true,
  "message": "Operation successful",
  "data": { ... }
}
```

### Error Response
```json
{
  "success": false,
  "message": "Error description",
  "errors": [ ... ]
}
```
