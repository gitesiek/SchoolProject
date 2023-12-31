from flask import Flask, render_template
from flask_login import LoginManager

from flask_wtf import CSRFProtect

from Users.models import db, User
from Users.users import users_bp

from Dashboard.dashboard import dashboard_bp


app = Flask(__name__, template_folder='templates')
app.register_blueprint(users_bp)
app.register_blueprint(dashboard_bp)

csrf = CSRFProtect(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SECRET_KEY'] = 'your-secret-key'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, threaded=False)
