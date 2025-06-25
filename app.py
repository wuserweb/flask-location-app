from flask import Flask, render_template, request

app = Flask(__name__)

VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print("Username:", username)
        print("Password:", password)

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return "<h2 style='color:green;'>Login successful!</h2>"
        else:
            return "<h2 style='color:red;'>Your password is invalid.</h2>"

    return render_template('indexe.html')

if __name__ == '__main__':
    app.run()