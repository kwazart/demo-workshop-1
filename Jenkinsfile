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
        stage('Install requirements') {
            steps {
                sh 'make deps'
            }
        }

        stage('Running Tests') {
            steps {
//                 powershell 'Start-Job -ScriptBlock {pytest ./tests/}'
                sh 'make test'
            }
        }

        stage('Build Docker image') {
            steps {
//                 powershell 'Start-Job -ScriptBlock {docker build -t summary-img}'
                sh 'docker build -t summary-img'
            }
        }

        stage('Build Docker container') {
            steps {
//                 powershell 'Start-Job -ScriptBlock {docker run -d -p 8000:8000 main.app summary-img}'
                sh 'docker run -d -p 8000:8000 main.app summary-img'
            }
        }
    }
}