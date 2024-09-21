# Login_Authenticator_Project_SQL-Python

Project Overview
This project is a simple user registration and login application built using Python's Tkinter library for the graphical user interface and MySQL for the database. Users can register by providing a username and password, and then log in using those credentials.

Prerequisites
Before you begin, ensure you have the following installed:

Python 3.x
MySQL Server
mysql-connector-python library
Tkinter (usually comes pre-installed with Python)
To install the MySQL connector, you can use pip:

bash
Copy code
pip install mysql-connector-python
Database Setup
Create Database and Table: Ensure you have a MySQL database named kareem. You can create it using the following SQL commands:

sql
Copy code
CREATE DATABASE kareem;

USE kareem;

CREATE TABLE reg_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
User Permissions: Make sure that the MySQL user root has access to the kareem database. You can change the user and password in the code if needed.

Code Explanation
The application consists of two main functions:

register_user()
Retrieves the username and password from the input fields.
Connects to the MySQL database and inserts the new user into reg_table.
Displays a success message or an error message based on the outcome.
login_user()
Retrieves the username and password from the login input fields.
Queries the reg_table to check if the credentials are valid.
Displays a success or error message accordingly.
GUI Components
The application window is created using Tkinter.
It contains labels and entry fields for username and password, along with buttons for registration and login.
Running the Application
Clone or download the project files.
Ensure your MySQL server is running.
Update the database connection parameters if necessary.
Run the application:
bash
Copy code
python your_script_name.py
Use the GUI to register a new user and then log in with the same credentials.
Notes
Passwords are stored in plaintext in the database for simplicity. For a production environment, consider using hashed passwords with a library like bcrypt.
Ensure your MySQL server is secured and not exposed to the public internet.
Troubleshooting
If you encounter a connection error, verify your MySQL server status and credentials.
Check the console for any printed error messages to help diagnose issues.
License
This project is open-source and can be freely modified and distributed.
