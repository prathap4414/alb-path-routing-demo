from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Flask App</h1><p>This is served from Flask (path '/5000').</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
