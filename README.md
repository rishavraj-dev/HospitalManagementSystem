# 🏥 Hospital Management System (Python + MySQL)

## 📌 Project Title
**Hospital Management System – Terminal Based (Python + MySQL)**



## 📌 Overview of the Project
This project is a simple, menu-driven **Hospital Management System** developed using **Python** and **MySQL**.  
It allows hospital staff to manage **patients**, **beds**, and **drugs** using a terminal interface.

The system supports basic CRUD (Create, Read, Update, Delete) operations and is made as a beginner-friendly mini project.



## Features

### Patient Module
- Add a new patient  
- View all patients  
- Update patient details  
- Export patient data to CSV  

### Bed Module
- Add new beds  
- View bed status  
- Assign beds to patients  
- Free beds  
- Export bed data to CSV  

### Drug Module
- Add new drug  
- View drug list  
- Update drug details  
- Export drugs to CSV  

---

## 🛠 Technologies / Tools Used
- **Python 3.x**
- **MySQL Server**
- **MySQL Workbench**
- **mysql-connector-python** library
- Terminal/Command Prompt

---

## 🛠 Steps to Install & Run the Project
### 1. Clone the Repository

git clone https://github.com/rishavraj-dev/HospitalManagementSystem
cd HospitalManagementSystem

### 2. Install Required Python Package
Install the MySQL connector library (make sure Python 3.12 or later  is installed).

pip install mysql-connector-python

### 3. Create MySQL Database
In MySQL Workbench (or via CLI):
```sql
CREATE DATABASE hospital_db;
USE hospital_db;
```

### 4. Create Required Tables
Run these SQL statements inside the `hospital_db` database:
```sql
CREATE TABLE patients(
	patient_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100),
	age INT,
	gender VARCHAR(10),
	phone VARCHAR(20),
	address VARCHAR(200),
	disease VARCHAR(200),
	admit_date DATE,
	discharge_date DATE
);

CREATE TABLE beds(
	bed_id INT PRIMARY KEY,
	ward_type VARCHAR(50),
	status VARCHAR(20),
	current_patient_id INT
);

CREATE TABLE drugs(
	drug_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100),
	type VARCHAR(50),
	stock_qty INT,
	price DECIMAL(10,2),
	expiry_date DATE
);
```

### 5. Update MySQL Credentials
Edit the file `connection.py` and change the username/password (and optionally host) to match your local MySQL setup.
Example:
```python
connection = mysql.connector.connect(
	host="localhost",
	user="root",
	password="<your-password>",
	database="hospital_db"
)
```

### 6. Run the Project
From the project directory:
```
python main.py
```

### 7. Instructions for Testing
- Start program with `python main.py`
- Choose a module (Patients / Beds / Drugs)
- Add sample entries
- Try updating records
- Export CSV files from each module
- Verify CSV files appear in the project folder

### 📸 Screenshots (Optional)
You can capture terminal output and MySQL Workbench table views for documentation.

### 👤 Author
Rishav Raj  
B.Tech CSE (Core) — VIT Bhopal University

---

Feel free to extend modules (e.g., billing, staff management) or add validation and error handling as next steps.