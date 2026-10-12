pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Menarik kode dari GitHub...'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t hartitawirastri/praktikum-cloudcomputing-1:latest .'
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USER')]) {
                    bat 'echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USER% --password-stdin'
                    bat 'docker push hartitawirastri/praktikum-cloudcomputing-1:latest'
                }
            }
        }
    }
}
