# grayscale_image_converter

## Description:
Develop a software that will convert a .jpg image to grayscale. As input arguments, the software will have the following arguments:
- -i <image_path> - full path of your image
- -o <output_folder> - folder where you want to save the new image
- -n <new_name> - name of your new image

command: grayscale_img_converter.exe -i <image_path> -o <output_folder> -n <new_name>

## Build
To build the software locally, execute the following command in the root folder of this project:
```bash
source build.sh -m deploy
```

## CI/CD
GitHub Action was used to perform automatic workflow for software life cycle.
For every push on main branch, a runner will be triggered and it will perform the following steps:
- install requirements
- test source code
- build exe file
- deploy exe file

Pipeline link: https://github.com/cornelcristea/grayscale_image_converter/actions

## Docker Container
#### Requirements: 
- Docker Desktop
- Dev Container extension for VS Code

#### Configure:
- Create a docker account on https://hub.docker.com/ website to be able to build the container.
- After the account was created, execute the following commnad in terminal (replace DOCKER_USER and DOCKER_PASS with your credentials)
```bash
    docker login -u DOCKER_USER -p DOCKER_PASS
```
<i>If "daemon error" is present during login process, please open Docker Desktop -> Settings -> Docker Engine and be sure that "debug" parameter is present like in the following example:</i>
```bash
    "experimental": false,
    "debug": true
```
#### Open Container:
- Open project folder in VS Code
- from View menu select Command Palette
- search and select "Reopen in Container" option