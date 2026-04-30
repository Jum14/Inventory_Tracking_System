# Inventory Tracking System

A web-based Inventory Tracking System developed using **Python Django** to help businesses, schools, offices, and organizations efficiently manage products, stock levels, and inventory transactions through a centralized digital platform.

---

# Table of Contents

1. Project Overview  
2. Objectives  
3. Key Features  
4. Technologies Used  
5. System Architecture  
6. Database Structure  
7. Installation Guide  
8. How to Run the System  
9. Default Admin Access  
10. System Modules  
11. Workflow Process  
12. Screenshots / Interface Guide  
13. Security Features  
14. Future Improvements  
15. Developers  
16. License  

---

# 1. Project Overview

Traditional inventory systems often rely on paper records or spreadsheets, which may cause:

- Incorrect stock counts  
- Lost records  
- Duplicate entries  
- Delayed updates  
- Human errors  

This project solves those issues by providing a **real-time web-based inventory management system** where authorized users can manage products, monitor stock levels, and track all inventory movements.

---

# 2. Objectives

The system was built to:

- Centralize all inventory data in one platform  
- Track stock levels in real time  
- Reduce manual errors  
- Improve efficiency of stock handling  
- Maintain transaction history logs  
- Help monitor low-stock products  
- Provide secure access using authentication  

---

# 3. Key Features

## User Authentication

- Secure login system  
- Session-based access  
- Logout functionality  
- Restricted pages for unauthorized users  

## Dashboard Analytics

- Total Products  
- Total Categories  
- Low Stock Items  
- Inventory Charts  
- Category Stock Overview  

## Product Management (CRUD)

Users can:

- Add products  
- Edit products  
- Delete products  
- View products  
- Search products  

## Category Management

- Add categories  
- Edit categories  
- Delete categories  

## Supplier Management

- Add suppliers  
- Update supplier information  
- Remove suppliers  

## Stock Transactions

### Stock In

Increase item quantity when new stocks arrive.

### Stock Out

Reduce item quantity when products are used, sold, or removed.

## Transaction Logs

Every stock movement is recorded with:

- Product name  
- Quantity  
- Type (IN / OUT)  
- Date and Time  
- User who handled it  
- Remarks  

## Low Stock Alert

Products below minimum stock level are marked automatically.

---

# 4. Technologies Used

| Technology | Purpose |
|--------|---------|
| Python | Core Programming Language |
| Django | Web Framework |
| SQLite | Database |
| HTML5 | Frontend Structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive UI |
| JavaScript | Interactive Components |
| Chart.js | Dashboard Charts |

---

# 5. System Architecture

The project follows Django's **MVT Pattern**:

## Model

Handles database structure.

## View

Handles business logic and processing.

## Template

Handles user interface.

---

# 6. Database Structure

Main tables used:

## Users

Stores login credentials and permissions.

## Categories

Stores product categories.

## Products

Stores:

- Product Name  
- SKU  
- Description  
- Quantity  
- Price  
- Minimum Stock Level  
- Category  

## Suppliers

Stores supplier information.

## Transactions

Stores complete stock movement history.

---

# 7. Installation Guide

## Requirements

Install:

- Python 3.x  
- pip  
- Virtual Environment (recommended)

## Clone / Open Project Folder

bash
cd inventory_project

📦 Inventory Tracking System

📖 Project Overview

The Inventory Tracking System is a robust, web-based application built to streamline inventory management, monitor stock movements, and manage supplier relationships. Developed as a comprehensive final IT project, this system provides businesses with an intuitive dashboard and automated tools to ensure optimal stock levels and efficient operations.

🎯 Objectives

To provide a centralized platform for tracking products, categories, and suppliers.

To automate low-stock detection and prevent inventory shortages.

To deliver actionable business insights through an interactive analytics dashboard.

To demonstrate practical, full-stack web development skills using the Django framework.

✨ Features

📊 Interactive Dashboard

Key Metrics: Real-time summary of total users, products, suppliers, and categories.

Data Visualization: Dynamic charts rendering stock distribution per category and stock vs. minimum level comparisons (powered by Django ORM aggregation and JSON).

📦 Product Management

Full CRUD (Create, Read, Update, Delete) operations for inventory items.

Comprehensive product profiles including: Name, SKU, Category, Description, Price, Stock Level, and Supplier.

Automated Low Stock Detection: The system automatically flags products when their current stock falls below or equals the defined minimum stock level.

🗂️ Category Management

Organize products into logical groupings for easier navigation and reporting.

UI Customization support allowing specific icons and colors for different categories.

🏢 Supplier Management

Maintain detailed records of all suppliers and vendors.

Link suppliers directly to products for seamless reordering.

🔄 Inventory Transactions

Track all incoming and outgoing stock movements to maintain an accurate audit trail of inventory changes.

🔐 Authentication & Security

Secure, login-required access for all system features.

Role-based access control distinguishing between Admin (full access) and Staff (restricted operational access) roles.

🛠️ Tech Stack

Backend: Python, Django

Frontend: HTML5, CSS3, Bootstrap

Database: SQLite (Default Django DB, easily scalable to PostgreSQL/MySQL)

Data Visualization: Chart.js (or similar frontend charting library consuming Django JSON endpoints)

🏗️ System Architecture

The project follows Django's MVT (Model-View-Template) architecture and is divided into modular, highly cohesive apps:

inventory_project/
│
├── core/                   # Main project settings and configurations
├── products/               # App: Product & Category models, views, and logic
├── suppliers/              # App: Supplier management and details
├── transactions/           # App: Stock movement tracking and history
├── templates/              # Global HTML templates (Bootstrap integrated)
├── static/                 # CSS, JavaScript, and Image assets
└── manage.py               # Django execution script


🚀 Installation & Setup

Follow these instructions to get a local copy up and running.

Prerequisites

Python 3.8 or higher installed on your machine.

Git installed.

Step-by-step Setup

Clone the repository:

git clone [https://github.com/yourusername/inventory-tracking-system.git](https://github.com/yourusername/inventory-tracking-system.git)
cd inventory-tracking-system


Create and activate a virtual environment:

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


Install the required dependencies:

pip install -r requirements.txt


Apply database migrations:

python manage.py makemigrations
python manage.py migrate


Create a superuser (Admin account):

python manage.py createsuperuser
# Follow the prompts to set up your email, username, and password


Run the development server:

python manage.py runserver


Access the application:
Open your web browser and navigate to http://127.0.0.1:8000/.

💡 Usage Instructions

Login: Access the system using the Admin credentials created during setup, or use the following pre-configured demo accounts:

Username: Manager — Has full access to all CRUD operations.

Username: staff_johndoe — Has limited access on the system and only has the power to change the quantity of products.

Password (for both accounts): dummytest1

Setup Data: Navigate to Categories and Suppliers to populate your initial data.

Add Products: Go to the Products module to add new inventory items, linking them to the categories and suppliers you just created. Ensure you set a sensible "Minimum Stock Level" to activate the low-stock alerts.

Track Transactions: Use the Transactions module to log whenever stock is added or removed.

Monitor: Regularly check the Dashboard to view stock visualizations and monitor low-stock warnings.

🔮 Future Improvements

While the current system fulfills its core objectives, future iterations could include:

[ ] Export Functionality: Allow users to export reports and stock levels to CSV or PDF formats.

[ ] Email Notifications: Automated email alerts to admins when a product hits its minimum stock threshold.

[ ] RESTful API: Implementation of Django REST Framework (DRF) to allow mobile app integration.

[ ] Multi-Branch Support: Ability to track inventory across different warehouse locations.
