
---

# 🎨 **Creative Prime Studio Management System**

A **Python-based Desktop Application** built using **Tkinter & CustomTkinter** to manage **employees, hiring & firing processes, and order/task assignments** for Creative Prime Studio.  
The system uses **MySQL** for secure data storage and supports structured management of studio operations.

---

## ✅ **Features**

### 👥 **Employee Management**

* Add, update, and manage employee records
* Store employee personal and professional details
* Hiring and firing system with database persistence

### 📦 **Order Management**

* Create and manage client orders
* Assign orders to employees
* Track order allocation and status

### 🗄️ **Database-Driven System**

* MySQL used for permanent data storage
* Secure database connection module
* Structured tables for employees and orders

### 🖥 **Modern CustomTkinter GUI**

* Built with **CustomTkinter** for a modern UI
* User-friendly forms and dialogs
* Message boxes for alerts and confirmations
* Clean and organized multi-window layout

### 📊 **Data Handling & Export**

* Data processing using **Pandas**
* Excel file support using **openpyxl**
* Image handling with **Pillow (PIL)**

---

## 🛠 **Technologies Used**

* **Python**
* **Tkinter & CustomTkinter (GUI)**
* **MySQL (Database)**
* **Pandas (Data Handling)**
* **Pillow (Image Processing)**
* **openpyxl (Excel Support)**

---

## 🚀 **How to Run the Creative Prime Studio Management System**

Follow these steps to properly set up and run the application.

---

## **1️⃣ Create the MySQL Database**

Open **MySQL Workbench** and run:

```sql
CREATE DATABASE creative_prime_studio;

---

## **1️⃣ Create the MySQL Database**

Open **MySQL Workbench

```sql
CREATE DATABASE academy_management;
```

---

## **2️⃣ Create Required Table**

After creating the database, run this SQL command to create the **admin** table:

```sql
CREATE TABLE admin (
    StudentId INT AUTO_INCREMENT PRIMARY KEY,
    Student_Name VARCHAR(100) NOT NULL,
    Father_Name VARCHAR(100) NOT NULL,
    CNIC VARCHAR(100) UNIQUE NOT NULL,
    Father_CNIC VARCHAR(100) UNIQUE NOT NULL,
    Gender VARCHAR(100) NOT NULL,
    DOB VARCHAR(100) NOT NULL,
    Phone VARCHAR(100) NOT NULL,
    Address VARCHAR(300) NOT NULL,
    Father_pro VARCHAR(100) NOT NULL,
    Course VARCHAR(100) NOT NULL,
    Admission_Date VARCHAR(100) NOT NULL,
    Course_Duration VARCHAR(100) NOT NULL,
    Passing_Date VARCHAR(100) NOT NULL,
    Fee_Status VARCHAR(100) NOT NULL
);
```

---

## **3️⃣ Connect Your MySQL Database to the App**

In your project, open your main.py

Update your credentials:

```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="academy_management"
)
```



---

## **4️⃣ Install Required Python Libraries**

Run these commands in terminal:

```bash
pip install customtkinter
pip install pillow
pip install fpdf
pip install mysql-connector-python
```

---

## **5️⃣ Run the Application**

After installing the requirements, run:

```bash
main.py

```
##  **Generated PDFs**

This system automatically generates:

| Document Type      | Format | Description                            |
| ------------------ | ------ | -------------------------------------- |
| Student Challan    | PDF    | Fee challan with institute details     |
| Student ID Card    | PDF    | Printable ID card (single or batch)    |
| Course Certificate | PDF    | Official course completion certificate |



## 🤝 **Contributions**

Contributions, issues, and feature requests are welcome!
Feel free to open an issue or submit a pull request.

---

## 📌 **Future Improvements**


* QR code on ID cards
* Attendance management module
* Export/Import student data (CSV/Excel)

---
## 📸 Project Screenshots

### 🏫 Home Tab
![Dashboard](images/home_tab.png)

### 👨‍🎓 Admission Form
![Students](images/admission_tab.png)

### 🪟 View Tab
![Login](images/view_tab.png)




