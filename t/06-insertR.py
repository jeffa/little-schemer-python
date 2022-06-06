import unittest
from schemer.common import insertR

class TestLoad(unittest.TestCase):

    def test_insertR(self):
        mylist = ["apple", "banana", "cherry"]
        mycopy = mylist.copy()
        self.assertEqual( insertR('pear', 'apple', mylist), ["apple", "pear", "banana", "cherry"], 'atom removed from lat' )
        self.assertEqual( insertR('peach', 'banana', mylist), ["apple", "banana", "peach", "cherry"], 'atom removed from lat' )
        self.assertEqual( insertR('plum', 'cherry', mylist), ["apple", "banana", "cherry", "plum"], 'atom removed from lat' )
        self.assertEqual( insertR('cherry', 'cola', mylist), mylist, 'atom is not in lat so not removed' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

if __name__ == '__main__':
    unittest.main()
