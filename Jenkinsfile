pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker run --rm \
                      -v "$PWD/app:/app" \
                      -w /app \
                      python:3.12-slim \
                      sh -c "pip install -r requirements-dev.txt && pytest --cov=app --cov-report=xml"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t octabyte-assignment:${BUILD_NUMBER} -f docker/Dockerfile .
                '''
            }
        }

       
        stage('SonarQube Analysis') {
            steps {
                withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                sh '''
                    docker run --rm \
                    --network sonar_default \
                    -v "$PWD:/usr/src" \
                    -w /usr/src \
                    -e SONAR_HOST_URL="http://octabyte-sonarqube:9000" \
                    -e SONAR_TOKEN="$SONAR_TOKEN" \
                    sonarsource/sonar-scanner-cli
                '''
                }
            }
        }
        

    }
}