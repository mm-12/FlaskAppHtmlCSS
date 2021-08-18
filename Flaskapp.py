from flask import Flask, render_template

app = Flask(__name__)
port = 5000

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)