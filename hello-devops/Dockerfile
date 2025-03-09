# Utiliser une image Python officielle
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet
COPY . /app

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port utilisé par Flask
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "app.py"]
