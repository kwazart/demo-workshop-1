// Этот Jenkinsfile выполняет следующие действия:

// Проверяет код из Git репозитория.
// Устанавливает необходимую версию Python и Pip.
// Устанавливает зависимости через requirements.txt.
// Запускает тесты.
// Запускает приложение.


// Для запуска под windows используется конструкция powershell 'Start-Job -ScriptBlock { scripts }' 
// Для запуска под linux используется конструкция sh 'scripts'

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
                powershell 'Start-Job -ScriptBlock {pip install -r ./requirements.txt}' 
                // sh 'pip install -r ./requirements.txt'
            }
        }

        stage('Saving dependencies') {
            steps {
                powershell 'Start-Job -ScriptBlock {pip freeze > ./requirements.txt}'
                // sh 'pip freeze > ./requirements.txt'
            }
        }

        stage('Running Tests') {
            steps {
                powershell 'Start-Job -ScriptBlock {pytest ./tests/}'
                // sh 'pytest ./tests/'
            }
        }

        stage('Build') {
            steps {
                powershell 'Start-Job -ScriptBlock {streamlit run ./main.py --server.port 8080}'
                // sh 'streamlit run ./main.py --server.port 8081'
            }
        }
    }
}