# 🏛️ Government Payroll Management System  
**Course:** Database Systems (DBS)  
**Developer:** Aqsa Najeeb   
**Semester Project — UET, Taxila**

---

## 📘 Overview
The **Government Payroll Management System** is a role-based desktop application built using **Python (Tkinter)** and **Oracle Database**.  
It automates the payroll generation process for government employees, ensuring accuracy in salary calculation, tax deduction, and leave management.  

The system integrates **Stored Procedures, Views, and Triggers** from the database with an interactive **Graphical User Interface (GUI)** that provides different dashboards for HR, Accountant, Employee, and DBA roles.

---

## ⚙️ Tech Stack
| Component | Technology Used |
|------------|----------------|
| Frontend (GUI) | Python (Tkinter) |
| Backend | Oracle Database |
| Database Connectivity | cx_Oracle |
| Reporting | SQL Views, Tkinter Table View |
| Language | Python 3.x |
| Architecture | Role-based, modular, MVC-style design |

---

## 🧩 System Architecture

The application consists of **four dashboards** that interact with the same Oracle Database using stored logic for efficiency and consistency.

### 🧑‍💼 1. HR Dashboard
**Purpose:** Manage employee records and administrative operations.  
**Key Features:**
- Add, edit, and remove employees.  
- Manage grades, departments, and attendance.  
- Approve or reject leave requests.  
- View department-wise employee details and attendance summaries.  

**Database Tables Used:**
`EMP_T`, `DEPT_T`, `GRADE_T`, `LEAVE_T`, `ATTENDANCE_T`

---

### 🧮 2. Accountant Dashboard
**Purpose:** Generate and manage payroll records.  
**Key Features:**
- Prompt for **Employee ID** and **Payment Status**.  
- Fetch salary data and compute:
  - Gross Salary  
  - Tax Deduction  
  - Leave Deduction  
  - Net Salary  
- Insert record into `PAYROLL_T` table.  
- Display the final payslip or summary in a popup view.  

**Backend Logic:**
- Stored Procedures:
  - `CALCULATE_GROSS_SALARY`
  - `CALCULATE_TAX`
  - `CALCULATE_NET_SALARY`
- Manual Python-side deduction for unpaid leaves.  

**Database Tables Used:**
`PAYROLL_T`, `TAX_T`, `LEAVE_T`, `GRADE_T`

---

### 👨‍💻 3. Employee Dashboard
**Purpose:** Allow employees to view and manage their own information.  
**Key Features:**
- View personal profile and attendance summary.  
- Check payroll history and generated payslips.  
- Apply for leaves and track approval status.  
- Update limited personal details.  

**Database Views Used:**
- `EMP_PAYROLL_VIEW`
- `EMP_LEAVE_STATUS_VIEW`

**Database Tables Used:**
`EMP_T`, `PAYROLL_T`, `LEAVE_T`

---

### 🧠 4. DBA Dashboard
**Purpose:** Handle database maintenance and system administration.  
**Key Features:**
- Create and manage Views, Procedures, and Triggers.  
- Review and monitor database tables and relationships.  
- Handle user access privileges and data integrity checks.  

**Database Operations:**
- Schema maintenance, triggers, and constraint monitoring.

---

## 🔐 Login and Role-Based Access
- User authentication through Oracle Database.  
- Redirects users to the correct dashboard based on their **role (HR / Accountant / Employee / DBA)**.  
- Stores Employee ID session-wise for subsequent operations.  

---

## 📊 Reports and Data Visualization
- **Leave Reports:** Display all employee leaves with their approval status.  
- **Payroll Reports:** Show computed payrolls with tax and deductions.  
- **Employee Summary:** Combine data from multiple tables through SQL Views for readable insights.

---

## 🧾 Database Schema (Core Tables)
| Table Name | Purpose |
|-------------|----------|
| `EMP_T` | Stores employee details |
| `GRADE_T` | Defines grade-based pay scales |
| `ATTENDANCE_T` | Tracks daily attendance records |
| `LEAVE_T` | Records leave applications and statuses |
| `TAX_T` | Holds tax rates and related data |
| `PAYROLL_T` | Stores finalized payroll entries |
| `DEDUCTIONS_T` | Stores all deductions (tax, leave, etc.) applied to finalized payroll entries |

---

## 🧠 Stored Procedures
| Procedure Name | Description |
|----------------|-------------|
| `CALCULATE_GROSS_SALARY` | Calculates total pay including allowances |
| `CALCULATE_TAX` | Applies tax deductions based on grade and salary |
| `CALCULATE_NET_SALARY` | Computes final take-home salary |
| `CALCULATE_LEAVE_DEDUCTION` *(optional)* | Deducts unpaid leaves from total salary |

---

## 💡 Features Summary
✅ Clean, interactive GUI with four dashboards.  
✅ Strong Oracle database integration.  
✅ Uses stored procedures and views for consistent logic.  
✅ Leave management linked directly to payroll deduction.  
✅ Role-based access and authentication.  
✅ Pop-up based reports and form-based payroll entry.  

---

## 🚧 Challenges Faced
| Challenge | Description | Solution |
|------------|--------------|----------|
| **Database Column Mismatches** | Stored procedures referenced outdated columns like `AMOUNTPAID`. | Updated all references to match the latest table schema. |
| **Manual Leave Deduction Logic** | Initially done through SQL, caused issues. | Shifted to manual calculation in Python for accuracy. |
| **Passing DB Connection in Functions** | Created repetitive code. | Shifted to handle Oracle connection inside each function. |
| **UI Responsiveness** | Pop-ups overlapped or broke layout. | Used Tkinter `Frames`, `Toplevel()`, and padding for neat display. |
| **Salary Month/Year Redundancy** | Initially fetched from `TAX_T`. | Removed fields entirely for simplicity and flexibility. |

---

## 🧪 How to Run the Project

### 🧰 Prerequisites
- Python 3.x installed  
- Oracle Database (11g or higher)  
- Oracle Client configured  
- `cx_Oracle` Python library installed  

### 📦 Installation
```bash
pip install cx_Oracle
pip install tinkter
````

### ▶️ Run the Application

```bash
python Login_Screen.py
```

### ⚠️ Notes

* Update your Oracle **username, password, and DSN** in the connection configuration file before running.
* Ensure all database tables and stored procedures are created before launching the GUI.

---

## 🧭 Directory Structure

```
Government_Payroll_System/
│
├── Login_Screen.py             # Main code functionality
├── oracle_connect.py           # Oracle DB connection setup
├── Database ER diagram         # ERD of project
├── Python Code.txt             # Complete Python code
├── SQL Queries.txt             # Database quesries
└── README.md                   # Project documentation
```

---

## 🤝 Connect With Me

If you’d like to collaborate, discuss ideas, or share feedback, feel free to reach out:

* 📧 GitHub: [Aqsa Najeeb](https://github.com/AqsaNajeeb)
* 💼 LinkedIn: [Aqsa Najeeb](https://www.linkedin.com/in/aqsa-najeeb/)

---

## 📜 License

This project was developed for academic purposes under the Database Systems course.
Unauthorized commercial use or redistribution is not permitted without prior permission.

---
