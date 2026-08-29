pipeline {
    agent any

    stages {

        stage('Test') {
            steps {
                sh '''
                    docker run --rm \
                      --volumes-from jenkins \
                      -w "$WORKSPACE/app" \
                      python:3.12-slim \
                      sh -c "pip install -r requirements-dev.txt && pytest --cov=app --cov-report=xml"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                      -t octabyte-assignment:${BUILD_NUMBER} \
                      -f docker/Dockerfile .
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                sh '''
                    docker run --rm \
                      --volumes-from jenkins \
                      --network sonar_default \
                      -w "$WORKSPACE" \
                      -e SONAR_HOST_URL="http://octabyte-sonarqube:9000" \
                      -e SONAR_TOKEN="$SONAR_TOKEN" \
                      sonarsource/sonar-scanner-cli
                '''
            }
        }
    }
}