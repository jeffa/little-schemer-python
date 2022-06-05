import unittest
from schemer.common import rember

class TestLoad(unittest.TestCase):

    def test_member(self):
        mylist = ["apple", "banana", "cherry"]
        mycopy = mylist.copy()
        self.assertEqual( rember('apple', mylist), ["banana", "cherry"], 'atom removed from lat' )
        self.assertEqual( rember('banana', mylist), ["apple", "cherry"], 'atom removed from lat' )
        self.assertEqual( rember('cherry', mylist), ["apple", "banana"], 'atom removed from lat' )
        self.assertEqual( rember('cola', mylist), mylist, 'atom is not in lat so not removed' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

if __name__ == '__main__':
    unittest.main()
