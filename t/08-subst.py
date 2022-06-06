import unittest
from schemer.common import subst

class TestLoad(unittest.TestCase):

    def test_subst(self):
        mylist = ["apple", "banana", "cherry"]
        mycopy = mylist.copy()
        self.assertEqual( subst('pear', 'apple', mylist), ["pear", "banana", "cherry"], 'atom removed from lat' )
        self.assertEqual( subst('peach', 'banana', mylist), ["apple", "peach", "cherry"], 'atom removed from lat' )
        self.assertEqual( subst('plum', 'cherry', mylist), ["apple", "banana", "plum"], 'atom removed from lat' )
        self.assertEqual( subst('cherry', 'cola', mylist), mylist, 'atom is not in lat so not removed' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

if __name__ == '__main__':
    unittest.main()
