
import unittest
from os import mkdir
from shutil import rmtree
from os.path import exists, abspath, dirname, sep, realpath
from sys import argv
from importlib.util import spec_from_file_location, module_from_spec

class UnitTestMain(unittest.TestCase):
    @staticmethod
    def setup():
        # prepare test enviroment
        current_dir = dirname(realpath(__file__))
        pwd_list = current_dir.split(sep)
        repo_dir = sep.join(pwd_list[:-2])
        target_dir = repo_dir + sep + "target"
        test_dir = target_dir + sep + "test"

        # delete the old "target" folder
        if exists(target_dir):
            rmtree(target_dir) 

        # prepare new environment
        mkdir(target_dir)
        mkdir(test_dir)
        
        return repo_dir

    def test_convert_image(self):
        # path variables
        repo_dir = UnitTestMain.setup()
        input_image = repo_dir + sep + "main" + sep + "test" + sep + "image.jpg"
        output_dir = repo_dir + sep + "target" + sep + "test"
        new_name = "image_grayscale"
        expected_image = output_dir + sep + new_name + ".jpg"

        # call main function
        spec = spec_from_file_location("convert_image", repo_dir + sep + "main" + sep + "src" + sep + "main.py")
        main = module_from_spec(spec)
        spec.loader.exec_module(main)
        output_image = main.convert_image(input_image, output_dir, new_name)

        # delete cache files
        try:
            rmtree(repo_dir + sep + "main" + sep + "src" + sep + "__pycache__")
            rmtree(repo_dir + sep + "main" + sep + "test" + sep + "__pycache__")
        except:
            print("'__pycache__ folder cannot be deleted.")

        # check existance of grayscale image
        if output_image == expected_image and exists(expected_image):
            test_result = True
        else:
            test_result = False
        
        # check result
        self.assertTrue(test_result)
        

if __name__ == "__main__":
    unittest.main()