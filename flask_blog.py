from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = "c8ce2bbe5ef23bd8e4e1ec216760de18"
posts = [
    {
        "author": "ink kila",
        "title": "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "April 20, 2019"
    },
    {
        "author": "ink kila",
        "title": "Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "April 22, 2019"
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/register")
def register():
    

if __name__ == "__main__":
    app.run(debug=True)
