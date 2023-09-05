
import unittest
from os import mkdir 
from shutil import rmtree
from os.path import exists, abspath, dirname, sep
from sys import argv
from importlib.util import spec_from_file_location, module_from_spec

class UnitTestMain(unittest.TestCase):
    @staticmethod
    def setup():
        # prepare test enviroment
        current_dir = dirname(abspath(argv[0]))
        pwd_list = current_dir.split(sep)
        repo_dir = sep.join(pwd_list[:-2])
        target_dir = repo_dir + sep + "target"
        test_dir = target_dir + sep + "test"

        # make target/test folder in repository
        if not exists(target_dir):
            mkdir(target_dir)
            mkdir(test_dir)
        elif not exists(test_dir):
            mkdir(test_dir)
        
        print("REPO DIR === " + repo_dir)
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
        rmtree(repo_dir + sep + "main" + sep + "src" + sep + "__pycache__")

        # check existance of grayscale image
        if output_image == expected_image and exists(expected_image):
            test_result = True
        else:
            test_result = False
        
        # check result
        self.assertTrue(test_result)
        

if __name__ == "__main__":
    unittest.main()