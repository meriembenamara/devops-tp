from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, CI/CD!"

# Nouveau point de terminaison /status
@app.route('/status')
def status():
    return "API is up and running!"

if __name__ == "__main__":
    app.run()

