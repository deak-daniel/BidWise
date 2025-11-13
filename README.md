# BidWise – Smart Quotation App

BidWise is a simple quotation management system where **admins** can add products or services, and **users** can generate price offers by selecting items that fit their needs.

---

## 🚀 Features

- **Admin dashboard**
  - Add, edit, and delete products or services
  - Set product name, description, and price
- **User quotation system**
  - Browse available products
  - Select items to include in an offer
  - Automatically calculate total cost
  - Generate a formatted price quotation
- **SQLite database**
  - Two main tables: `User` and `Product`
- **REST API backend (FastAPI)**
  - Endpoints for user management and quotation data
- **Simple web UI (Streamlit or other frontend)**
  - User-friendly interface for admins and clients

---

## 🗂️ Database Structure

### **User Table**
Stores information about admin users who can manage product data.

| Column       | Type      | Description              |
|---------------|-----------|--------------------------|
| `id`          | INTEGER   | Primary key              |
| `username`    | TEXT      | Admin username           |
| `password`    | TEXT      | Hashed password          |
| `role`        | TEXT      | User role (e.g. admin)   |

---

### **Product Table**
Contains items that can appear in a quotation.

| Column       | Type      | Description                        |
|---------------|-----------|------------------------------------|
| `id`          | INTEGER   | Primary key                        |
| `name`        | TEXT      | Product or service name            |
| `description` | TEXT      | Short description                  |
| `price`       | REAL      | Unit price                         |

---

## ⚙️ Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** Streamlit (optional UI)
- **Database:** SQLite
- **Dependencies:** SQLAlchemy, Requests, Uvicorn

---

## 🧩 Example API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `POST` | `/users` | Create admin user |
| `GET` | `/products` | List all products |
| `POST` | `/products` | Add new product |
| `PUT` | `/products/{id}` | Update product |
| `DELETE` | `/products/{id}` | Delete product |
| `POST` | `/quote` | Generate quotation from selected products |

---

## 🧱 Example Quotation Logic

1. User selects multiple `product_id` values.
2. The API fetches product details and calculates:
total = sum(product.price for product in selected_products)

css
Copy code
3. The response returns a summary like:

```json
{
"selected_items": [
 {"name": "Website Design", "price": 500},
 {"name": "Hosting", "price": 100}
],
"total": 600
}