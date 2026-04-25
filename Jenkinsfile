pipeline {
    agent any

    environment {
        // Updated for Ubuntu 24.04 Java path
        JAVA_HOME = "/usr/lib/jvm/java-21-openjdk-amd64"
        DEPLOY = "/var/www/html"
    }

    stages {
        stage('Checkout') {
            steps {
                // Connects to your repository
                git branch: 'main',
                    url: 'https://github.com/aldrieBQRN/cicd.git',
                    credentialsId: 'github-pat'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                # Create and update the virtual environment
                python3 -m venv venv
                . venv/bin/activate
                pip install selenium webdriver-manager
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                # 1. Remove default Apache index to prevent priority conflicts
                sudo rm -f ${DEPLOY}/index.html
               
                # 2. Sync project files to the web server directory
                # We exclude venv and .git to keep the web server clean
                sudo rsync -av --delete --exclude='venv' --exclude='.git' . ${DEPLOY}/
               
                # 3. Set correct ownership and permissions for Apache
                sudo chown -R www-data:www-data ${DEPLOY}
                sudo chmod -R 755 ${DEPLOY}
                '''
            }
        }

        stage('Start Apache') {
            steps {
                // Wrapped in sh to avoid Groovy syntax errors
                sh 'sudo systemctl restart apache2'
            }
        }

        stage('Test') {
            steps {
                sh '''
                # Run the Selenium test against the freshly deployed site
                . venv/bin/activate
                python test.py
                '''
            }
        }
    }

    post {
        always {
            // Cleans up any background Chrome processes to free up memory
            sh 'pkill -u jenkins chrome || true'
        }
        success {
            echo 'Pipeline completed successfully! Site is live and tested.'
        }
        failure {
            echo 'Pipeline failed. Check the console output for details.'
        }
    }
}
