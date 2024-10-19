from sqlalchemy import func
from database import db
from models.employee import Employee
from models.product import Product
from models.order import Order
from models.production import Production
from models.customer import Customer

def analyze_employee_performance():
    results = (
        db.session.query(
            Employee.name,
            func.sum(Production.quantity_produced).label("total_quantity")
        )
        .join(Production, Employee.id == Production.employee_id)
        .group_by(Employee.name)
        .all()
    )
    return results

def identify_top_selling_products():
    results = (
        db.session.query(
            Product.name,
            func.sum(Order.quantity).label("total_sold")
        )
        .join(Order, Product.id == Order.product_id)
        .group_by(Product.name)
        .order_by(func.sum(Order.quantity).desc())
        .all()
    )
    return results

def determine_customer_lifetime_value():
    results = (
        db.session.query(
            Customer.name,
            func.sum(Order.total_price).label("total_value")
        )
        .join(Order, Customer.id == Order.customer_id)
        .group_by(Customer.name)
        .having(func.sum(Order.total_price) > 100) 
        .all()
    )
    return results

def evaluate_production_efficiency(date):
    results = (
        db.session.query(
            Product.name,
            func.sum(Production.quantity_produced).label("total_produced")
        )
        .join(Production, Product.id == Production.product_id)
        .filter(Production.date_produced == date)
        .group_by(Product.name)
        .all()
    )
    return results
