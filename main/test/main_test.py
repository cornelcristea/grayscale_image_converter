
import unittest
from os import mkdir, remove
from shutil import copyfile, rmtree
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

        # make target/test folder in repository
        if not exists(target_dir):
            mkdir(target_dir)
            mkdir(test_dir)
        elif not exists(test_dir):
            mkdir(test_dir)
        
        print(" repo dir : " + repo_dir)
        print(" src dir : " + src_dir)
        copyfile(src_dir + "\\main.py", repo_dir + "\\main\\test\\main.py")

        return repo_dir

    def test_convert_image(self):
        # path variables
        repo_dir = UnitTestMain.setup()
        input_image = repo_dir + "\\main\\test\\image.jpg"
        output_dir = repo_dir + "\\target\\test"
        new_name = "image_grayscale"
        expected_image = output_dir + "\\" + new_name + ".jpg"

        # call main function
        import main
        output_image = main.convert_image(input_image, output_dir, new_name)

        # check existance of grayscale image
        if output_image == expected_image and exists(expected_image):
            test_result = True
        else:
            test_result = False
        
        # check result
        self.assertTrue(test_result)

        # delete cache files
        rmtree(repo_dir + "\\main\\test\\__pycache__")
        remove(repo_dir + "\\main\\test\\main.py")

if __name__ == "__main__":
    unittest.main()