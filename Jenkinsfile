pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python -m venv env'
                sh 'source env/bin/activate'
                sh 'python -m pip install --upgrade pip'
                sh 'pip install pytest'
                sh 'pip install pytest-cov'
                sh 'pip install coverage'
                sh 'pip install pylint'
            }
        }
        stage('Test') {
            steps {
                sh 'python apply_pylint.py'

//                 sh 'python -m pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                sh 'deploy!!'
            }
        }
    }
}
