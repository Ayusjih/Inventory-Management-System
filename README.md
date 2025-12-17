# Inventory Management System 

A robust, database-driven Python application designed to manage inventory, track product stock, and generate actionable reports. This system simulates real-world enterprise requirements using **Python** and **MySQL**.

## 📋 Features

* **Database Integration:** Automatically connects to MySQL and creates the required database/tables if they don't exist.
* **CRUD Operations:**
    * **Add Product:** with validation for unique IDs and positive integers.
    * **Update Product:** Modify price or quantity for existing items.
    * **Delete Product:** Remove obsolete items from the database.
* **View Inventory:** Displays a formatted, easy-to-read table of all products.
* **Smart Reports:** Generates alerts for low-stock items (default threshold < 5).
* **Bulk Update (Advanced):** Apply percentage price adjustments (e.g., +10% inflation) or set fixed quantities for specific categories.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Database:** MySQL Server
* **Libraries:**
    * `mysql-connector-python` (Database connectivity)
    * `tabulate` (For formatting tables in the console)

## ⚙️ Prerequisites

Before running the application, ensure you have the following installed:

1.  **Python** (Version 3.6 or higher)
2.  **MySQL Server** (Running locally or remotely)

## 🚀 Installation & Setup

### 1. Install Python Dependencies
Open your terminal or command prompt and install the required libraries:


<img width="890" height="645" alt="Screenshot 2025-12-17 120349" src="https://github.com/user-attachments/assets/3c2ec1f6-387d-4e13-8968-ba1e312fc01e" />
<img width="1020" height="562" alt="Screenshot 2025-12-17 120401" src="https://github.com/user-attachments/assets/73e8a9fb-c252-457d-b9f4-f6519de23fdc" />
<img width="866" height="596" alt="Screenshot 2025-12-17 120413" src="https://github.com/user-attachments/assets/c86b0fb4-d982-446e-9eed-b214014c8646" />
<img width="812" height="597" alt="Screenshot 2025-12-17 120428" src="https://github.com/user-attachments/assets/d54cd912-6346-41be-b2b4-1cf153aba92a" />
<img width="574" height="421" alt="Screenshot 2025-12-17 120433" src="https://github.com/user-attachments/assets/97f55987-97d5-442d-ba36-1ec23a85ac37" />
<img width="1061" height="788" alt="Screenshot 2025-12-17 130615" src="https://github.com/user-attachments/assets/b7b2235f-1aed-4917-95f2-ac719e431d86" />











```bash
pip install mysql-connector-python tabulate
