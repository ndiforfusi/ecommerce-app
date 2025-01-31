from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder="static")

# Serve images from /static
@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

# Serve CSS from /static
@app.route('/static/<path:filename>')
def serve_static_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def product_list():
    return render_template('products.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
