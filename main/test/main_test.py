
import unittest
from os import mkdir 
from shutil import rmtree
from os.path import exists, abspath, dirname
from sys import path, argv

class UnitTestMain(unittest.TestCase):
    @staticmethod
    def setup():
        # prepare test enviroment
        current_dir = dirname(abspath(argv[0]))
        pwd_list = current_dir.split("\\")
        repo_dir = "\\".join(pwd_list[:-2])
        target_dir = repo_dir + "\\target"
        test_dir = target_dir + "\\test"
        src_dir =  repo_dir + "\\main\\src" 

        # import source file as globally
        path.append(src_dir)
        import main
        globals()['main'] = main

        # make target/test folder in repository
        if not exists(target_dir):
            mkdir(target_dir)
            mkdir(test_dir)
        elif not exists(test_dir):
            mkdir(test_dir)
            
        return repo_dir

    def test_convert_image(self):
        # path variables
        repo_dir = UnitTestMain.setup()
        input_image = repo_dir + "\\main\\test\\image.jpg"
        output_dir = repo_dir + "\\target\\test"
        new_name = "image_grayscale"
        expected_image = output_dir + "\\" + new_name + ".jpg"

        # call main function
        output_image = main.convert_image(input_image, output_dir, new_name)

        # check existance of grayscale image
        if output_image == expected_image and exists(expected_image):
            test_result = True
        else:
            test_result = False
        
        # check result
        self.assertTrue(test_result)

        # delete cache files
        pycache_dir = repo_dir + "\\main\\src\\__pycache__"
        rmtree(pycache_dir)

if __name__ == "__main__":
    unittest.main()