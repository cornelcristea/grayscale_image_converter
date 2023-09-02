# grayscale_image_converter
<br>

## Requiments:
1. Develop a python software that will convert a .jpg image to grayscale. As input, the software will have the following arguments:
<br><br>
-i <image_path> - full path of your image<br>
-o <output_folder> - folder where you want to save the new image<br>
-n <new_name> - name of your new image

2. The life cycle of this software will be integrate in a CI/CD environment
<br>
Remark: For each commit in the "main" branch an agent must be triggered and it will do the following steps:<br>
- install python requiments
- test the source file
- build .exe file if test is passed
- deploy the .exe file as artifacts
<br>

## Implementation:
1. Software development: DONE
2. Unitary test development: DONE
3. Continuous Integration: IN PROGRESS
