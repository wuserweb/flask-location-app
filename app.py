from flask import Flask, render_template, request, redirect, url_for

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
            return redirect(url_for('dashboard'))
        else:
            return render_template('indexe.html', error="Invalid credentials")

    return render_template('indexe.html')

@app.route('/dashbord')
def dashbord():
    return render_template('dashbord.html')

if __name__ == '__main__':
    app.run()
