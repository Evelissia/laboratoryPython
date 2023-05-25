import unittest
from webApp import calculate_monthly_payment

class MortgageCalculatorTests(unittest.TestCase):
    def test_calculate_monthly_payment(self):
        # Проверка расчета ежемесячного платежа
        loan_amount = 100000
        interest_rate = 5.0
        loan_term = 30

        expected_monthly_payment = 536.82

        monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term)

        self.assertAlmostEqual(monthly_payment, expected_monthly_payment, places=2)


    def test_calculate_monthly_payment_with_negative_loan_amount(self):
        # Проверка обработки отрицательной величины займа
        loan_amount = -100000
        interest_rate = 5.0
        loan_term = 30

        # Ожидаем получить исключение ValueError
        with self.assertRaises(ValueError):
            calculate_monthly_payment(loan_amount, interest_rate, loan_term)
            
    def test_calculate_monthly_payment_with_zero(self):
        loan_amount = 100000
        interest_rate = 0.0
        loan_term = 30

        monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term)

        self.assertEqual(monthly_payment, 0.0)

if __name__ == '__main__':
    unittest.main()