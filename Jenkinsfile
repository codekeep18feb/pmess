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
                script {
                    echo 'Stopping running Docker containers...'
                    sh 'if [ "$(docker ps -q)" ]; then docker stop $(docker ps -q); fi'
                    echo 'Building Docker image...'
                    sh 'docker build -t shravani10k/hey-python-flask:0.0.1.RELEASE .'
                }
            }
        }


        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    sh 'if [ -z "$(docker ps -q -f name=hey-python-flask)" ]; then docker container start hey-python-flask; fi'
                    sh 'docker exec -i hey-python-flask sh -c "pip3 install -r requirements.txt && pytest -s"'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying...'
                    sh 'docker container run -d -p 3001:3001 shravani10k/hey-python-flask:0.0.1.RELEASE'
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
v
