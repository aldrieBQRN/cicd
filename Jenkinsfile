pipeline {
    agent any

    environment {
        // Updated to your system's Java 21 path based on previous steps
        JAVA_HOME = "/usr/lib/jvm/java-21-openjdk-amd64"
        DEPLOY = "/var/www/html"
    }

    stages {
        stage('Checkout') {
            steps {
                // Ensure YOUR_USERNAME is replaced with your actual GitHub username
                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/cicd.git',
                    credentialsId: 'github-pat'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install selenium webdriver-manager
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                # Remove the default index.html to ensure your file takes priority
                sudo rm -f ${DEPLOY}/index.html
               
                # Sync files to the web directory
                sudo rsync -av --delete --exclude='venv' --exclude='.git' ./ ${DEPLOY}/
               
                # Fix permissions
                sudo chown -R www-data:www-data ${DEPLOY}
                sudo chmod -R 755 ${DEPLOY}
                '''
            }
        }

        stage('Start Apache') {
            steps {
                // Jenkins needs the NOPASSWD visudo setup you did earlier for this
                sudo systemctl restart apache2
            }
        }

        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate
                # No Xvfb needed since we use --headless=new in test.py
                python test.py
                '''
            }
        }
    }

    post {
        always {
            // Clean up any stray chrome processes if needed
            sh 'pkill -u jenkins chrome || true'
        }
    }
}

