from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
	return render_template('auth/sign-up.html')

@app.route('/user')
def user_dash():
	return render_template('auth/user-dash.html')

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    local_stores = [
        {'name': 'Store 1', 'description': 'A great store!', 'url': 'https://www.store1.com', 'image': 'https://www.example.com/store1.jpg'},
        {'name': 'Store 2', 'description': 'Another great store!', 'url': 'https://www.store2.com', 'image': 'https://www.example.com/store2.jpg'},
        {'name': 'Store 3', 'description': 'Yet another great store!', 'url': 'https://www.store3.com', 'image': 'https://www.example.com/store3.jpg'}
    ]
    recent_transactions = [
        {'store': 'Store 1', 'amount': 50.00, 'date': '2023-04-01'},
        {'store': 'Store 2', 'amount': 25.00, 'date': '2023-03-31'},
        {'store': 'Store 3', 'amount': 10.00, 'date': '2023-03-30'},
        {'store': 'Store 1', 'amount': 75.00, 'date': '2023-03-29'},
        {'store': 'Store 2', 'amount': 20.00, 'date': '2023-03-28'}
    ]
    credit_factors = [
        'Pay bills on time',
        'Keep credit utilization low',
        'Don\'t open too many new accounts',
        'Maintain a long credit history'
    ]
    tips = [
        'Use credit for everyday purchases to build credit',
        'Set up automatic payments to avoid missed payments',
        'Check your credit report regularly for errors'
    ]
    return render_template('dash/main-dash.html', local_stores=local_stores, recent_transactions=recent_transactions, credit_factors=credit_factors, tips=tips)



@app.route('/submit', methods=['POST'])
def submit():
    account_type = request.form['account-type']
    return f'Thank you for signing up as a {account_type}!'


if __name__ == '__main__':
    app.run(debug=True)