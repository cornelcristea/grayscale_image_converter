import unittest
from os import mkdir
from os.path import exists, join
from shutil import copy2


class MainTest(unittest.TestCase):

    @staticmethod
    def setup():
        test_dir = "..//..//target//test"
        src_dir = "..//src"
        if not exists(test_dir):
            try:
                mkdir(test_dir)
            except:
                print("ERROR: The ""target"" folder cannot be created.")

            copy2(join(src_dir, "//main.py"), join(test_dir, "//main.py"))


    def convert_image_test(self):
        MainTest.setup()
        # variables
        input_image = ".//img_input.jpg"
        output_dir = "./"
        new_name = "img_out"
        img_ref = ".//img_reference.jpg"

        # call main function
        from main import convert_image
        img_out = convert_image(input_image, output_dir, new_name)

        # check result
        self.assertEqual(img_out, img_ref)
