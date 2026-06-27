# NewCommerce — Django E-Commerce Project

A multi-role e-commerce web application built with Django 5.2.

## Features
- Customer registration, login, and product browsing
- Seller registration, login, and product management
- Product variants (color, size, SKU)
- Product image uploads
- Role-based access control (customer / seller / admin)
- Django Admin panel

## Tech Stack
- Python 3.12
- Django 5.2.8
- SQLite3
- Bootstrap 4
- django-crispy-forms

## Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/Dhanush_TU/newcommerce.git
cd newcommerce

# 2. Create and activate virtual environment
python -m venv env
env\Scripts\activate        # Windows
source env/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py makemigrations account
python manage.py makemigrations sellar
python manage.py makemigrations core
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Run server
python manage.py runserver
```


