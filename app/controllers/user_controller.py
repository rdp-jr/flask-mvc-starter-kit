from flask import render_template, redirect, url_for
from app.models.user import User
from app.forms.user.LoginForm import LoginForm
from app.forms.user.RegisterForm import RegisterForm
from flask_login import login_user, login_required, logout_user, current_user
from app import flask_bcrypt


def index():
    """ 
    index 
    """

    pass

def create():
    """ 
    create 
    """

    pass


def store():
    """ 
    store 
    """

    pass


def show(user_id):
    """ 
    show 

    @user_id: id of the user
     
    """

    return f"user {user_id}"

def edit(user_id):
    """ 
    edit 

    @user_id: id of the user
    """

    pass

def update(user_id):
    """ 
    update 

    @user_id: id of the user
    """

    pass


def delete(user_id):
    """ 
    delete 

    @user_id: id of the user

    """

    pass

@login_required
def dashboard():
    return render_template('user/dashboard.html')

@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))


def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))


    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if flask_bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('users.dashboard'))

    return render_template('user/login.html', form=form)

def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))



    form = RegisterForm()

    if form.validate_on_submit() and form.password.data == form.confirm_password.data:
        hashed_password = flask_bcrypt.generate_password_hash(form.password.data)

        # create separate service for this
        # new_user = User(username=form.username.data, password=hashed_password)
        # print(new_user)
        # db.session.add(new_user)
        # db.session.commit()
        new_user = User.create(username=form.username.data, password=hashed_password)
        

        return redirect(url_for('users.login'))
    return render_template('user/register.html', form=form)