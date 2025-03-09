pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "yourusername/hello-devops"  // Remplace 'yourusername' par ton nom Docker Hub
    }
    stages {
        stage('Build Docker') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }
        stage('Push Docker') {
            steps {
                sh 'echo "docker push ${DOCKER_IMAGE}"'  // Simulation du push
            }
        }
    }
}
