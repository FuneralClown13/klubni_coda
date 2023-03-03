import unittest
from Calculator import calculate


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculate = calculate

    def test_one_num(self):
        self.assertEqual(self.calculate('5'), 5)
        self.assertEqual(self.calculate('1.1'), 1.1)

    def test_add(self):
        self.assertEqual(self.calculate('5 + 5'), 10)
        self.assertEqual(self.calculate('5+10'), 15)
        self.assertEqual(self.calculate('999+1'), 1000)

    def test_sub(self):
        self.assertEqual(self.calculate('18 - 2'), 16)
        self.assertEqual(self.calculate('21-7'), 14)
        self.assertEqual(self.calculate('25- 2 . 3 3'), 22.67)

    def test_mul(self):
        self.assertEqual(self.calculate('2 * 2'), 4)
        self.assertEqual(self.calculate('0.1*10'), 1)
        self.assertEqual(self.calculate('12.5*2'), 25)

    def test_div(self):
        self.assertEqual(self.calculate('18 / 2'), 9)
        self.assertEqual(self.calculate('21/7'), 3)
        self.assertEqual(self.calculate('25/2'), 12.5)

    def test_combined(self):
        self.assertEqual(self.calculate('5+8-8*2/4'), 9)
        self.assertEqual(self.calculate('5*4*3*2*1'), 120)
        self.assertEqual(self.calculate('5*4+3-2*1'), 21)

    def test_bad_request(self):
        """if you enter an invalid character ->'Bad request' """
        bad_request = 'Bad request'
        self.assertTrue(self.calculate('3x+1') == bad_request)
        self.assertTrue(self.calculate('zzz') == bad_request)
        self.assertTrue(self.calculate('3f+1-1') == bad_request)

    def test_object_type(self):
        """if you enter an invalid character ->'Bad object type' """
        bad_object_type = 'Bad object type'
        self.assertTrue(self.calculate(True) == bad_object_type)
        self.assertTrue(self.calculate((1,)) == bad_object_type)
        self.assertTrue(self.calculate(256) == bad_object_type)
        self.assertTrue(self.calculate(['5+5']) == bad_object_type)

    def test_zero_division(self):
        """if you enter some / zero -> 'Zero division error'"""
        self.assertEqual(self.calculate('2/0'), 'Zero division error')
        self.assertEqual(self.calculate('2/10/0'), 'Zero division error')

if __name__ == '__main__':
    unittest.main()
