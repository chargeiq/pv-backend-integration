// docker build options
env.DOCKER_BUILD_OPTIONS = "--network host"

podTemplate {
    node('jenkins-slave') {
        container('container') {
            stage('pull git repository') {
                //pull current branch
                checkout scm
                // write branch name to environment
                env.REPO_NAME = scm.getUserRemoteConfigs()[0].getUrl().tokenize('/').last().split("\\.")[0]
            }

            stage('build/push docker image') {
                // Docker Registry defined as ENV in Pod Template
                docker.withRegistry("${env.DOCKER_REGISTRY}", "ecr:eu-central-1:aws-credentials-dev") {
                    // build image from Dockerfile
                    def customImage = docker.build("${env.REPO_NAME}/${env.BRANCH_NAME}:${env.BUILD_ID}", "${env.DOCKER_BUILD_OPTIONS} -f Dockerfile . ")
                    // push to registry with jenkins build number
                    customImage.push()
                    // set also latest tag
                    customImage.push("latest")
                }  
            }

            stage('deploy to kubernetes') {
                // deploy to kubernetes
                sh '''
                    kubectl rollout restart -f ${REPO_NAME}.y*ml || kubectl apply -f ${REPO_NAME}.y*ml
                    # kubectl apply all .yaml or .yml files
                    for i in *.y*ml;do
                        kubectl apply -f \$i
                    done
                '''  
            }
        }
    }
}