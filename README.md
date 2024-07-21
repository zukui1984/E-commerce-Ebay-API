# E-commerce eBay API

## Tech requirements
1. Python / Flask (Python framework)
2. eBay Developer Program
3. API - eBay (products) and Stripe (payment)

## File structure
```bash
ecommerce-flask/
├── app.py
├── .env
├── templates/
│   └── index.html
```

## Instructions
1. Install Flask, dotenv (.env), Stripe
```python
pip install Flask requests python-dotenv stripe
```
2. Create .env
3. Create eBay - Application Key & User Token (Auth'n'Auth)
    - Create project name: **ecommerce_2024**
    - **Application Key**: App ID (Client ID), Dev ID, Cert ID (Client Secret)
    - Create Sandbox to get User Token
<img src="https://github.com/user-attachments/assets/73b11c2e-df8a-4bc5-a4ef-451f379831e8" width="700" />

4. Add API Key eBay (App ID & User Token) & Stripe on .env
   
<img src="https://github.com/user-attachments/assets/17e6fef9-4d22-4956-bbd6-2173915df976" width="700" />

5. Create API Endpoints - [complete code](https://github.com/zukui1984/E-commerce-Flask/blob/master/app.py)
   
    -  GET /products: Fetches product data from eBay's sandbox API
    -  POST /checkout: Creates a Stripe checkout session for payment processing.
    
6. To run the application
```python
python app.py
```
<img src="https://github.com/user-attachments/assets/00cc23bd-7d2c-4c1e-a159-594568f8ba2e" width="700" />

7. To view product list - JSON
```
http://localhost:5000/products
```
<img src="https://github.com/user-attachments/assets/e15b02c3-27ef-4e25-bca4-9d14b034b940" width="700" />






