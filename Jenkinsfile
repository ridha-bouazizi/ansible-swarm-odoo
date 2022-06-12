pipeline {
    agent any

    stages {
        stage('Clone deps') {
            steps {
                git credentialsId: 'github', url: 'https://github.com/ridha-bouazizi/ansible-swarm-odoo.git'
                sh 'ls'
            }
        }
    }
}