pipeline {
    agent any
    environment {
        dockerImage = ''
        registry = 'romankojnok/fitnesscalculator'
        registryCredential = 'dockerhub-rk'
    }
    // Cloning Github Project
    stages {
         stage('Git Clone') {
            steps {
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-rk', url: 'https://github.com/roman-kojnok/qafinalproject/']]])

        }
    }
            // Building Docker Image
        stage('Build Image') {
            steps {
             script {
                    dockerImage = docker.build registry
            }
        }
    }
        // Testing
        stage('Test') {
            steps {
                echo "Testing..."
            }

        }

        // Pushing docker image to dockerhub
        stage('DockerHub Upload') {
            steps {
             script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
            }
        }
    }
}


     stage('Docker stop container') {
         steps {
            sh 'docker ps -f name=fitnesscalculatorContainer -q | xargs --no-run-if-empty docker container stop'
            sh 'docker container ls -a -fname=fitnesscalculatorContainer -q | xargs -r docker container rm'
         }
       }


    // Running Docker container
    stage('Docker Run') {
     steps{
         script {
            dockerImage.run("-p 5000:5000 --rm --name fitnesscalculatorContainer")
         }
      }
    }
  }
}
