FROM jenkins/jenkins:lts
ENV JENKINS_USER admin
ENV JENKINS_PASS admin
USER root
RUN apt update && apt install -y software-properties-common && apt install -y python3
RUN set -xe \
    && apt update \
    && apt install -y python3-pip
RUN pip install --upgrade pip
USER jenkins
# Skip initial setup
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
# COPY default-user.groovy /usr/share/jenkins/ref/init.groovy.d/
COPY default-user.groovy /usr/share/jenkins/ref/init.groovy.d/
# COPY and install the plugins 
COPY plugins.txt /usr/share/jenkins/ref/
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt