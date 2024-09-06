
# OLE-pâtisserie Project

## Course: Web Systems Development

---

## Project Overview
OLE-pâtisserie is a web-based application designed to facilitate the management of a patisserie shop. The system allows customers to place orders online, view products, and submit reviews. Additionally, the system provides administrative functionalities to manage orders and customer feedback. The project is developed using a combination of Python (Flask), JavaScript (Node.js), and MongoDB for the backend, and HTML/CSS for the frontend.

### Key Features:
- **Customer Registration/Login**: Users can register and log into the system.
- **Order Management**: Customers can browse the product catalog, add items to their cart, and place orders.
- **Admin Management**: Admins can view open orders, close completed orders, and review customer feedback.
- **Customer Feedback**: Users can submit reviews and feedback on their shopping experience.

---

## Detailed Explanation of Core Files

### 1. `app.py`
The `app.py` file is the core Python file for the backend of the application. It uses the Flask framework to handle web requests and manage communication between the frontend and the MongoDB database.

#### Libraries Used:
- **Flask**: Used to create web applications. It handles HTTP requests and routes, rendering HTML templates, and redirects.
- **PyMongo**: Connects the Flask app to the MongoDB database.
- **Flask_login**: Manages user login/logout functionality.
- **Werkzeug**: Provides password encryption and utilities for secure file uploads.

#### Key Functionalities:
- **User Registration/Login**: Users can register, log in, and log out of the system.
- **Order Management**: Users can place new orders, which are stored in the MongoDB database.
- **Feedback System**: Users can submit feedback, which is stored in the database for admin review.

---

### 2. `server.js`
The `server.js` file is responsible for managing the backend using Node.js. It handles the communication between the frontend and MongoDB, as well as the REST API for fetching and updating order data.

#### Key Functionalities:
- **Order Placement**: The server accepts customer orders and stores them in the database.
- **Order Retrieval**: The server retrieves orders for both customers and admins.
- **Order Status Updates**: Admins can update the status of orders to indicate whether they are open or closed.

---

### 3. `database.py`
The `database.py` file handles all the database operations using PyMongo. It contains functions that allow the app to insert and retrieve data from MongoDB, ensuring data is stored efficiently and retrieved as needed.

#### Key Functions:
- **User Management**: Handles inserting new users and validating login credentials.
- **Order Management**: Handles storing and retrieving customer orders.
- **Feedback Management**: Handles storing and retrieving customer feedback.

---

### 4. `templates/`
This directory contains the HTML templates for the app's user interface. Flask uses these templates to render the views for customers and admins. The templates are designed with Bootstrap for responsive, user-friendly interfaces.

---

### 5. `static/`
The `static/` folder contains static assets such as CSS files, JavaScript files, and images. These files are responsible for the frontend's look and feel.

---

## How to Run the Project

### Prerequisites:
- Python 3.x
- Node.js
- MongoDB
- Flask
- PyMongo

### Setup:
1. Clone the repository to your local machine.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Start MongoDB locally.
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. For the Node.js server, navigate to the directory and run:
   ```bash
   node server.js
   ```
6. Open your browser and navigate to `http://localhost:5000` to access the app.

---

## Future Improvements
- **Product Recommendations**: Implement a recommendation system based on user purchase history.
- **Advanced Admin Panel**: Develop an admin panel with additional features like product management, order history, and analytics.
- **Payment Integration**: Add integration for online payments.

## Conclusion
OLE-pâtisserie is a robust web application that combines Flask, Node.js, and MongoDB to create a seamless experience for both customers and admins. The project demonstrates effective use of backend technologies, database management, and frontend development to manage a patisserie business efficiently.

## Video of this Project
https://youtu.be/PrMNnWrNdgw/

