# Dynamic Pricing API
This project implements a dynamic pricing system with class inheritance to handle different types of products and discounts. It supports dynamic price calculation, applying various types of discounts, and managing orders through a RESTful API.
________________________________________

## Features

•	Product management with unique pricing rules: 
o	Seasonal Product: Applies a discount based on the current season.
o	Bulk Product: Applies tiered discounts based on quantity purchased.
o	Premium Product: Adds a fixed percentage markup for premium features.

•	Discount management system with: 
o	Percentage Discounts
o	Fixed Amount Discounts
o	Tiered Discounts (based on quantity or order value).

•	Fully tested RESTful APIs for reliability.
________________________________________

## Setup Instructions

Prerequisites

Ensure the following are installed:
•	Python (>=3.8)
•	pip (Python package manager)
•	Virtualenv (optional but recommended)
•	SQLite (comes with Django by default)
________________________________________

1. Clone the Repository
git clone <repository_url>
cd dynamic_pricing

2. Create and Activate a Virtual Environment
Create a virtual environment to isolate dependencies:
python -m venv venv

Activate the environment:
•	Windows: 
•	venv\Scripts\activate

•	macOS/Linux: 
•	source venv/bin/activate

3. Install Dependencies
Install all required Python packages:
pip install -r requirements.txt

4. Apply Migrations
Set up the database and create necessary tables:
python manage.py makemigrations
python manage.py migrate

5. Create a Superuser
Create an admin user for the Django admin panel:
python manage.py createsuperuser
Follow the prompts to set a username, email, and password.

6. Run the Development Server
Start the Django development server:
python manage.py runserver 127.0.0.1:8080
Access the project in your browser at http://127.0.0.1:8080/.
________________________________________

## APIs

## 1. Product Price API

This API calculates product prices dynamically based on the product type.
•	URL: http://127.0.0.1:8080/api/product-price/
•	Method: POST

Input Body (JSON):

# a. SeasonalProduct:
{
    "type": "seasonal",
    "name": "Winter Coat",
    "base_price": 100.0,
    "quantity": 2
}

Expected Output:
{
    "final_price": 160.0
}

# b. BulkProduct:
{
    "type": "bulk",
    "name": "Box of Pens",
    "base_price": 10.0,
    "quantity": 25
}

Expected Output:
{
    "final_price": 225.0
}

# c. PremiumProduct:
{
    "type": "premium",
    "name": "Luxury Watch",
    "base_price": 500.0,
    "quantity": 1
}

Expected Output:
{
    "final_price": 575.0
}
________________________________________

## 2. Apply Discount API

This API applies different types of discounts to a given price.
•	URL: http://127.0.0.1:8080/api/apply-discount/
•	Method: POST

Input Body (JSON):

# a. PercentageDiscount:

{
    "price": 100.0,
    "discount_type": "percentage",
    "percentage": 0.10
}

Expected Output:
{
    "final_price": 90.0
}

# b. FixedAmountDiscount:
{
    "price": 500.0,
    "discount_type": "fixed",
    "fixed_amount": 50.0
}

Expected Output:
{
    "final_price": 450.0
}

# c. TieredDiscount:
{
    "price": 1200.0,
    "discount_type": "tiered",
    "tiers": {
        "500": 0.05,
        "1000": 0.10
    }
}

Expected Output:
{
    "final_price": 1080.0
}

________________________________________

## Running Tests

To ensure functionality, run the tests:
python manage.py test

Tests validate:
•	Correct price calculation for SeasonalProduct, BulkProduct, and PremiumProduct.
•	Proper discount application for percentage, fixed amount, and tiered discounts.
________________________________________

## Conclusion
This project demonstrates a system for calculating dynamic product prices and applying various discounts using class inheritance and RESTful APIs. It is fully tested and ready for deployment.
________________________________________

