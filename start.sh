#!/bin/bash

# RoadWatch AI - Quick Start Script
# Starts all three services in separate terminal windows

echo "🚀 Starting RoadWatch AI Application..."

# Start MongoDB
echo "📦 Starting MongoDB..."
mongod --dbpath ./data &

# Start Backend
echo "🔧 Starting Backend Server..."
cd server
npm install
npm start &

# Start Frontend
echo "⚛️ Starting Frontend..."
cd ../client
npm install
npm start &

# Start AI Service
echo "🤖 Starting AI Service..."
cd ../ai-service
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py &

echo ""
echo "✅ All services started!"
echo ""
echo "📍 Access points:"
echo "   Frontend:   http://localhost:3000"
echo "   Backend:    http://localhost:5000"
echo "   AI Service: http://localhost:5001"
echo ""
echo "📝 Demo Credentials:"
echo "   Phone: 9123456789"
echo "   OTP: 123456"
