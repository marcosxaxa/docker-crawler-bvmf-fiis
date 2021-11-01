pipeline {
    agent {
        docker {
            image 'python:3.6-slim'
        }
    }
    stages {
        stage('Test'){
            steps{
                sh "python -V"
                sleep 15
            }
        }
    }
}