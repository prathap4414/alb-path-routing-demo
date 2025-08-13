from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Flask!</h1>"

@app.route('/5000')
def flask5000():
    return "<h1>Hello from Flask at /5000!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
