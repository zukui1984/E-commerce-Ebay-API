# E-commerce eBay API Integration
A simple e-commerce REST API using Flask (Python), integrating with eBay's sandbox API to fetch product data & Stripe for payment processing. 

## Tech requirements
1. Python / Flask (Python framework)
2. eBay Developer Program
3. API - eBay (products) and Stripe (payment)
4. Heroku - Hosting (optional)

## Project structure
```markdown
ecommerce_project/
├── app.py
└── templates/
    └── index.html
├── requirements.txt
```

## Instructions
1. Create an account at eBay Developer Programs for API
<img src="https://github.com/user-attachments/assets/b912c99d-763a-47b8-90cd-0b2b0f136ac6" width="700" />

2. Install Flask, dotenv (.env), Stripe
```python
pip install Flask requests python-dotenv stripe
```
3. Create .env folder (environment variables - security)
```python
EBAY_APP_ID=ID_KEY
EBAY_AUTH_TOKEN=TOKEN_KEY
STRIPE_PUBLISHABLE_KEY=pk_test_KEY
STRIPE_SECRET_KEY=sk_test_KEY
```
4. Create eBay - Application Key & User Token (Auth'n'Auth)
    - Create project name: **ecommerce_2024**
    - **Application Key**: App ID (Client ID), Dev ID, Cert ID (Client Secret)
    - Create Sandbox to get User Token
<img src="https://github.com/user-attachments/assets/73b11c2e-df8a-4bc5-a4ef-451f379831e8" width="700" />

5. Add API Key eBay (App ID & User Token) & Stripe on .env
   
<img src="https://github.com/user-attachments/assets/17e6fef9-4d22-4956-bbd6-2173915df976" width="700" />
        
6. Create API Endpoints - [complete code](https://github.com/zukui1984/E-commerce-Flask/blob/master/app.py)
   
    -  **GET /products**: Fetches product data from eBay's sandbox API
    -  **POST /checkout**: Creates a Stripe checkout session for payment processing.
    
7. To run the application
```python
python app.py
```
<img src="https://github.com/user-attachments/assets/00cc23bd-7d2c-4c1e-a159-594568f8ba2e" width="700" />

8. To view product list - JSON
```
http://localhost:5000/products
```
<img src="https://github.com/user-attachments/assets/e15b02c3-27ef-4e25-bca4-9d14b034b940" width="700" />

