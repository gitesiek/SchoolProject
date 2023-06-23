from flask import Blueprint, render_template, redirect, flash
from flask_login import current_user, login_user, login_required, logout_user

from .models import db, User
from .forms import RegistrationForm, LoginForm

users_bp = Blueprint('users', __name__)


@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/dashboard')

    form = RegistrationForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Username already exists in database.', 'error')
        else:
            new_user = User(username=form.username.data,
                            password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')

    return render_template('Users/register.html', form=form)


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/dashboard')

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            return redirect('/dashboard')
        else:
            flash('Invalid username or password', 'error')

    return render_template('Users/login.html', form=form)


@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
