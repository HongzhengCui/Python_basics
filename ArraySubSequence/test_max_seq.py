import unittest
from max_seq import max_seq

class TestMaxSequence(unittest.TestCase):
    def test_valid_list(self):
        self.assertEqual(max_seq([1,2,1,3,5,8,2,4,6,9]), [1,3,5,8], "The result is not expected")  
        
    def test_illegal_list(self):
        with self.assertRaises(Exception) as context:
            max_seq(["a","b",1,2,3,5,8,2,4,6,9])
        self.assertTrue(type(context.exception) == TypeError,"All elements in the list must be int or float")
        
    def test_empty_list(self):
        self.assertEqual(max_seq([]), [])