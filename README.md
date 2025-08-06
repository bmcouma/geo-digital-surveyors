# Geo Digital Surveyors

Professional website for Geo Digital Surveyors built with Django, Bootstrap, and SQLite.

## 🏗️ Project Overview

Geo Digital Surveyors is a comprehensive web application for a land surveying company in Kenya. The website provides information about surveying services, showcases projects through a gallery, maintains a blog, and offers contact forms for client inquiries.

## ✨ Features

### Core Functionality
- **Home Page**: Hero section with company introduction and testimonials
- **About Page**: Company information and team details
- **Services Page**: Detailed service offerings with descriptions
- **Gallery**: Project showcase with image management
- **Contact Form**: Client inquiry submission with email notifications
- **Testimonials**: Client feedback system with approval workflow
- **Blog System**: Complete blog with categories, tags, comments, and likes
- **FAQ Section**: Frequently asked questions
- **Newsletter Subscription**: Email subscription system

### Technical Features
- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **Modern UI/UX**: Clean, professional design with animations
- **Admin Panel**: Comprehensive Django admin interface
- **SEO Optimized**: Meta tags, structured data, and clean URLs
- **Form Validation**: Client and server-side validation
- **AJAX Integration**: Dynamic interactions without page reloads
- **Image Management**: Upload and optimization for gallery and blog
- **Search Functionality**: Blog search and filtering
- **Comment System**: Nested comments with approval workflow

## 🛠️ Technology Stack

### Backend
- **Django 5.2.4**: Web framework
- **SQLite**: Database (can be easily migrated to PostgreSQL/MySQL)
- **Pillow**: Image processing
- **Python 3.8+**: Programming language

### Frontend
- **Bootstrap 5.3.3**: CSS framework
- **Bootstrap Icons**: Icon library
- **AOS (Animate On Scroll)**: Animation library
- **Google Fonts**: Typography (Poppins)
- **Vanilla JavaScript**: Interactive features

### Development Tools
- **Git**: Version control
- **Pip**: Package management
- **Virtual Environment**: Python environment isolation

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for version control)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd geo-digital-surveyors
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📁 Project Structure

```
geo-digital-surveyors/
├── geodigitalsurveyors/          # Main Django project
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Main URL configuration
│   ├── wsgi.py                   # WSGI configuration
│   └── asgi.py                   # ASGI configuration
├── geodigitalsurveyorsapp/       # Main Django app
│   ├── models.py                 # Database models
│   ├── views.py                  # View functions
│   ├── urls.py                   # App URL configuration
│   ├── forms.py                  # Form definitions
│   ├── admin.py                  # Admin interface
│   ├── templates/                # HTML templates
│   │   ├── base.html            # Base template
│   │   ├── home.html            # Home page
│   │   ├── about.html           # About page
│   │   ├── services.html        # Services page
│   │   ├── gallery.html         # Gallery page
│   │   ├── contact.html         # Contact page
│   │   ├── testimonials.html    # Testimonials page
│   │   ├── faqs.html            # FAQ page
│   │   ├── privacy.html         # Privacy policy
│   │   ├── terms.html           # Terms and conditions
│   │   ├── blog_detail.html     # Blog post detail
│   │   └── blog/                # Blog templates
│   │       ├── blog.html        # Blog listing
│   │       └── blog_create.html # Blog creation
│   └── static/                  # Static files (CSS, JS, images)
├── static/                       # Global static files
│   ├── css/
│   ├── js/
│   └── img/
├── media/                        # User-uploaded files
├── templates/                    # Global templates
├── manage.py                     # Django management script
├── requirements.txt              # Python dependencies
├── db.sqlite3                   # SQLite database
└── README.md                    # Project documentation
```

## 🗄️ Database Models

### Core Models
- **Service**: Company services with descriptions and icons
- **GalleryImage**: Project gallery images with titles and descriptions
- **ContactMessage**: Client contact form submissions
- **Testimonial**: Client testimonials with approval system
- **FAQ**: Frequently asked questions

### Blog Models
- **BlogCategory**: Blog post categories
- **BlogTag**: Blog post tags
- **BlogPost**: Main blog posts with content and metadata
- **Comment**: Blog comments with nested replies
- **Like**: Blog post likes tracking
- **Subscription**: Newsletter email subscriptions

## 🎨 Customization

### Styling
The project uses CSS custom properties (variables) for easy theming:

```css
:root {
  --primary-color: #145DA0;
  --secondary-color: #0C2D48;
  --accent-color: #2E8BC0;
  /* ... other variables */
}
```

### Adding New Pages
1. Create a new template in `geodigitalsurveyorsapp/templates/`
2. Add a view function in `views.py`
3. Add URL pattern in `urls.py`
4. Update navigation in `base.html`

### Adding New Models
1. Define model in `models.py`
2. Create and run migrations
3. Register in `admin.py`
4. Create forms in `forms.py` (if needed)

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database Configuration
The project uses SQLite by default. For production, consider PostgreSQL or MySQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False` in settings
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use environment variables for sensitive data
- [ ] Set up a production database (PostgreSQL/MySQL)
- [ ] Configure static file serving
- [ ] Set up email backend for contact forms
- [ ] Configure media file storage
- [ ] Set up SSL certificate
- [ ] Configure backup strategy

### Static Files
```bash
python manage.py collectstatic
```

### Database Backup
```bash
python manage.py dumpdata > backup.json
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support or questions, please contact:
- Email: info@geodigitalsurveyors.co.ke
- Phone: +254 799 187391

## 🙏 Acknowledgments

- Django community for the excellent web framework
- Bootstrap team for the responsive CSS framework
- All contributors and testers

---

**"Clients Opinion Matters"** - Geo Digital Surveyors
