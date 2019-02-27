from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/_secret/')
def secret():
    return 'You found the secret shop!'


if __name__ == "__main__":
    app.run(debug = True)
