pipeline {
    agent { docker { image 'tiangolo/uvicorn-gunicorn-fastapi:python3.8' } }
    stages {
        stage('deps') {
            steps {
                sh 'pip3 install -r requirement.txt'
            }
        }
        stage('main') {
            steps {
                parallel (
                    'testing': {
                        sh 'pytest'
                    },
                    'linting': {
                        sh 'flake8 app_python'
                    }
                )
            }
        }
    }
}
