pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from the version control system
                git 'https://github.com/codekeep18feb/pmess.git'
            }
        }
        
        stage('Build') {
            steps {
                // Build your Docker image
                script {
                    docker.build('shravani10k/hey-python-flask:0.0.1.RELEASE')
                }
            }
        }
        
        stage('Test') {
            steps {
                // Run your tests
                script {
                    docker.image('shravani10k/hey-python-flask:0.0.1.RELEASE').inside {
                        sh 'your test commands here'
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy your application
                script {
                    docker.image('shravani10k/hey-python-flask:0.0.1.RELEASE').inside {
                        sh 'your deployment commands here'
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
