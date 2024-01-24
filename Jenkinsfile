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
                        sh 'pip3 install -r requirements.txt'
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying...'
                    sh 'docker container run -d -p 3000:3000 shravani10k/hey-python-flask:0.0.1.RELEASE'
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
