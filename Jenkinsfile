pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "meriembenamara/hello-devops"
    }
    stages {
        stage('Build Docker') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }
        stage('Push Docker') {
            steps {
                sh 'echo "docker push ${DOCKER_IMAGE}"'  
            }
        }
    }
}
