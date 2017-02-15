# test_babyset.py
import unittest

from baby_set import BabySet

class TestBabySetMethods(unittest.TestCase):

    def test_init(self):
        bset = BabySet([2, 4, 4])
        self.assertEqual(bset.size(), 2)

    def test_init_empty(self):
        bset = BabySet()
        self.assertEqual(bset.size(), 0)

    def test_add(self):
        bset = BabySet([2, 4, 4])
        bset.add(4)
        self.assertEqual(bset.size(), 2)
    
    def test_addSeq(self):
        bset = BabySet([2, 4, 4])
        bset.addSeq([3, 4, 5,])
        self.assertEqual(bset.size(), 4)

    def test_get(self):
    	bset = BabySet([2, 4, 4])
        with self.assertRaises(KeyError):
            bset.get(3)

    def test_remove(self):
        bset = BabySet([2, 4, 4])
        self.assertEqual(bset.remove(4), 4) #remove element 4 from set 
        self.assertEqual(bset.size(), 1)    #returns size of updated set
        with self.assertRaises(KeyError):   #raises error when value does not exist in set
            bset.remove(3)

    def test_clear(self):
        bset = BabySet()                    #defines emtpy set
        self.assertEqual(bset.size(), 0)    #checks size of set


if __name__ == '__main__':
    unittest.main()