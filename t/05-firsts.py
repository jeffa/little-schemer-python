import unittest
from schemer.common import firsts

class TestLoad(unittest.TestCase):

    def test_firsts(self):
        mylist = [
            ["apple", "banana", "cherry"],
            ["plum", "pear", "peach"],
            ["bean", "carrot", "eggplant"],
        ]
        mycopy = mylist.copy()
        self.assertEqual( firsts([]), [], 'empty lat does not blow up' )
        self.assertEqual( firsts(mylist), ["apple", "plum", "bean"], 'extracted first element of each list' )
        self.assertEqual( firsts([
            [["five", "plums"], "four"],
            ["eleven", "green", "oranges"],
            [["no"], "more"],
        ]), [ ["five", "plums"], "eleven", ["no"] ], 'complex lat works' )
        self.assertEqual( mylist, mycopy, 'lat has not changed' )

if __name__ == '__main__':
    unittest.main()
