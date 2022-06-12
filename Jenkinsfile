pipeline {
    agent any

    stages {
        stage('Clone deps') {
            steps {
                git credentialsId: 'github', url: 'https://github.com/ridha-bouazizi/ansible-swarm-odoo.git'
                sh 'ls'
            }
        }
        stage('SonarQube analysis') {
            
            steps{
                script{
                    def scannerHome = tool 'sonarScanner';
                    withSonarQubeEnv('My SonarQube Server') {
                    sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }
        // stage ('testsonar - Build') {
        //         withEnv(["JAVA_HOME=${ tool '"+JDK+"' }", "PATH=${env.JAVA_HOME}/bin"]) {
        //             // Unable to convert a build step referring to "hudson.plugins.sonar.SonarRunnerBuilder". Please verify and convert manually if required.
        //             // Shell build step
        //             sh """
        //             #!/bin/bash
        //             set -e
        //             pip install nose coverage nosexcover pylint
        //             """
        //             // Shell build step
        //             sh """
        //             #!/bin/bash
        //             set -e
        //             nosetests -sv --with-xunit --xunit-file=nosetests.xml --with-xcoverage --xcoverage-file=coverage.xml 
        //             """ 
        //             }
        //     }
        // stage('Copy plugins') {
        //     steps {
        //         git credentialsId: 'github', url: 'https://github.com/ridha-bouazizi/ansible-swarm-odoo.git'
        //         sh 'ls'
        //     }
        // }
    }
}