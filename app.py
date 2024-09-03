from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

products = {
    "desinfetante": 3.50,
    "agua_sanitaria": 3.50,
    "alcool_perfumado": 12.00,
    "sabao_liquido": 12.00,
    "sabao_de_pedra": 5.50,
    "amaciante": 14.00,
    "solupan": 7.00,
    "limpa_pedra": 7.00,
    "limpa_aluminio": 5.00
}

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    total = 0
    quantities = {}
    
    for product, price in products.items():
        quantity = int(data.get(product, 0))
        quantities[product] = quantity
        total += quantity * price
    
    response = {
        "total": total,
        "quantities": quantities
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
