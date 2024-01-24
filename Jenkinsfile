pipeline {
    agent {label "jenkins_slave1_pynode"}


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
                    sh 'python3 -m pytest -s'
                  
            
            }
        }

        stage('Deploy') {
            steps {
              
                    echo 'Deploying...'
                    sh 'docker container run -d -p 3000:3000 shravani10k/hey-python-flask:0.0.1.RELEASE'
                
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
