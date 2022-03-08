import unittest

from core.image2ascii import toascii

class TestImage2Ascii(unittest.TestCase):
    
    def setUp(self) -> None:
        self.image_path = './src/test/assets/test.jpg'
    """
    Test if the image2ascii function works as expected.
    """
    def test_image2ascii(self):
        l =  toascii(self.image_path, max_height=15)
        self.assertTrue(len(l) > 0, "The image2ascii function doesn't work as expected.")

    """
    Should save to a file.
    """
    def test_savefile(self):
        l =  toascii(self.image_path, max_height=30)
        with open('./src/test/assets/test_output.txt', 'w') as f:
            f.write(l)
        self.assertTrue(len(l) > 0, "The image2ascii function doesn't work as expected.")

if __name__ == '__main__':
    unittest.main()