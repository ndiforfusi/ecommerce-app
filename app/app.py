from flask import Flask, render_template

app = Flask(__name__, static_folder="app/static", template_folder="app/templates")

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
