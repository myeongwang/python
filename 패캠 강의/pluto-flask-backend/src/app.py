from flask import Flask

app = Flask(__name__)

#method: get
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/<username>")
def hell_user(username):
    return f"<h1>Hello, {username}!</h1>"

@app.route("/feed/<int:feed_id>")
def show_feed(feed_id):
    return f"<h1>FeedID : {feed_id}</h1>"


if __name__ == "__main__":
    app.run()
