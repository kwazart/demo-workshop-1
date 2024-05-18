// Этот Jenkinsfile выполняет следующие действия:

// Проверяет код из Git репозитория.
// Устанавливает необходимую версию Python и Pip.
// Устанавливает зависимости через requirements.txt.
// Запускает тесты.
// Запускает приложение.

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/kwazart/demo-workshop-1'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Build') {
            steps {
                sh 'streamlit run main.py'
            }
        }
    }
}