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
CREATE TABLE employees (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Skill VARCHAR(100),
    Phone VARCHAR(50),
    Address VARCHAR(255),
    Hire_date VARCHAR(50)
);
CREATE TABLE orders (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    order_Name VARCHAR(100),
    client_Name VARCHAR(100),
    order_des VARCHAR(255),
    price INT,
    assign_id INT
);

