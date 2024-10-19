from flask import request, jsonify
from services.taskTwoService import (
    analyze_employee_performance,
    identify_top_selling_products,
    determine_customer_lifetime_value,
    evaluate_production_efficiency
)

def get_employee_performance():
    results = analyze_employee_performance()
    return jsonify(results), 200

def get_top_selling_products():
    results = identify_top_selling_products()
    return jsonify(results), 200

def get_customer_lifetime_value():
    results = determine_customer_lifetime_value()
    return jsonify(results), 200

def get_production_efficiency():
    date = request.args.get('date') 
    results = evaluate_production_efficiency(date)
    return jsonify(results), 200
