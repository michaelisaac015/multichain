from common.database import Database
from common.blockchain import Blockchain
from models.user import User


from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)  # '__main__'
app.secret_key = "jose"


@app.route('/')
def home_template():
    return render_template('home.html')


@app.route('/login')
def login_template():
    return render_template('login.html')


@app.route('/register')
def register_template():
    return render_template('register.html')


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template("profile.html", email=session['email'])


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email, password)

    return render_template("profile.html", email=session['email'])


@app.route('/blocks/<string:user_id>')
@app.route('/blocks')
def user_blocks(user_id=None):
    if user_id is not None:
        user = User.get_by_id(user_id)
    else:
        user = User.get_by_email(session['email'])

    blocks = user.get_blocks()

    return render_template("user_blocks.html", email=user.email)


if __name__ == '__main__':
    app.run(port=4990, debug=True)
