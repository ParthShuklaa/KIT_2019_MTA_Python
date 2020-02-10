import flask

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/KIT')
def kit_Hello():
    return "<h1>Hello KIT.....</h1>"

if __name__ == "__main__":
    app.run()