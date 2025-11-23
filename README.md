#  Hospital Management System

## Project Title
**Hospital Management System – Terminal Based (Python + MySQL)**

## Overview of the Project
This is a simple, menu-driven **Hospital Management System**  project , developed using **Python** and **MySQL**.  
It allows hospital staff to manage **patients**, **beds**, and **drugs** using a terminal interface.
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

## Technologies / Tools Used
- **Python 3.13 or above** get it from https://www.python.org/downloads/
- **MySQL Server** get it from https://dev.mysql.com/downloads/mysql/
- **MySQL Workbench** same for this get from https://dev.mysql.com/downloads/mysql/
- **mysql-connector-python** library
- Command Prompt 

## Steps to Install & Run the Project
### 1. Clone the Repository

git clone https://github.com/rishavraj-dev/HospitalManagementSystem
cd HospitalManagementSystem

### 2. Install Required Python Package
Install the MySQL connector library (make sure Python 3.13 or later  is installed).
```
pip install mysql-connector-python
```

### 3. Create MySQL Database
Inside the  MySQL Workbench:
```sql
CREATE DATABASE hospital_db;
USE hospital_db;
```

### 4. Create Required Tables
Following SQL Commands will get the required table structure for the project 
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

### 7. Final last steps to start 
- Start program with `python main.py`
- Choose a module (Patients / Beds / Drugs)
- Add sample entries
- Try updating records
- Export CSV files from each module
- Verify CSV files appear in the project folder

### 👤 Author
Rishav Raj  
B.Tech CSE (Core) — VIT Bhopal University
