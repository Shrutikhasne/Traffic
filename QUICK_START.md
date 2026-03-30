# RoadWatch AI - Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Prerequisites Check
- **Node.js 16+**: Check with `node --version`
- **Python 3.9+**: Check with `python --version`
- **MongoDB 5.0+**: Check with `mongod --version`

If not installed, download from:
- Node.js: https://nodejs.org/
- Python: https://www.python.org/downloads/
- MongoDB: https://www.mongodb.com/try/download/community

---

## ✅ Step-by-Step Setup

### 1️⃣ **Backend Setup** (5 minutes)

```bash
cd server

# Install dependencies
npm install

# Create .env file
copy .env.example .env

# Start MongoDB (in separate terminal)
mongod

# Start backend server
npm start
```

✅ Backend running at: **http://localhost:5000**

---

### 2️⃣ **Frontend Setup** (3 minutes)

```bash
cd ../client

# Install dependencies
npm install

# Create .env file
copy .env.example .env

# Start React app
npm start
```

✅ Frontend running at: **http://localhost:3000**

---

### 3️⃣ **AI Service Setup** (3 minutes)

```bash
cd ../ai-service

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Or (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env

# Start AI service
python app.py
```

✅ AI Service running at: **http://localhost:5001**

---

## 🎮 Test the Application

### Default Login Credentials
- **Phone**: `9123456789` (any 10-digit number works)
- **OTP**: `123456`
- **Name**: Your Name

### Test Flow

1. **Go to**: http://localhost:3000
2. **Enter phone**: 9123456789
3. **Click**: "Send OTP"
4. **Enter OTP**: 123456
5. **Enter name**: Test User
6. **Click**: "Verify OTP"
7. **Dashboard**: You're in! 🎉

### Try Features

- **Upload Video**: Go to Upload tab
- **View Profile**: Go to Profile tab
- **Admin Panel**: Set role to 'admin' in MongoDB
- **Check API**: Visit http://localhost:5000/api/health

---

## 📁 File Structure Reference

```
Traffic/
├── client/              # React Frontend
│   ├── src/
│   │   ├── pages/      # Login, Dashboard, Profile, Admin
│   │   ├── components/ # Cards, Navigation
│   │   ├── services/   # API calls, Auth
│   │   └── App.js
│   └── package.json
│
├── server/              # Node.js Backend
│   ├── models/         # User, Video, Violation DB schemas
│   ├── controllers/    # Business logic
│   ├── routes/         # API endpoints
│   ├── middleware/     # Auth check, errors
│   ├── server.js
│   └── package.json
│
├── ai-service/          # Python AI
│   ├── app.py          # Flask endpoints
│   ├── detection.py    # YOLOv8 detection
│   └── requirements.txt
│
└── README.md           # Full documentation
```

---

## 🐳 Using Docker (Alternative)

```bash
# Install Docker and Docker Compose

# Run everything at once
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

---

## 🔧 Troubleshooting

### Backend Won't Start
```
Error: Port 5000 in use
Solution: Kill process or change PORT in .env
```

### MongoDB Connection Failed
```
Error: connect ECONNREFUSED 127.0.0.1:27017
Solution: Make sure MongoDB is running
  mongod (Windows/Mac/Linux)
```

### Frontend Won't Load
```
Error: API connection refused
Solution: Check backend is running at localhost:5000
```

### Python/venv Issues
```
Error: 'python' not found
Solution: Use 'python3' instead or add Python to PATH
```

---

## 📊 API Endpoints Quick Reference

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/auth/send-otp` | POST | Send OTP |
| `/api/auth/verify-otp` | POST | Verify & Login |
| `/api/videos/upload` | POST | Upload video |
| `/api/violations/my-violations` | GET | Get violations |
| `/api/vehicles/verify` | POST | Verify vehicle |
| `/api/reports/create` | POST | Create report |
| `/api/admin/dashboard` | GET | Admin stats |

---

## 🔐 Environment Variables

### Backend (.env)
```env
PORT=5000
MONGODB_URI=mongodb://localhost:27017/roadwatch-ai
JWT_SECRET=your_secret_key
```

### Frontend (.env)
```env
REACT_APP_API_URL=http://localhost:5000/api
```

### AI Service (.env)
```env
AI_SERVICE_PORT=5001
DEBUG=True
```

---

## 📱 Mobile Testing

### Enable Mobile Dev Server
```bash
# Get your PC IP
ipconfig (Windows)
# or
ifconfig (Mac/Linux)

# Update frontend .env
REACT_APP_API_URL=http://YOUR_IP:5000/api

# Access from phone
http://YOUR_IP:3000
```

---

## 🧪 Test API with Postman

1. **Download Postman**: https://www.postman.com/downloads/
2. **Import Collection**: File → Import → [Create new from scratch]
3. **Create Requests**:

```
POST http://localhost:5000/api/auth/send-otp
{
  "phone": "9123456789"
}

GET http://localhost:5000/api/health
```

---

## 📝 Next Steps

1. ✅ Backend & Frontend running
2. ✅ Tested login
3. ⏭️ Upload a sample video
4. ⏭️ View violations in dashboard
5. ⏭️ Try creating a police report
6. ⏭️ Access admin panel

---

## 🆘 Need Help?

Check documentation:
- **Backend**: `server/README.md`
- **Frontend**: `client/README.md`
- **AI Service**: `ai-service/README.md`
- **Full Docs**: `README.md`
- **Sample API**: `SAMPLE_API_RESPONSES.md`

---

## 🎓 Learning Resources

- **React**: https://react.dev
- **Express.js**: https://expressjs.com
- **MongoDB**: https://docs.mongodb.com
- **Python Flask**: https://flask.palletsprojects.com
- **YOLOv8**: https://docs.ultralytics.com

---

## 🚀 Deployment

When ready for production:

1. **Backend**: Deploy to Heroku, Railway, or AWS
2. **Frontend**: Deploy to Vercel, Netlify, or GitHub Pages
3. **Database**: Use MongoDB Atlas cloud
4. **AI Service**: Deploy to EC2, Railway, or Google Cloud

---

## 📞 Support

For issues:
1. Check the troubleshooting section
2. Review error logs in terminal
3. Check browser console (F12)
4. Read full README.md

---

**Happy coding! 🚗 RoadWatch AI - Making Roads Safer** 🎉
