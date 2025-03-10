from flask import Flask

# Créer l'application Flask
app = Flask(__name__)

# Définir un point de terminaison pour la page d'accueil
@app.route('/')
def hello():
    return "Hello, CI/CD!"

# Lancer l'application sur toutes les interfaces réseau et sur le port 5000
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
