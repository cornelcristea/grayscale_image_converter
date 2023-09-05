# grayscale_image_converter

## Requirements:
1. Develop a python software that will convert a .jpg image to grayscale. As input, the software will have the following arguments:
- -i <image_path> - full path of your image<br>
- -o <output_folder> - folder where you want to save the new image<br>
- -n <new_name> - name of your new image
<br><br>
2. The life cycle of this software will be integrate in a CI/CD environment. For each commit in the "main" branch a workflow must be triggered and it will do the following steps:
- install python requiments <br>
- test the source file<br>
- build .exe file<br>
- deploy the .exe file as artifacts<br>
<br>
3. The environment for this project should be opened in a docker container<br>
Remark: create a docker image that will contain all necessary resources

## Implementation:
1. Software development: DONE
2. Unitary test development: DONE
3. Continuous Integration: ALMOST DONE
4. Docker Container: IN PROGRESS

## Build locally
To build locally run the shell script in the repo main folder
```bash
source build.sh -m debug
```
The -m input argumnet represents the build mode and it can be:
- debug - for sw test
- deploy - for sw build
