from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder="static")

# Updated IT Products Catalogue
products = [
    {"id": 1, "name": "HP ProBook 15.6\" Laptop", "price": "$650", "image": "laptop_01.webp"},
    {"id": 2, "name": "Acer Aspire 15.6\" Laptop", "price": "$550", "image": "laptop_02.webp"},
    {"id": 3, "name": "HP EliteBook 14\" Laptop", "price": "$850", "image": "laptop_03.webp"},
    {"id": 4, "name": "HP Pavilion 24\" Monitor", "price": "$450", "image": "monitor_01.webp"},
    {"id": 5, "name": "HP All-in-One 27\"", "price": "$1100", "image": "monitor_02.jpg"},
    {"id": 6, "name": "Dell Dual Core PC Bundle", "price": "$300", "image": "sale.jpg"},
    {"id": 7, "name": "HP EliteDesk Dual Monitor Setup", "price": "$700", "image": "system_unit_01.jpg"},
    {"id": 8, "name": "Lenovo ThinkCentre Gaming PC", "price": "$900", "image": "system_unit_02.webp"},
    {"id": 9, "name": "Dell OptiPlex Business Desktop", "price": "$500", "image": "system_unit_03.webp"},
    {"id": 10, "name": "HP Workstation with LCD", "price": "$650", "image": "system_unit_04.webp"},
]

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/products')
def product_list():
    return render_template('products.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return "Product not found", 404

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
