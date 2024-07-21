from flask import Flask, request, jsonify, render_template
import requests
import stripe
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# API keys from .env file
EBAY_APP_ID = os.getenv('EBAY_APP_ID')
EBAY_AUTH_TOKEN = os.getenv('EBAY_AUTH_TOKEN')
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')

# Configure Stripe
stripe.api_key = STRIPE_SECRET_KEY

# Sandbox URL for eBay API
EBAY_API_URL = 'https://svcs.sandbox.ebay.com/services/search/FindingService/v1'

# REST API - GET
@app.route('/products', methods=['GET'])
def get_products():
    headers = {
        'X-EBAY-API-IAF-TOKEN': EBAY_AUTH_TOKEN
    }
    params = {
        'OPERATION-NAME': 'findItemsByKeywords',
        'SERVICE-VERSION': '1.0.0',
        'SECURITY-APPNAME': EBAY_APP_ID,
        'RESPONSE-DATA-FORMAT': 'JSON',
        'keywords': 'smartphones',  # Example keyword, you can change it to any category
        'paginationInput.entriesPerPage': 10
    }
    response = requests.get(EBAY_API_URL, headers=headers, params=params)
    data = response.json()
    app.logger.info(data)  # Log the entire response for debugging
    try:
        items = data['findItemsByKeywordsResponse'][0]['searchResult'][0]['item']
        products = []
        for item in items:
            product = {
                'id': item['itemId'][0],
                'name': item['title'][0],
                'price': float(item['sellingStatus'][0]['currentPrice'][0]['__value__']),
                'image': item['galleryURL'][0],
                'url': item['viewItemURL'][0]
            }
            products.append(product)
        return jsonify(products)
    except KeyError as e:
        app.logger.error(f"KeyError: {e}")
        return jsonify({'error': 'Unexpected API response format', 'response': data}), 500

# REST API - POST
@app.route('/checkout', methods=['POST'])
def create_checkout_session():
    data = request.json
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': data['name'],
                        'images': [data['image_url']],
                    },
                    'unit_amount': int(data['unit_price'] * 100),
                },
                'quantity': data['quantity'],
            }],
            mode='payment',
            success_url='http://localhost:5000/success',
            cancel_url='http://localhost:5000/cancel',
        )
        return jsonify({'id': session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route('/')
def index():
    return render_template('index.html', stripe_publishable_key=STRIPE_PUBLISHABLE_KEY)

if __name__ == '__main__':
    app.run(debug=True)
