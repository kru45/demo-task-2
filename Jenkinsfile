pipeline {
    agent any
    
    environment {
        // This line securely links Jenkins to Python
        API_KEY = credentials('my-internal-api-key')
    }

    stages {
        stage('Security Check') {
            steps {
                echo 'Checking for API credentials...'
                // This will run the script using the token hidden in Jenkins
                sh 'python3 api_test.py'
            }
        }
    }
}
