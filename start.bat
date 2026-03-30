@echo off
REM RoadWatch AI - Quick Start Script (Windows)
REM Starts all three services in separate command windows

echo Starting RoadWatch AI Application on Windows...

REM Start MongoDB
echo Starting MongoDB...
start "MongoDB" mongod --dbpath ./data

REM Start Backend
echo Starting Backend Server...
start "Backend" cmd /k "cd server && npm install && npm run dev"

REM Start Frontend
echo Starting Frontend...
start "Frontend" cmd /k "cd client && npm install && npm start"

REM Start AI Service
echo Starting AI Service...
start "AI Service" cmd /k "cd ai-service && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && python app.py"

echo.
echo All services started!
echo.
echo Access points:
echo   Frontend:   http://localhost:3000
echo   Backend:    http://localhost:5000
echo   AI Service: http://localhost:5001
echo.
echo Demo Credentials:
echo   Phone: 9123456789
echo   OTP: 123456
