import unittest
from schemer.common import *

class TestLoad(unittest.TestCase):

    def test_lat(self):
        mylist = ["apple", "banana", "cherry"]
        mycopy = mylist.copy()
        self.assertEqual( lat('mylist'), False, 'atom is not a lat' )
        self.assertEqual( lat(['a','b','c']), True, 'lat is a lat' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

if __name__ == '__main__':
    unittest.main()
