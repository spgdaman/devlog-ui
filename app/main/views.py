from flask import render_template, redirect, url_for, flash
from . import main
from .forms import SignupForm, LoginForm
from flask_login import login_required, login_user
from ..models import User

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/signup', methods=["GET","POST"])
def sign_up():
    form = SignupForm()

    if form.validate_on_submit():
        flash("Your Sign Up was Successful!")
        return redirect(url_for('main.login'))
    return render_template('signup.html', form=form)

@main.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # if form.username.data == User.username:
        #     user_id = User.user_id
        #     login_user(user_id)
        #     flash("You Log In was Successful!")
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form)

@main.route('/profile/user')
def profile():
    return render_template('profile.html')

@main.route('/posts')
def display_all_posts():
    return render_template('allposts.html')

@main.route('/post/post_id')
def post():
    return render_template('post.html')

@main.route('/profile/user/edit')
def edit_profile():
    return render_template('editprofile.html')