'''
Created on Feb 21, 2017

@author: Ben Rose

Pledge: I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
'''
import unittest
import hw4

class Test(unittest.TestCase):
    
    def test01(self):
        '''Tests pascal_row at 0,1,2,3, and 4.'''
        self.assertEqual(hw4.pascal_row(0), [1])
        self.assertEqual(hw4.pascal_row(1), [1,1])
        self.assertEqual(hw4.pascal_row(2), [1,2,1])
        self.assertEqual(hw4.pascal_row(3), [1,3,3,1])
        self.assertEqual(hw4.pascal_row(4), [1,4,6,4,1])
        
    def test02(self):
        '''Tests pascal_triangle at 0,1,2,3, and 4.'''
        self.assertEqual(hw4.pascal_triangle(0),[[1]])
        self.assertEqual(hw4.pascal_triangle(1),[[1],[1,1]])
        self.assertEqual(hw4.pascal_triangle(2),[[1],[1,1],[1,2,1]])
        self.assertEqual(hw4.pascal_triangle(3),[[1],[1,1],[1,2,1],[1,3,3,1]])
        self.assertEqual(hw4.pascal_triangle(4),[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
        
if __name__ == '__main__':
    unittest.main()