
# Flask User Authentication App

A simple Flask web application for user authentication, including registration, login, and dashboard functionality.

---

## **Features**
- **User Registration**: Users can register with a unique email address, name, and password.
- **User Login**: Registered users can log in with their email and password.
- **Dashboard**: Logged-in users can access a personalized dashboard.
- **Logout**: Users can log out to clear their session.
- **Session Management**: Secure session-based authentication to protect routes.

---

## **Technologies Used**
- **Flask**: A lightweight Python web framework.
- **SQLite**: A lightweight database for storing user information.
- **HTML/CSS**: Front-end templates for the user interface.
- **Jinja2**: Templating engine for rendering dynamic HTML pages.

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/flask-user-auth.git
cd flask-user-auth
```

### **2. Install Dependencies**
Make sure you have Python 3 installed. Then, install the required packages:
```bash
pip install Flask
```

### **3. Initialize the Database**
Run the Flask app to initialize the SQLite database:
```bash
python app.py
```
This will create a `database.db` file in your project directory.

### **4. Run the App**
Start the Flask development server:
```bash
python app.py
```
The app will be available at `http://127.0.0.1:5000`.

---

## **Usage**

### **Home Page**
- Access the home page at `http://127.0.0.1:5000/`.
- Links to `/login` and `/register`.

### **Register**
- Navigate to `http://127.0.0.1:5000/register`.
- Fill out the registration form to create a new account.

### **Login**
- Navigate to `http://127.0.0.1:5000/login`.
- Log in with your registered email and password.

### **Dashboard**
- After logging in, you will be redirected to `http://127.0.0.1:5000/dashboard`.
- View your profile information and log out.

### **Logout**
- Click the "Logout" link in the dashboard to log out.
- You will be redirected to the home page.

---

---

## **Contributing**
Contributions are welcome! Here’s how you can contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- Flask documentation: https://flask.palletsprojects.com/
- SQLite documentation: https://www.sqlite.org/docs.html

---
