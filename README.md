# Social Media API

A robust RESTful API for a social media platform built using Django and Django REST Framework (DRF). This API handles user authentication, post management, social interactions (likes, follows), and provides a personalized feed for users.

## Features

- **User Management**
    - User Registration and Login (Token-based Authentication).
    - Profile Management (Bio, Profile Picture).
    - Follow/Unfollow system.
- **Post Management**
    - Create, Read, Update, and Delete (CRUD) posts.
    - Support for text content and image uploads.
    - Feed generation based on followed users.
- **Interactions**
    - Like/Unlike posts.
    - Comment on posts.
- **Documentation**
    - Interactive API documentation using Swagger UI and Redoc.
- **Deployment Ready**
    - Configured for **PythonAnywhere**.

## Tech Stack

- **Backend Framework**: Django, Django REST Framework
- **Database**: SQLite (Default), can be configured for MySQL/PostgreSQL on PythonAnywhere.
- **Authentication**: Token Authentication (DRF)
- **Documentation**: drf-yasg (Swagger/Redoc)

## Getting Started Locally

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1.  **Clone the repository**
    ```bash
    git clone <repository-url>
    cd ALX_BACKEND_SOCIAL_MEDIA_API
    ```

2.  **Create a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser** (for Admin access)
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

The API will be available at `http://127.0.0.1:8000/`.

## Deployment on PythonAnywhere

This project is ready to be deployed on [PythonAnywhere](https://www.pythonanywhere.com/).

### Deployment Steps:
1.  **Sign up** for a PythonAnywhere account.
2.  Open a **Bash Console** on PythonAnywhere and clone your repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/ALX_BACKEND_SOCIAL_MEDIA_API.git
    ```
3.  **Create a Virtual Environment** on PythonAnywhere:
    ```bash
    cd ALX_BACKEND_SOCIAL_MEDIA_API
    mkvirtualenv --python=/usr/bin/python3.10 my-env
    pip install -r requirements.txt
    ```
4.  **Set up the Web App**:
    - Go to the **Web** tab.
    - Click **Add a new web app**.
    - Choose **Manual Configuration** (since we are setting up a virtualenv).
    - Select **Python 3.10** (or your matching version).
5.  **Configure WSGI**:
    - In the **Web** tab, click the link to edit your **WSGI configuration file**.
    - Delete the default content and uncomment the Django section.
    - Set the path to your project (e.g., `/home/yourusername/ALX_BACKEND_SOCIAL_MEDIA_API`).
    - Set the settings module: `social_media_api.settings`.
6.  **Configure Virtualenv**:
    - In the **Web** tab, under **Virtualenv**, enter the path to your environment (e.g., `/home/yourusername/.virtualenvs/my-env`).
7.  **Run Migrations**:
    - Go back to the Bash console and run:
    ```bash
    python manage.py migrate
    ```
8.  **Reload**:
    - Go key to the **Web** tab and click the **Reload** button.

Your API should now be live at `yourusername.pythonanywhere.com`.

## API Documentation

Once running, you can access the docs at:

-   **Swagger UI**: `/swagger/`
-   **Redoc**: `/redoc/`
