pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh "poetry run pytest"
      }
    }
    stage('Build') {
      steps {
        echo 'poetry publish --build'
      }
    }
  }
}
