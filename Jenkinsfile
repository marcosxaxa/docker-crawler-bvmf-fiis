pipeline {
    agent {
        docker {
            image 'python'
        }
    }
    
    stages {
        stage('Test'){
            steps{
                sh "ls -la"
                sleep 15
            }
        }
    }
}