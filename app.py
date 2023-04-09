from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
	return render_template('auth/sign-up.html')

@app.route('/submit', methods=['POST'])
def submit():
    account_type = request.form['account-type']
    return f'Thank you for signing up as a {account_type}!'


if __name__ == '__main__':
    app.run(debug=True)



