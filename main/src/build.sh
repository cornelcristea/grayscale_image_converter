#!/bin/sh

# bash ./main/src/build.sh this command will be called from yaml script


###########################
# VARIABLES
###########################
TARGET_DIR="./target"
TEST_FILE="./main/test/main_test.py"
SRC_FILE="./main/src/main.py"
REQ_FILE="./main/src/requiments.txt"
PY_FILE="grayscale_image_converter.py"
EXE_FILE=${TARGET_DIR}"/build/grayscale_image_converter.exe"
###########################
# SETUP
###########################
echo "STATUS: Installing requiments"
python -m ensurepip --upgrade
pip install -r ${REQ_FILE}
if [ ! -d ${TARGET_DIR} ]; then
    mkdir ${TARGET_DIR};
fi
###########################
# TEST
###########################
echo "STATUS: Testing source file"
python ${TEST_FILE}
status=$?
###########################
# BUILD
###########################
if [ ${status} -eq 0 ]; then
    echo "STATUS: Building executable file"
    cp -r ${SRC_FILE} ${TARGET_DIR}"/"${PY_FILE}
    cd ${TARGET_DIR}
    pyinstaller ${PY_FILE} -y
else
    echo "ERROR: Build failed"
fi
###########################
# DEPLOY
###########################
echo "STATUS: Deploy software"
# upload the .exe file to gitHub as artifact 


"""
# Replace with your GitHub personal access token and repository name
GITHUB_TOKEN="YOUR_PERSONAL_ACCESS_TOKEN"
REPO_OWNER="YOUR_GITHUB_USERNAME"
REPO_NAME="YOUR_REPOSITORY_NAME"

# Replace with the file you want to upload
FILE_TO_UPLOAD="path/to/your_file.txt"

# Step 1: Get the upload URL
response=$(curl -X POST -H "Authorization: token $GITHUB_TOKEN" \
             "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/actions/artifacts" \
             -d '{"name": "MyArtifact"}')
upload_url=$(echo "$response" | jq -r '.upload_url' | sed -e "s/{?name,label}//")

# Step 2: Upload the file
curl -X POST -H "Authorization: token $GITHUB_TOKEN" \
     -H "Content-Type: application/zip" \
     --data-binary @"$FILE_TO_UPLOAD" \
     "$upload_url?name=$(basename "$FILE_TO_UPLOAD")"
"""   
