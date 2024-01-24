pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/codekeep18feb/pmess.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'Building Docker image...'
                    sh 'docker build -t shravani10k/hey-python-flask:0.0.1.RELEASE .'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    docker.image('shravani10k/hey-python-flask:0.0.1.RELEASE').inside {
                        sh 'pip install -r requirements.txt'
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying...'
                    docker.image('shravani10k/hey-python-flask:0.0.1.RELEASE').inside {
                        // Add deployment steps if needed
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
