# 📱 Social Media Dashboard

A comprehensive analytics dashboard for managing and analyzing social media accounts. Built with Vue.js and Django, this platform provides real-time insights, scheduling capabilities, and multi-platform integration.

## ✨ Features

- 📊 **Analytics Dashboard**: Real-time metrics and insights
- 📅 **Content Scheduling**: Plan and schedule posts across platforms
- 🔗 **Multi-Platform Support**: Instagram, Twitter, Facebook, LinkedIn
- 📈 **Performance Tracking**: Engagement rates, reach, impressions
- 🎨 **Visual Reports**: Interactive charts and graphs
- 🔐 **OAuth Authentication**: Secure login with social providers
- 👥 **Team Collaboration**: Multi-user support with roles
- 📱 **Mobile Responsive**: Works on all devices
- 🔔 **Notifications**: Real-time alerts and updates
- 📊 **Export Data**: CSV, PDF, Excel exports

## 🛠️ Tech Stack

### Frontend
- **Vue.js 3** with Composition API
- **Vuetify** for UI components
- **Chart.js** for data visualization
- **Vuex** for state management
- **Axios** for API calls
- **Vue Router** for navigation

### Backend
- **Django 4** with Django REST Framework
- **PostgreSQL** for data storage
- **Celery** for background tasks
- **Redis** for caching
- **JWT** authentication
- **OAuth 2.0** integration

### Integrations
- Instagram Graph API
- Twitter API v2
- Facebook Marketing API
- LinkedIn API

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL 14+
- Redis 6+

### Installation

```bash
# Clone the repository
git clone https://github.com/L8ab/social-media-dashboard.git
cd social-media-dashboard

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend setup (in new terminal)
cd frontend
npm install
npm run serve
```

### Environment Variables

```env
# Backend (.env)
DATABASE_URL=postgresql://user:pass@localhost/dbname
REDIS_URL=redis://localhost:6379
SECRET_KEY=your_secret_key
INSTAGRAM_CLIENT_ID=your_instagram_client_id
TWITTER_API_KEY=your_twitter_api_key

# Frontend (.env)
VUE_APP_API_URL=http://localhost:8000/api
```

## 📁 Project Structure

```
social-media-dashboard/
├── backend/                # Django backend
│   ├── accounts/           # User management
│   ├── analytics/          # Analytics logic
│   ├── scheduler/          # Content scheduling
│   └── integrations/       # Social media APIs
├── frontend/               # Vue.js frontend
│   ├── components/         # Vue components
│   ├── views/              # Page views
│   ├── store/              # Vuex store
│   └── services/           # API services
└── docs/                   # Documentation
```

## 🎯 Key Features

### Analytics Dashboard
- Real-time follower growth
- Engagement rate calculations
- Best posting times analysis
- Content performance metrics
- Audience demographics

### Content Scheduler
- Visual calendar interface
- Bulk upload support
- Auto-posting capabilities
- Content library management
- Preview before posting

### Multi-Platform Management
- Unified interface for all platforms
- Cross-platform posting
- Platform-specific optimizations
- Hashtag suggestions
- Content recommendations

## 📊 API Endpoints

- `GET /api/analytics/overview` - Dashboard overview
- `GET /api/posts/` - List all posts
- `POST /api/posts/schedule` - Schedule new post
- `GET /api/accounts/` - Connected accounts
- `GET /api/reports/` - Generate reports

## 🧪 Testing

```bash
# Backend tests
cd backend
python manage.py test

# Frontend tests
cd frontend
npm run test:unit
npm run test:e2e
```

## 📈 Performance Metrics

- Dashboard load time: < 2s
- Real-time updates: < 500ms latency
- API response time: < 300ms
- Supports 10,000+ posts

## 🔒 Security

- JWT token-based authentication
- OAuth 2.0 for social logins
- Rate limiting on API endpoints
- Data encryption at rest
- HTTPS only in production

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

MIT License - see LICENSE file for details

## 👤 Author

**L8ab**
- GitHub: [@L8ab](https://github.com/L8ab)
- Email: L8ab@proton.me
- Instagram: [@L8ab](https://www.instagram.com/L8ab)

---

**POWERED BY L8AB SYSTEMS** ⚡

