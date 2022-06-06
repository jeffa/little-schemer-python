import unittest
from schemer.common import(insertL, multiinsertL)

class TestLoad(unittest.TestCase):

    def test_insertL(self):
        mylist = ["apple", "banana", "cherry"]
        mycopy = mylist.copy()
        self.assertEqual( insertL('pear', 'apple', mylist), ["pear", "apple", "banana", "cherry"], 'atom removed from lat' )
        self.assertEqual( insertL('peach', 'banana', mylist), ["apple", "peach", "banana", "cherry"], 'atom removed from lat' )
        self.assertEqual( insertL('plum', 'cherry', mylist), ["apple", "banana", "plum", "cherry"], 'atom removed from lat' )
        self.assertEqual( insertL('cherry', 'cola', mylist), mylist, 'atom is not in lat so not removed' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

    def test_multiinsertL(self):
        mylist = ["apple", "banana", "apple", "cherry", "apple"]
        mycopy = mylist.copy()
        self.assertEqual( multiinsertL('pear', 'apple', mylist), ["pear", "apple", "banana", "pear", "apple", "cherry", "pear", "apple"], 'atom substituted' )
        self.assertEqual( multiinsertL('peach', 'banana', mylist), ["apple", "peach", "banana", "apple", "cherry", "apple"], 'atom substituted' )
        self.assertEqual( multiinsertL('plum', 'cherry', mylist), ["apple", "banana", "apple", "plum", "cherry", "apple"], 'atom substituted' )
        self.assertEqual( multiinsertL('cherry', 'cola', mylist), mylist, 'atom is not in lat so not substituted' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

if __name__ == '__main__':
    unittest.main()
