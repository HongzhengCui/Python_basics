from clock import MyClock24
import unittest

class TestClock(unittest.TestCase):
        
    def test_create(self):
        """ test creation """
 
        a = MyClock24(1,5,30)
        self.assertEqual(str(a),"01:05:30")

    def test_create_errors(self):
        """ test creation with bad ranges"""

        with self.assertRaises(Exception) as context:
            b = MyClock24(25,5,30)
        self.assertTrue(type(context.exception) == ValueError,"Not handling hour out of range properly")

        with self.assertRaises(Exception) as context:
            b = MyClock24(5,65,30)
        self.assertTrue(type(context.exception) == ValueError,"Not handling minutes out of range properly")

        with self.assertRaises(Exception) as context:
            b = MyClock24(5,5,95)
        self.assertTrue(type(context.exception) == ValueError,"Not handling seconds out of range properly")

        with self.assertRaises(Exception) as context:
            b = MyClock24(-1,5,30)
        self.assertTrue(type(context.exception) == ValueError,"Not handling hour out of range properly")

        with self.assertRaises(Exception) as context:
            b = MyClock24(5,-1,30)
        self.assertTrue(type(context.exception) == ValueError,"Not handling minutes out of range properly")

        with self.assertRaises(Exception) as context:
            b = MyClock24(5,5,-1)
        self.assertTrue(type(context.exception) == ValueError,"Not handling seconds out of range properly")


    def test_str(self):
        """ test __str__ works correctly - formatting """
        a = MyClock24(7,7,7)
        self.assertEqual(str(a),"07:07:07")

        b = MyClock24(23,59,59)
        self.assertEqual(str(b),"23:59:59")

    def test_repr(self):
        """ testing __repr__ """
        import ast

        b = MyClock24(23,59,58)
        self.assertEqual(ast.literal_eval(repr(b)),{'hours': 23, 'minutes': 59, 'seconds': 58})

    def test_properties(self):
        """ test access comparisons """
        a = MyClock24(23,59,58)
        self.assertEqual(a.hours,23)
        self.assertEqual(a.minutes,59)
        self.assertEqual(a.seconds,58)

    def test_comparisons(self):
        """ test that the magic methods implemented for comparisons """
        a = MyClock24(23,59,58)
        b = MyClock24(23,59,58)
        c = MyClock24(0,0,0)

        self.assertTrue(a == b, "Equality should be true")
        self.assertFalse(a == c, "equality should fail")

        self.assertFalse(a != b, "inequality check should fail")
        self.assertTrue(a != c, "inequality should succeed")

        self.assertTrue(a  >  c ,"greater than")
        self.assertTrue(a >= b, "greater than equals")

        self.assertTrue(c < a ,"less than")
        self.assertTrue(b <= a, "less than equals")

    def test_arithmetic(self):
        """ test arithmetic """
        a = MyClock24(23,59,58)
        b = a + 3
        self.assertEqual(str(b),"00:00:01")
        c = b - 3
        self.assertTrue( a == c)

        b = MyClock24(0,0,3)
        c = a + b
        self.assertEqual(str(c),"00:00:01")
        d = c - b
        self.assertTrue( a == d)

    def test_tick(self):
        """ test tick()"""
        a = MyClock24(23,59,0)
        for i in range(70):
            a.tick()
        self.assertEqual(str(a),"00:00:10")

