from Eval import Eval
import unittest


class EvalTest(unittest.TestCase):
    def test_expression_string_to_list(self):
        evaluator = Eval()
        evaluator.expression_string = "1+2+3+4"
        evaluator._get_expression_list()
        assert evaluator.expression_list == [1, '+', 2, '+', 3, '+', 4]

        evaluator = Eval()
        evaluator.expression_string = "12+23+34+45"
        evaluator._get_expression_list()
        assert evaluator.expression_list == [12, '+', 23, '+', 34, '+', 45]

        evaluator = Eval()
        evaluator.expression_string = "12*23/34^45-8"
        evaluator._get_expression_list()
        expected_result = [12, '*', 23, '/', 34, '^', 45, '-', 8]
        assert evaluator.expression_list == expected_result

    def test_exponents(self):
        new_eval = Eval()
        ans = new_eval.exponents([1, '*', 2, '^', 3, '+', 4])
        assert ans == [1, '*', 8, '+', 4]

    def test_multiplication_or_division(self):
        new_eval = Eval()
        ans = new_eval.multiplication_or_division([1, '*', 2, '-', 3, '+', 4])
        assert ans == [2, '-', 3, '+', 4]
        ans = new_eval.multiplication_or_division([1, '/', 2, '-', 3, '+', 4])
        assert ans == [0.5, '-', 3, '+', 4]

    def test_addition_or_subtraction(self):
        new_eval = Eval()
        ans = new_eval.addition_or_subtraction([1, '+', 2, '-', 3, '+', 4])
        assert ans == [3, '-', 3, '+', 4]
        ans = new_eval.addition_or_subtraction([1, '-', 2, '-', 3, '+', 4])
        assert ans == [-1, '-', 3, '+', 4]

    def test_order_emdas(self):
        new_eval = Eval()
        ans = new_eval.order_emdas([1, '+', 2, '-', 3, '+', 4])
        assert ans == 4
        ans = new_eval.order_emdas([12, '*', 23, '/', 34, '^', 45, '-', 8])
        assert ans == -8.0

    def test_init_with_invalid_string(self):
        # test for invalid placement of symbols
        expression = '1 + 3 - * 2'
        self.assertRaises(ValueError, Eval, expression)
        # test for invalid parentheses
        expression = '(4 + 2) * (18 +(24)'
        self.assertRaises(ValueError, Eval, expression)


if __name__ == '__main__':
    unittest.main()
