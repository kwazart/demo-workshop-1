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
                'pip install -r ./requirements.txt'
                // sh 'pip install -r ./requirements.txt'
            }
        }

        stage('Saving dependencies') {
            steps {
                'pip freeze > ./requirements.txt'
                // sh 'pip freeze > ./requirements.txt'
            }
        }

        stage('Test') {
            steps {
                'pytest ./tests/'
                // sh 'pytest ./tests/'
            }
        }

        stage('Build') {
            steps {
                'streamlit run ./main.py --server.port 8080'
                // sh 'streamlit run ./main.py --server.port 8080'
            }
        }
    }
}