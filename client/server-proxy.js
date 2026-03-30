const express = require('express');
const path = require('path');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();
const PORT = process.env.PORT || 3000;

// Proxy API calls to backend
app.use('/api', createProxyMiddleware({
  target: 'http://localhost:5000',
  changeOrigin: true,
  pathRewrite: {
    '^/api': '/api'
  }
}));

// Serve static files from public directory
app.use(express.static(path.join(__dirname, 'public')));

// Serve index.html for all non-API routes (SPA)
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`🚀 RoadWatch AI Frontend running on port ${PORT}`);
  console.log(`📱 Access the app at http://localhost:${PORT}`);
  console.log(`🔗 Backend API: http://localhost:5000`);
  console.log(`⚙️ AI Service: http://localhost:5001`);
});
