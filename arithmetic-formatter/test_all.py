import unittest
from main import arithmetic_arranger

class TestArithmeticArranger(unittest.TestCase):

    def test_arrangement(self):
        actual = arithmetic_arranger(["3 + 5", "2 - 4", "42 + 2", "1 - 9999"])
        expected = "    3      2      42      1\n+   5  -   4  +   2  - 9999\n-----  -----  -----  ------"
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["3 + 5", "2 - 4", "42 + 2", "1 - 9999"]')

        actual = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
        expected = "   11      3801      1      123      1\n+   4  -  2999  +   2  +  49  - 9380\n-----  -------  -----  -----  ------"
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]')

    def test_too_many_problems(self):
        actual = arithmetic_arranger(["3 + 5", "2 - 4", "42 + 2", "1 - 9999", "9 - 8", "72 - 78"])
        expected = "Error: Too many problems."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many problems."')

    def test_incorrect_operator(self):
        actual = arithmetic_arranger(["3 + 5", "2 - 4", "42 + 2", "1 * 9999"])
        expected = "Error: Operator must be '+' or '-'."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that uses the "*" operator to return "Error: Operator must be \'\+\' or \'\-\'."')

    def test_too_many_digits(self):
        actual = arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 7", "123 + 49"])
        expected = "Error: Numbers cannot be more than four digits."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that has a number over 4 digits long to return "Error: Numbers cannot be more than four digits."')

    def test_only_digits(self):
        actual = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 7", "123 + 49"])
        expected = "Error: Numbers must only contain digits."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."')

    def test_actually_five_problems(self):
        actual = arithmetic_arranger(["96 + 42", "3801 - 2999", "45 + 7", "123 + 49", "988 + 40"])
        expected = "   96      3801      45      123      988\n+  42  -  2999  +   7  +  49  +  40\n-----  -------  -----  -----  -----"
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with five arithmetic problems.')

    def test_first_two_problems(self):
        actual = arithmetic_arranger(["3 + 5", "2 - 4"])
        expected = "  3      2\n+ 5  -   4\n---  -----"
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["3 + 5", "2 - 4"]')

    def test_no_problems(self):
        actual = arithmetic_arranger([])
        expected = ""
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with no problems.')

    def test_return_first_two_problems(self):
        actual = arithmetic_arranger(["3 + 5", "2 - 4"], True)
        expected = "  3      2\n+ 5  -   4\n---  -----\n  8     -2"
        self.assertEqual(actual, expected, 'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with ["3 + 5", "2 - 4"] and a second argument of `True`.')

    def test_return_five_problems_with_solutions(self):
        actual = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 7", "123 + 49", "988 + 40"], True)
        expected = "   32         1      45      123      988\n- 698  -  3801  +   7  +  49  +  40\n-----  -------  -----  -----  -----\n -666     -3800     52      172     1028"
        self.assertEqual(actual, expected, 'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with five arithmetic problems and a second argument of `True`.')

if __name__ == "__main__":
    unittest.main()