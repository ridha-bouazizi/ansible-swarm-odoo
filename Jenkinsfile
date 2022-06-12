// Powered by Infostretch 

timestamps {

node () {

	stage ('testsonar - Checkout') {
 	 checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/ridha-bouazizi/ansible-swarm-odoo.git']]]) 
	}
	stage ('testsonar - Build') {
 	
withEnv(["JAVA_HOME=${ tool '"+JDK+"' }", "PATH=${env.JAVA_HOME}/bin"]) { 

// Unable to convert a build step referring to "hudson.plugins.sonar.SonarRunnerBuilder". Please verify and convert manually if required.		// Shell build step
sh """ 
#!/bin/bash
set -e
pip install nose coverage nosexcover pylint 
 """		// Shell build step
sh """ 
#!/bin/bash
set -e
nosetests -sv --with-xunit --xunit-file=nosetests.xml --with-xcoverage --xcoverage-file=coverage.xml 
 """ 
	}
}
}
}