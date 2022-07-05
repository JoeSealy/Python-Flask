from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "a324537758596f5ae524d5fcdd8790a4"
posts = [
    {
        "author":"Joe Sealy",
        "title": "Blog Post 1",
        "content": "First Post content",
        "date_posted": "June 28, 2022"
    },
    {
        "author":"Toe Sealy",
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
    return render_template("about.html", title = "About")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("Register.html", title  = "Register", form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title  = "Login", form = form)

if __name__ == "__main__":
    app.run(debug=True)