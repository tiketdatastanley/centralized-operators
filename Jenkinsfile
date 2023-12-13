pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Run Python Command') {
            steps {
                script {
                    echo 'Running the Python command...'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! Send notifications or perform additional actions here.'
        }

        failure {
            echo 'Pipeline failed! Send notifications or perform additional actions here.'
        }
    }
}
