from flask import Flask  # pip install Flask

# Pass in name to determine root path, then Flask can find other files easier
app = Flask(__name__)


# Route - mapping (connecting) a URL to Python function (Decorator)
@app.route('/')
def index():
    return "Method Used %s" % request.method


"""
@app.route('/fish')
def fish():
    return '<h1>Hey Fishie</h1>'


@app.route('/profile/<username>')
def profile(username):
    return "Hey There %s" % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post ID is %s" % post_id

"""
# Runs app only when we run this script directly, not if we import this somewhere else
if __name__ == "__main__":
    app.run(debug=True)

# http://127.0.0.1:5000/
