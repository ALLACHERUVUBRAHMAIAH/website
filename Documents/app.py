from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Google app engine platform!"

@app.route("/about")
def about():
    return "This is a simple Python Web App."

if __name__ == "__main__":
    app.run(debug=True)
