def docker_registry = 'registry.cn-hangzhou.aliyuncs.com'

node {
	stage('拉取git仓库') {
		checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '1972c055-7fce-4da7-bd2b-41a7f176d4bc', url: 'git@github.com:lijixiang723/micro_service_demo.git']]])
	}

	stage('构建镜像打包'){
	    // 登录到阿里云镜像仓库
	    sh "docker login -u ${username} -p ${password} ${aliyun_registry}"
	    // 打包镜像
	    sh "docker build -t jenkins_micro_test:latest ."
	    // 打标签
	    sh "docker tag jenkins_micro_test:latest ${docker_registry/li_jixiang/jixiang:jenkins_micro_test}"
	    sh "docker push ${docker_registry/li_jixiang/jixiang:jenkins_micro_test}"

	}
}
