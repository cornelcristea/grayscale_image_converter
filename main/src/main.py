
# import libraries
from cv2 import imread, cvtColor, COLOR_BGR2GRAY, imwrite
from sys import argv
from os.path import join

# sw version
VERSION = "1.0.0"

# this is the main function of the program
def convert_image(input_image, output_dir, new_name):
    output_name = new_name + ".jpg"
    output_image = join(output_dir, output_name)
    
    print("Reading the input file...")
    img = imread(input_image)

    print("Convert the image to grayscale...")
    try:
        img_gray = cvtColor(img, COLOR_BGR2GRAY)
        imwrite(output_image, img_gray)
        print("The image was converted with success.")
    except:
        print("ERROR: The image cannot be converted.")

# display info 
print("===============================\n")
print(f"GARYSCALE IMAGE CONVERTER {VERSION}")
print("\nThis software will convert a .jpg image to grayscale. Please add the following parameters:\n"
    "\n<image_path> - full path of your image"
    "\n<output_folder> - folder where you want to save the new image"
    "\n<new_name> - name of your new image\n"
    "\nexample: python img_converter.py -i <image_path> -o <output_folder> -n <new_name>\n")
print("===============================")

# check input parameters
try:
    img_path = argv[1]
    out_dir = argv[3]
    new_name = argv[5]
except IndexError:
    print("ERROR: Missing input parameter.")

# call main function
convert_image(img_path, out_dir, new_name)