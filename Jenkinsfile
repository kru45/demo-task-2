pipeline {
    agent any
    
    environment {
        // 'my-internal-api-key' is the ID you gave it in the Jenkins UI
        // API_KEY is the name Python will see
        API_KEY = credentials('my-internal-api-key')
    }

    stages {
        stage('Security Check') {
            steps {
                echo 'Checking for API credentials...'
                // Run the script. Jenkins will handle the secret injection.
                sh 'python3 api_test.py'
            }
        }
    }
}
