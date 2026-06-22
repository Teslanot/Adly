# Adly – Django Classified Ads Platform

Welcome to my first Django project! A modern classifieds website where users can:

- Register and log in to their profile
- Post listings with images
- Add listings to favourites
- View top users by number of posts
- Browse listings added today or this week
- Log out and see their username

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/AlekseevDaniel/Adly.git
cd Adly
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file and add the following:
```ini
TOKEN=your_django_secret_key
EMAIL_USER=example@email.com
EMAIL_PASSWORD=aaaa bbbb cccc dddd
```

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Collect static files
```bash
python manage.py collectstatic
```

### 7. Run the development server
```bash
python manage.py runserver
```

---

## Production Deployment (Gunicorn + Nginx)

1. Update `settings.py`:
   - `DEBUG = False`
   - `ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']`

2. Install Gunicorn:
```bash
pip install gunicorn
```

3. Start the application:
```bash
gunicorn yourproject.wsgi:application --bind 0.0.0.0:8000
```

4. Configure `nginx` and `supervisor` (optional)

---

## Planned Features

- Public user profiles for contacting sellers
- Social account linking (Telegram, etc.)

---

## Project Structure
```
adboard/
│
├── add/               # Listings app
├── auth/              # Registration & authentication
├── main/              # Core Django folder
├── templates/         # HTML templates
├── static/            # Static files (Tailwind CSS, JS)
├── media/             # User and listing images
├── manage.py          # Entry point
├── .env               # Secret keys (not committed)
└── ...
```

---

## Dependencies

- Python 3.10+
- Django 4.x+
- Pillow
- Tailwind CSS (via CLI or CDN)
- Gunicorn (for deployment)

Full list in `requirements.txt`.

---

## 📄 License

MIT License — free to use, copy, modify and distribute with attribution.

---

## 👤 Author

Built from scratch with Django ❤️  
**Dan (AlekseevDaniel)** · [github.com/AlekseevDaniel](https://github.com/AlekseevDaniel)

Found a bug or have an idea? Open an Issue or Pull Request.

---
