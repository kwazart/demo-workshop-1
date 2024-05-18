// Этот Jenkinsfile выполняет следующие действия:

// Проверяет код из Git репозитория.
// Устанавливает необходимую версию Python и Pip.
// Устанавливает зависимости через requirements.txt.
// Запускает тесты.
// Запускает приложение.


// Для запуска под windows используется конструкция powershell 'Start-Job -ScriptBlock { scripts }' 
// Для запуска под linux используется конструкция sh 'scripts'

pipeline {
    agent { dockerfile true }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/kwazart/demo-workshop-1'
            }
        }

        stage('Running Tests') {
            steps {
                powershell 'Start-Job -ScriptBlock {pytest ./tests/}'
                // sh 'pytest ./tests/'
            }
        }

        // stage('Build') {
        //     steps {
        //         powershell 'Start-Job -ScriptBlock {streamlit run ./main.py --server.port 8000}'
        //         // sh 'streamlit run ./main.py --server.port 8000'
        //     }
        // }
    }
}