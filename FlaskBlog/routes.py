from flask import render_template, flash, redirect,  url_for
from FlaskBlog.forms import RegistrationForm, LoginForm
from FlaskBlog.models import User, Post
from FlaskBlog import app
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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))

    return render_template("register.html", title="Register", form=form)


@app.route("/login",  methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessfull. Please check username or password", "danger")
    return render_template("login.html", title="Login", form=form)
