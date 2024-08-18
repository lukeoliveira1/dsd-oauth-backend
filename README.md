# OAuth Backend

This project is a Django Rest Framework API that provides OAuth authentication using GitHub and Google. <br/>
Integrated with the **getmovies-nextjs** repository, it will offer a complete solution for authentication and authorization.

## Technologies Used

- **Django Rest Framework (DRF)**: Framework for creating RESTful APIs.
- **dj-rest-auth**: Library for authentication and session management.
- **django-allauth**: Third-party authentication system for Django.
- **djangorestframework-simplejwt**: JWT (JSON Web Token) implementation for authentication.
- **drf-spectacular**: OpenAPI schema generator for DRF.

## Setup

### Create and Activate a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Create .env with Environment Variables
```
GITHUB_CLIENT_ID
GITHUB_CLIENT_SECRET
GITHUB_CALLBACK_URL
GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET
GOOGLE_CALLBACK_URL
```

### Apply Migrations
```
python manage.py migrate
```

### Create a Superuser
```
python manage.py createsuperuser
```
