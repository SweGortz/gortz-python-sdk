pipeline {
  agent any
  stages {
    stage('Setup') {
      steps {
        sh "$HOME/.local/bin/poetry install --no-root"      }
    }
    stage('Test') {
      steps {
        sh "$HOME/.local/bin/poetry run 'pre-commit install'"
        sh "$HOME/.local/bin/poetry run 'pre-commit run --all'"
      }
    }
    stage('Build and publish') {
      steps {
        echo '$HOME/.local/bin/poetry publish --build'
      }
    }
  }
}
