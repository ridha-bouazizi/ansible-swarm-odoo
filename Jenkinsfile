pipeline {
    agent any

    stages {
        stage('Clone deps') {
            steps {
                git credentialsId: 'github', url: 'https://github.com/ridha-bouazizi/ansible-swarm-odoo.git'
                
            }
        }
        stage('SonarQube analysis') {
            
            steps{
                script{
                    def scannerHome = tool 'sonarScanner';
                    withSonarQubeEnv('sonarServer') {
                    sh 'ls'
                    sh "${scannerHome}/bin/sonar-scanner \
                    -Dsonar.projectKey=odooInspect \
                    -Dsonar.language=py \
                    -Dsonar.sourceEncoding=UTF-8 \
                    -Dsonar.python.xunit.reportPath=nosetests.xml \
                    -Dsonar.python.coverage.reportPath=coverage.xml \
                    -Dsonar.sources=./addons \
                    -Dsonar.host.url=http://172.31.95.121:9000 \
                    -Dsonar.login=6ac0526fbb81ed5c4e832824f5df114df2409759"
                    sh """
                    #!/bin/bash
                    set -e
                    pip install nose coverage nosexcover pylint
                    """
                    // Shell build step
                    sh """
                    #!/bin/bash
                    set -e
                    nosetests -sv --with-xunit --xunit-file=nosetests.xml --with-xcoverage --xcoverage-file=coverage.xml 
                    """ 
                    }
                }
            }
        }
        stage('Copy plugins') {
            steps {
                git credentialsId: 'github', url: 'https://github.com/ridha-bouazizi/ansible-swarm-odoo.git'
                sh 'cp -r ./addons/* /addons/'
            }
        }
    }
}