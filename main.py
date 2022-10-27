from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! version 2.0</p>"

if __name__ == '__main__':
   app.run(debug=True)
