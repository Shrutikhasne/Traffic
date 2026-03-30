# RoadWatch AI - Frontend Documentation

## React Application

### Setup Instructions

```bash
npm install
npm start
```

### Environment Variables

```env
REACT_APP_API_URL=http://localhost:5000/api
REACT_APP_SOCKET_URL=http://localhost:5000
```

### Project Structure

```
src/
├── components/
│   ├── PrivateRoute.js       - Protected route wrapper
│   ├── BottomNav.js          - Mobile navigation
│   ├── ViolationCard.js      - Violation display component
│   └── ...
├── pages/
│   ├── LoginPage.js          - OTP login
│   ├── DashboardPage.js      - Main dashboard
│   ├── VideoUploadPage.js    - Video upload
│   ├── ViolationDetailsPage.js - Violation view
│   ├── ProfilePage.js        - User profile
│   ├── AdminDashboard.js     - Admin panel
│   └── ...
├── services/
│   ├── api.js                - API client
│   ├── authContext.js        - Auth state
│   └── ...
├── assets/                   - Images, fonts
├── App.js
└── index.js
```

### Key Components

**LoginPage**
- Phone number input
- OTP verification
- Name entry
- Auto-login on verification

**DashboardPage**
- Recent violations
- Video uploads
- Quick stats
- Navigation to details

**VideoUploadPage**
- Video file selection
- GPS location capture
- Metadata input
- Progress tracking

**ViolationDetailsPage**
- Full violation info
- Vehicle details
- Evidence snapshot
- Police report filing

**AdminDashboard**
- Pending violations
- Approve/reject interface
- Data export
- Analytics

### State Management

**AuthContext**
- User data
- JWT token
- Login/logout functions
- Token persistence

### Services

**api.js**
- Centralized API client with Axios
- Base URL configuration
- Request/response interceptors
- Grouped API methods

**authContext.js**
- Global authentication state
- Token management
- User persistence

### Styling with Tailwind CSS

- Dark blue theme (#1A3C6D)
- Red highlights for violations (#DC2626)
- Mobile-first responsive design
- Custom CSS in App.css

### Mobile Features

- Bottom navigation bar
- Touch-optimized buttons
- GPS geolocation
- Video camera integration

### Real-time Updates (Socket.io)

```javascript
// Listen for video processing completion
socket.on('video-processed', (data) => {
  // Update UI with results
});

// Listen for admin alerts
socket.on('violation-Alert', (data) => {
  // Show notification
});
```

---

## Component Examples

### ViolationCard Component
```javascript
<ViolationCard
  violation={{
    _id: '123',
    vehicleNumber: 'MH-01-AB-1234',
    vehicleType: 'truck',
    violationType: 'overtaking',
    confidence: 92,
    status: 'pending_verification',
    frameSnapshot: 'base64_image'
  }}
/>
```

### PrivateRoute Usage
```javascript
<Routes>
  <Route element={<PrivateRoute />}>
    <Route path="/dashboard" element={<DashboardPage />} />
  </Route>
</Routes>
```

---

## API Integration Pattern

```javascript
// Service method
export const violationAPI = {
  getUserViolations: () => api.get('/violations/my-violations')
};

// Component usage
const [violations, setViolations] = useState([]);
useEffect(() => {
  violationAPI.getUserViolations()
    .then(res => setViolations(res.data.violations))
    .catch(err => console.error(err));
}, []);
```

---

## Routing

- `/login` - Public login page
- `/dashboard` - User main dashboard
- `/upload` - Video upload
- `/violation/:id` - Violation details
- `/profile` - User profile
- `/admin` - Admin panel

Protected routes require valid JWT token.

---

## Deployment

```bash
# Build production bundle
npm run build

# Deploy to Vercel
vercel deploy

# Deploy to Netlify
netlify deploy --prod --dir=build
```

---

## Performance Optimization

- Code splitting with React.lazy()
- Image optimization
- Lazy loading of components
- Efficient API calls
- Local state management

---

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Android)

---

## Common Issues

**API Connection Error**
- Verify backend is running
- Check API_URL environment variable
- Check CORS settings

**Auth Token Expiration**
- Refresh token on expiry
- Force login when needed
- Clear storage on logout

**Video Upload Fails**
- Check file size (max 500MB)
- Verify video format (mp4, avi, etc.)
- Check internet connection

---

## Testing

```bash
# Run tests
npm test

# Build check
npm run build
```

---

## Development Tips

1. Use React DevTools extension
2. Check Network tab for API calls
3. Use console for debugging
4. Enable source maps in development
5. Test on actual mobile device using ngrok
