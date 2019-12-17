# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()

# from pysd import read_vensim
import pysd

data = pysd.read_vensim('50 years average.mdl')