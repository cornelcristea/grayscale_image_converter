pipeline {
    agent {
        label 'remote_node'
    }

    environment {
        TARGET_DIR = './target'
        TEST_FILE = './main/test/main_test.py'
        SRC_FILE = './main/src/main.py'
        REQ_FILE = './main/src/requirements.txt'
        PY_FILE = 'grayscale_image_converter.py'
    }

    stages {
        stage('Install requirements') {
            steps {
                sh "pip install -r $REQ_FILE"
            }
        }

        stage('Unit test') {
            steps {
                sh "python $TEST_FILE"
            }
        }

        stage('Build') {
            steps {
                sh """
                    cp -r $SRC_FILE $TARGET_DIR/$PY_FILE
                    cd $TARGET_DIR
                    pyinstaller $PY_FILE -y
                    cd ..
                    cp $TARGET_DIR/build/grayscale_image_converter/grayscale_image_converter $TARGET_DIR/grayscale_image_converter.exe
                """
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! Deploying to production...'
        }
        failure {
            echo 'Pipeline failed. Notify the team...'
        }
    }
}
