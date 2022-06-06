import unittest
from schemer.common import insertL

class TestLoad(unittest.TestCase):

    def test_insertL(self):
        mylist = ["apple", "banana", "cherry"]
        mycopy = mylist.copy()
        self.assertEqual( insertL('pear', 'apple', mylist), ["pear", "apple", "banana", "cherry"], 'atom removed from lat' )
        self.assertEqual( insertL('peach', 'banana', mylist), ["apple", "peach", "banana", "cherry"], 'atom removed from lat' )
        self.assertEqual( insertL('plum', 'cherry', mylist), ["apple", "banana", "plum", "cherry"], 'atom removed from lat' )
        self.assertEqual( insertL('cherry', 'cola', mylist), mylist, 'atom is not in lat so not removed' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

if __name__ == '__main__':
    unittest.main()
