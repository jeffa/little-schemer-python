import unittest
from schemer.common import member

class TestLoad(unittest.TestCase):

    def test_member(self):
        mylist = ["apple", "banana", "cherry"]
        mycopy = mylist.copy()
        self.assertEqual( member('apple', mylist), True, 'atom is in lat' )
        self.assertEqual( member('banana', mylist), True, 'atom is in lat' )
        self.assertEqual( member('cherry', mylist), True, 'atom is in lat' )
        self.assertEqual( member('cola', mylist), False, 'atom is not in lat' )
        self.assertEqual( mylist, mycopy, 'list has not changed' )

if __name__ == '__main__':
    unittest.main()
