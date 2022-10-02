pipeline {
  agent any
  stages {
    stage('Setup') {
      steps {
        sh "$HOME/.local/bin/poetry install --no-root"      }
    }
    stage('Test') {
      steps {
        sh "$HOME/.local/bin/poetry run 'pytest'"
      }
    }
    stage('Build and publish') {
        when {
            branch "master"
        }
      steps {
        echo '$HOME/.local/bin/poetry publish --build'
      }
    }
  }
}
