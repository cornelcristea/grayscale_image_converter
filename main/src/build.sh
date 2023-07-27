#!/bin/sh
# bash ./main/src/build.sh this command will be called from yaml script
###########################
# VARIABLES
###########################
TARGET_DIR="../../target"
TEST_DIR=${TARGET_DIR}/"test"
PY_FILE="grayscale_image_converter.py"
EXE_FILE=${TARGET_DIR}/build/${SW_NAME}
###########################
# SETUP
###########################
cd ./main/src
echo "STATUS: Installing requiments"
python -m ensurepip --upgrade
pip install -r requiments.txt
# make 'target' folder if not exist
if [ ! -d ${TARGET_DIR} ]; then
    mkdir ${TARGET_DIR};
fi
###########################
# TEST
###########################
echo "STATUS: Testing source file"
# if test OK then Build
###########################
# BUILD
###########################
echo "STATUS: Building executable file"
# copy main.py in target folder
cp -r $(pwd)/main.py ${TARGET_DIR}/${PY_FILE}
cd ${TARGET_DIR}
pyinstaller ${PY_FILE} -y
###########################
# DEPLOY
###########################
# upload the .exe file to gitHub as artifact 
   
