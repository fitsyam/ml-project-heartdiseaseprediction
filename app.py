from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/input")
def input():
    return render_template("input.html")

@app.route("/check_yourself")
def check_yourself():
    return redirect(url_for('input'))

if __name__ == '__main__':
    app.run(debug=True)
