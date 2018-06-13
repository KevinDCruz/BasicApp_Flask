from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return "Default Method Used %s" % request.method


@app.route('/profile')
def prof_name():
    return "Enter name in url "


@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)


if __name__ == "__main__":
    app.run()
