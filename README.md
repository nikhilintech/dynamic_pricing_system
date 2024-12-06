
# Dynamic Pricing API

This project implements a dynamic pricing system with tiered discount pricing for products based on quantity and total order value. It includes APIs for calculating discounts and supports testing for proper functionality.

---

## Features
- APIs for calculating dynamic pricing with tiered discounts.
- Bulk discount based on quantity thresholds.
- Order value discount based on total order price.
- Fully tested endpoints for reliability.


## Setup Instructions

## Prerequisites

Ensure the following are installed:
- Python (>=3.8)
- pip (Python package manager)
- Virtualenv (optional but recommended)
- SQLite (comes with Django by default)

---

### 1. Clone the Repository
git clone <repository_url>
cd dynamic_pricing


### 2. Create and Activate a Virtual Environment
Create a virtual environment to isolate dependencies:
python -m venv venv


Activate the environment:
- Windows:
  venv\Scripts\activate

- macOS/Linux:
  source venv/bin/activate


### 3. Install Dependencies
Install all required Python packages:
pip install -r requirements.txt


### 4. Apply Migrations
Set up the database and create necessary tables:
python manage.py makemigrations
python manage.py migrate


### 5. Create a Superuser
Create an admin user for the Django admin panel:

python manage.py createsuperuser

Follow the prompts to set a username, email, and password.


### 6. Run the Development Server
Start the Django development server:

python manage.py runserver 127.0.0.1:8080

Access the project in your browser at http://127.0.0.1:8080/

---

## Adding Products

### Option 1: Through Admin Panel
1. Go to the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
2. Log in using the superuser credentials.
3. Add products under the Products section.

### Option 2: Through Django Shell
You can also add products programmatically:

python manage.py shell

Then execute:

from pricing.models import Product

# Add a product
Product.objects.create(name="T-shirt", base_price=10.0)


---

## Testing APIs

### 1. Bulk Discount API
URL: `http://127.0.0.1:8000/api/bulk-discount/`  
Method: POST  
Example Request:
```json
{
    "product_id": 1,
    "quantity": 25
}
```

Example Response:
```json
{
    "product": "T-shirt",
    "quantity": 25,
    "base_price": 250.0,
    "discount": "10%",
    "final_price": 225.0
}
```

### 2. Order Discount API
URL: `http://127.0.0.1:8000/api/order-discount/`  
Method: POST  
Example Request:
```json
{
    "items": [
        {
            "product_id": 1,
            "quantity": 10
        },
        {
            "product_id": 2,
            "quantity": 5
        }
    ]
}
```

Example Response:
```json
{
    "total_price": 600.0,
    "discount": "5%",
    "final_total": 570.0
}
```

---

## Running Tests
To ensure the functionality is correct:

python manage.py test
