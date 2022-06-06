import unittest
from schemer.common import(subst, subst2, multisubst)

class TestLoad(unittest.TestCase):

    def test_subst(self):
        mylist = ["apple", "banana", "cherry"]
        mycopy = mylist.copy()
        self.assertEqual( subst('pear', 'apple', mylist), ["pear", "banana", "cherry"], 'atom substituted' )
        self.assertEqual( subst('peach', 'banana', mylist), ["apple", "peach", "cherry"], 'atom substituted' )
        self.assertEqual( subst('plum', 'cherry', mylist), ["apple", "banana", "plum"], 'atom substituted' )
        self.assertEqual( subst('cherry', 'cola', mylist), mylist, 'atom is not in lat so not substituted' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

    def test_subst2(self):
        mylist = ["apple", "banana", "cherry"]
        mycopy = mylist.copy()
        self.assertEqual( subst2('pear', 'apple', 'banana', mylist), ["pear", "banana", "cherry"], 'atom substituted' )
        self.assertEqual( subst2('peach', 'banana', 'apple', mylist), ["peach", "banana", "cherry"], 'atom substituted' )
        self.assertEqual( subst2('plum', 'cherry', 'banana', mylist), ["apple", "plum", "cherry"], 'atom substituted' )
        self.assertEqual( subst2('plum', 'cola', 'cherry', mylist), ["apple", "banana", "plum"], 'atom substituted' )
        self.assertEqual( subst2('cherry', 'cola', 'vanilla', mylist), mylist, 'atom is not in lat so not substituted' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

    def test_multisubst(self):
        mylist = ["apple", "banana", "apple", "cherry", "apple"]
        mycopy = mylist.copy()
        self.assertEqual( multisubst('pear', 'apple', mylist), ["pear", "banana", "pear", "cherry", "pear"], 'atoms substituted' )
        self.assertEqual( multisubst('peach', 'banana', mylist), ["apple", "peach", "apple", "cherry", "apple"], 'atoms substituted' )
        self.assertEqual( multisubst('plum', 'cherry', mylist), ["apple", "banana", "apple", "plum", "apple"], 'atoms substituted' )
        self.assertEqual( multisubst('cherry', 'cola', mylist), mylist, 'atom is not in lat so not substituted' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

if __name__ == '__main__':
    unittest.main()
