from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login_form():
    return render_template('root/tamplates/login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Add your login logic here
    return 'Login Successful'  # or render another template

