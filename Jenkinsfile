pipeline {
    agent { label "jenkins_slave1_pynode" }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/codekeep18feb/pmess.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t shravani10k/hey-python-flask:0.0.1.RELEASE .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pip3 install -r requirements.txt'
                sh 'pytest -s'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Stopping and removing existing container...'
                sh 'docker container stop hey-python-flask || true'
                sh 'docker container rm hey-python-flask || true'

                echo 'Deploying...'
                sh 'docker container run -d -p 3000:3000 --name hey-python-flask shravani10k/hey-python-flask:0.0.1.RELEASE'
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
