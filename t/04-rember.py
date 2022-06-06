import unittest
from schemer.common import(rember, multirember)

class TestLoad(unittest.TestCase):

    def test_rember(self):
        mylist = ["apple", "banana", "cherry", "banana"]
        mycopy = mylist.copy()
        self.assertEqual( rember('apple', mylist), ["banana", "cherry", "banana"], 'atom removed from lat' )
        self.assertEqual( rember('banana', mylist), ["apple", "cherry", "banana"], 'atom removed from lat' )
        self.assertEqual( rember('cherry', mylist), ["apple", "banana", "banana"], 'atom removed from lat' )
        self.assertEqual( rember('cola', mylist), mylist, 'atom is not in lat so not removed' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

    def test_multirember(self):
        mylist = ["coffee", "cup", "tea", "cup", "hick", "cup", "coffee"]
        mycopy = mylist.copy()
        self.assertEqual( multirember('cup', mylist), ["coffee", "tea", "hick", "coffee"], 'atoms removed from lat' )
        self.assertEqual( multirember('coffee', mylist), ["cup", "tea", "cup", "hick", "cup"], 'atoms removed from lat' )
        self.assertEqual( multirember('cola', mylist), mylist, 'atom is not in lat so not removed' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

if __name__ == '__main__':
    unittest.main()
