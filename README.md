# grayscale_image_converter
<br>

## Requiments:
1. Develop a python software that will convert a .jpg image to grayscale. As input, the software will have the following arguments:
<br><br>
-i <image_path> - full path of your image<br>
-o <output_folder> - folder where you want to save the new image<br>
-n <new_name> - name of your new image<br>
<br><br>
<b>STATUS:<b> DONE
<br><br>
2. The softare should be called with the following command in terminal:
cmd: img_converter.exe -i <image_path> -o <output_folder> -n <new_name>
<b>STATUS:<b> DONE
<br><br>
3. Develop the unitary test (at least one) for this software.
<b>STATUS:<b> DONE
<br><br>
3. The life cycle of this software will be integrate in a CI/CD environment. <br>
For each commit in the "main" branch an agent must be triggered and it will do the following steps:<br>
- install python requiments
- test the source file
- build .exe file if test is passed
- deploy the .exe file as artifacts
<br>
<b>STATUS:<b> IN PROGRESS
<br><br>