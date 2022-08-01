from flask import render_template, flash, redirect,  url_for, request
from FlaskBlog.forms import RegistrationForm, LoginForm
from FlaskBlog.models import User, Post
from FlaskBlog import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
posts = [
    {
        "author": "Joe Sealy",
        "title": "Blog Post 1",
        "content": "First Post content",
        "date_posted": "June 28, 2022"
    },
    {
        "author": "Toe Sealy",
        "title": "Blog Post 2",
        "content": "Second Post content",
        "date_posted": "June 29, 2022"
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode("utf-8")
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Account Created, Thank You", "success")
        return redirect(url_for("login"))

    return render_template("register.html", title="Register", form=form)


@app.route("/login",  methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get("next")
            return redirect (next_page) if next_page else redirect(url_for("home")) #ternary conditional
        else:
            flash("Login unsuccessfull. Please check username or password", "danger")
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/account")
@login_required
def account():
     return render_template("account.html", title="Account")
