node {
	stage('git pull') {
		checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '1972c055-7fce-4da7-bd2b-41a7f176d4bc', url: 'git@github.com:lijixiang723/micro_service_demo.git']]])
	}
}
