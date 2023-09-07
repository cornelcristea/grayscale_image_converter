#!/bin/sh

###########################
# LOCAL BUILD
###########################
# open a terminal in root of this repository and call the following command
#   source build.sh -m <mode>
#
# note: 
#   mode argument can be "test" or "deploy"
#
###########################
# ARGUMENT SETUP
###########################
help(){
    echo "Usage: $0 -m <mode>"
    echo -e "\t-m : mode can be *test* or *deploy*"
    exit 1
}

while getopts ":m:" opt;
do 
    case $opt in
        m) MODE=${OPTARG} ;;
        ?) help ;;
    esac
done

if [ -z "$MODE" ]
then
   echo "ERROR: Empty input argument";
   help
fi

###########################
# GLOBAL VARIABLES
###########################
TARGET_DIR="./target"
TEST_FILE="./main/test/main_test.py"
SRC_FILE="./main/src/main.py"
REQ_FILE="./main/src/requirements.txt"
PY_FILE="grayscale_image_converter.py"

###########################
# FUNCTIONS
###########################
install_req(){
    echo "STATUS: Installing requirements..."
    # python -m ensurepip --upgrade
    pip install -r ${REQ_FILE}
}

sw_test(){
    echo "STATUS: Test source file..."
    if [ ! -d ${TARGET_DIR} ]; then
        mkdir ${TARGET_DIR};
    fi
    python ${TEST_FILE}
}

build_exe() {
    status=$?
    if [ ${status} -eq 0 ]; then
        echo "STATUS: Build executable file..."
        cp -r ${SRC_FILE} ${TARGET_DIR}/${PY_FILE}
        cd ${TARGET_DIR}
        pyinstaller ${PY_FILE} -y 
        cd ..
        rm ${TARGET_DIR}/${PY_FILE}
    else
        echo "ERROR: Build failed."
    fi
}
###########################
# WORKFLOW
###########################
case ${MODE} in
    "test")
        install_req
        sw_test ;;
    "deploy")
        install_req
        sw_test
        build_exe ;;
    *)
        echo -e "Wrong input argument: $MODE \n"
        help ;;
esac