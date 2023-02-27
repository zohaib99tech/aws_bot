pipeline {
  agent any
  
  stages {
    stage('Clone Git Repository') {
      steps {
        // Clone the Git repository to a workspace directory
        git url: 'https://github.com/zohaib99tech/aws_bot.git', branch: 'main'
      }
    }
    stage('Get Timestamp'){
      steps{
      def timeStamp = Calendar.getInstance().getTime().format('YYYYMMdd-hhmmss',TimeZone.getTimeZone('CST'))
      }
    }
    stage('Deploy AWS EC2 instance') {
      steps {
        // create temp.directory for CICD tests
        sh 'mkdir -p /var/lib/jenkins/CICD-tests/'+$timeStamp

        // Copy source to working directory
        sh 'cp ./* /var/lib/jenkins/CICD-tests/'+$timeStamp

        sh 'cd /var/lib/jenkins/CICD-tests/'+$timeStamp
        // Restart the application server on the EC2 instance
        sh 'python3 ./gitaction_ts.py'

      }
      // steps {
      //   // Use SSH to copy the code from the workspace directory to the EC2 instance
      //   sshagent(credentials: ['ec2-authkey']) {
      //     sh 'scp -r ./aws_bot ec2-user@ec2-54-90-234-39.compute-1.amazonaws.com:/home/ec2-user'
      //   }
        
      //   // Restart the application server on the EC2 instance
      //   sshagent(credentials: ['ec2-authkey']) {
      //     sh 'ssh ec2-user@ec2-54-90-234-39.compute-1.amazonaws.com "sudo python /home/ec2-user/aws_bot/gitaction_ts.py"'
      //   }
      // }
    }
  }
}
