from flask import Flask

app = Flask(__name__)

@app.route("/")

def first_flask():
    return "Hello This is my first flask program"


@app.route("/test")

def testing():
    return "Testing page"


app.run(debug=True)