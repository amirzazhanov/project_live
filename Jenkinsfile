pipeline {
    agent { label 'build' }

    stages {
        stage("Checkout Repository") {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage("Build") {
            steps {
                script {
                    sh "docker compose build"
                }
            }
        }

        stage("Run Container") {
            steps {
                script {
                    sh "docker compose up -d"
                }
            }
        }

        stage("Run Tests") {
            steps {
                script {
                    println("Tested!")
                }
            }
        }

        stage("Stop Container") {
            steps {
                script {
                    sh "docker compose down"
                }
            }
        }

    }
}