# grayscale_image_converter

# Description:
Develop a software that will convert a .jpg image to grayscale. As input arguments, the software will have the following arguments:
- -i <image_path> - full path of your image
- -o <output_folder> - folder where you want to save the new image
- -n <new_name> - name of your new image

command: grayscale_img_converter.exe -i <image_path> -o <output_folder> -n <new_name>

# Build locally
To build locally run the shell script in the repo main folder
```bash
source build.sh -m debug
```
The -m input argumnet represents the build mode and it can be:
- debug - for test process
- deploy - for build process

# CI/CD
GitHub Action was used to perform automatic workflow for software life cycle.
For every push on main branch, a runner will be triggered and it will perform the following steps:
- install requirements
- test source code
- build exe file
- deploy exe file

Pipeline link: https://github.com/cornelcristea/grayscale_image_converter/actions

# Docker Container
## Requirements: 
- Docker Desktop
- Dev Container extension for VS Code

## Configure
Create a docker account on https://hub.docker.com/ website to be able to build the container.
After the account was created, execute the following commnad in terminal 
```bash
    docker login -u DOCKER_USER -p DOCKER_PASSWORD
```
* In my case, I created a shell script that will execute this command

If "daemon error" is present during login process, please follow the instructions from below:
Open Docker app -> Settings --> Docker Engine --> After the following line 
```bash
    "experimental": false
```
Add a new one with following instruction:
```bash
    "debug": true
```
Save and Restart Docker.

## Open Container
- Open project folder in VS Code
- from View menu select Command Palette
- search and select "Reopen in Container" option