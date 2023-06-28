pipeline {
    agent any

    environment {
        IMAGE_NAME = "develeap"
        IMAGE_REPO = "public.ecr.aws/q1c0q0c4"
        VERSION = "${env.BUILD_NUMBER}"
        AWS_REGION = "us-east-1"
        GITHUB_TOKEN = credentials('github_token')
    }

    stages {
        stage ('(1) Git clone') {
            steps {
                git branch: 'main', url: 'https://github.com/shay79il/DeveleapCI'
            }
        }
        stage ('(2) Build image') {
            steps {
                dir("app"){
                    sh 'docker build -t develeap .'
                    sh 'docker tag ${IMAGE_NAME}:latest ${IMAGE_REPO}/${IMAGE_NAME}:${VERSION}'
                    sh 'docker image ls'
                }
            }
        }
        stage ('(3) Push image to AWS ECR'){
            steps {
                withCredentials([
                    [
                        $class: 'AmazonWebServicesCredentialsBinding',
                        credentialsId: 'AWS Credentials - jenkins',
                        accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                        secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                    ]
                    ]) {

                        sh 'aws ecr-public get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${IMAGE_REPO}'
                    }

                    sh 'docker push ${IMAGE_REPO}/${IMAGE_NAME}:${VERSION}'
            }
        }
        
        stage ('(4) Clone/Pull K8S repo'){
            steps {
                script{
                    if(fileExists('DeveleapGitops')) {
                        echo 'Cloned repo already exist - Pulling latest changes'

                        dir("DeveleapGitops") {
                            sh 'git config pull.rebase true'
                            sh 'git pull https://github.com/shay79il/DeveleapGitops.git feature'
                        }

                    } else {
                        echo 'Repo does NOT exist - Cloning the repo'
                        sh 'git clone -b feature https://github.com/shay79il/DeveleapGitops.git'
                    }

                }
            }
        }
        
        stage ('(5) Update Manifest'){
            steps {
                dir("DeveleapGitops/jenkins-demo"){
                    sh 'sed -i "s#${IMAGE_REPO}.*#${IMAGE_REPO}/${IMAGE_NAME}:${VERSION}#g" deployment.yaml'
                    sh 'grep "image" deployment.yaml'
                }
            }
        }
        
        stage ('(6) Commit & Push'){
            steps {
                dir("DeveleapGitops/jenkins-demo"){
                    sh "git config --global user.email 'jenkins@ci.com'"
                    sh 'git remote set-url origin https://${GITHUB_TOKEN}@github.com/shay79il/DeveleapGitops'
                    sh 'git checkout feature'
                    sh 'git add -A'
                    sh 'git commit -am "Updated image version for build - ${VERSION}"'
                    sh 'git push origin feature'
                }
            }
        }
        
        stage ('(7) Raise PR'){
            steps {
                dir("DeveleapGitops"){
                        sh 'gh pr create            \
                            --fill                  \
                            --base main             \
                            --head feature          \
                            --title "Updated image version for build - ${VERSION}"'
                    }
            }
        }
    }
}