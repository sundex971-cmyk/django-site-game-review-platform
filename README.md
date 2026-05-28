# 🎮 Game Review Platform

Fullstack web application built with Django where users can browse games, search and filter titles, read reviews, and leave their own reviews after authentication.

---

# 🚀 Features

## 🔐 Authentication System

* User registration
* Login / Logout
* Session-based authentication
* Permissions for authorized users

---

## 🎮 Games Catalog

* Dynamic games list from database
* Search by title
* Genre filtering
* Game detail pages

---

## ⭐ Reviews System

* Users can leave reviews and ratings
* Reviews displayed on game pages
* Connected to both users and games
* Dynamic review rendering

---

## 🎨 Frontend

* Custom UI without Bootstrap
* Responsive layouts
* Modern dark theme

---

# 🛠 Tech Stack

* Python
* Django
* SQLite
* HTML5
* CSS3

---

# 📸 Screenshots

## Homepage

<img width="1920" height="1003" alt="image" src="https://github.com/user-attachments/assets/84770993-6562-407f-9e78-8d75d13831de" />

---

## Games Catalog

<img width="1890" height="753" alt="image" src="https://github.com/user-attachments/assets/0754865b-4f2b-410e-8889-8915c5591c88" />


<img width="1871" height="938" alt="image" src="https://github.com/user-attachments/assets/e21cb546-ee8c-487d-9384-83f3172d60c6" />


---

## Game Detail Page

<img width="1885" height="877" alt="image" src="https://github.com/user-attachments/assets/a037be4b-dc45-4af1-98e7-89c78c5bdeaa" />


---

## Authentication

<img width="1842" height="857" alt="image" src="https://github.com/user-attachments/assets/beeceaa4-d4c5-476d-a40d-fa2d93119872" />

<img width="1868" height="986" alt="image" src="https://github.com/user-attachments/assets/760cf189-8549-45d8-afc9-97b15f56dca7" />

---

# ⚙️ Installation

## 1. Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/django-game-review-platform.git
```

---

## 2. Open project folder

```bash
cd django-game-review-platform
```

---

## 3. Create virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Apply migrations

```bash
python manage.py migrate
```

---

## 6. Run server

```bash
python manage.py runserver
```

---

# 🔑 Admin Panel

To create admin account:

```bash
python manage.py createsuperuser
```

Admin panel available at:

```text
/admin/
```

---

# 📚 What I Learned

* Django project structure
* Authentication system
* Working with databases and models
* ForeignKey relationships
* Dynamic templates
* Search and filtering systems
* CRUD operations
* Backend/frontend integration

---

# 👨‍💻 Author

Roman Litvinschii
