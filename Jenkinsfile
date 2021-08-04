def docker_registry = 'registry.cn-hangzhou.aliyuncs.com'
def username = '小马哥保佑不脱发'
def password = '1997723ljx'

node {
	stage('拉取git仓库') {
		checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '1972c055-7fce-4da7-bd2b-41a7f176d4bc', url: 'git@github.com:lijixiang723/micro_service_demo.git']]])
	}

	stage('构建镜像打包'){
	sshPublisher(publishers: [sshPublisherDesc(configName: 'aliyun-ssh', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'sh /usr/sbin/start.sh', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: 'micro_service_demo', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '**/.*')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
	    }
}
