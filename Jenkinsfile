pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m venv env'
                sh 'source env/bin/activate'
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install pytest'
                sh 'pip3 install pytest-cov'
                sh 'pip3 install coverage'
                sh 'pip3 install pylint'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 apply_pylint.py'

//                 sh 'python3 -m pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                sh 'deploy!!'
            }
        }
    }
}
