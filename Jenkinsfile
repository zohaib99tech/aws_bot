pipeline {
  agent any
  
  stages {
    stage('Clone Git Repository') {
      steps {
        // Clone the Git repository to a workspace directory
        git url: 'https://github.com/zohaib99tech/aws_bot.git', branch: 'main'
      }
    }
    
    stage('Deploy to EC2 Instance') {
      steps {
        // Use SSH to copy the code from the workspace directory to the EC2 instance
        sshagent(credentials: ['AWSEC2_server']) {
          sh 'scp -r ./aws_bot ec2-user@ec2-54-90-234-39.compute-1.amazonaws.com:/home/ec2-user'
        }
        
        // Restart the application server on the EC2 instance
        sshagent(credentials: ['AWSEC2_server']) {
          sh 'ssh ec2-user@ec2-54-90-234-39.compute-1.amazonaws.com "sudo python /home/ec2-user/aws_bot/gitaction_ts.py"'
        }
      }
    }
  }
}
