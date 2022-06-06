import unittest
from schemer.common import(insertR, multiinsertR)

class TestLoad(unittest.TestCase):

    def test_insertR(self):
        mylist = ["apple", "banana", "cherry"]
        mycopy = mylist.copy()
        self.assertEqual( insertR('pear', 'apple', mylist), ["apple", "pear", "banana", "cherry"], 'atom removed from lat' )
        self.assertEqual( insertR('peach', 'banana', mylist), ["apple", "banana", "peach", "cherry"], 'atom removed from lat' )
        self.assertEqual( insertR('plum', 'cherry', mylist), ["apple", "banana", "cherry", "plum"], 'atom removed from lat' )
        self.assertEqual( insertR('cherry', 'cola', mylist), mylist, 'atom is not in lat so not removed' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

    def test_multiinsertR(self):
        mylist = ["apple", "banana", "apple", "cherry", "apple"]
        mycopy = mylist.copy()
        self.assertEqual( multiinsertR('pear', 'apple', mylist), ["apple", "pear", "banana", "apple", "pear", "cherry", "apple", "pear"], 'atom substituted' )
        self.assertEqual( multiinsertR('peach', 'banana', mylist), ["apple", "banana", "peach", "apple", "cherry", "apple"], 'atom substituted' )
        self.assertEqual( multiinsertR('plum', 'cherry', mylist), ["apple", "banana", "apple", "cherry", "plum", "apple"], 'atom substituted' )
        self.assertEqual( multiinsertR('cherry', 'cola', mylist), mylist, 'atom is not in lat so not substituted' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

if __name__ == '__main__':
    unittest.main()
