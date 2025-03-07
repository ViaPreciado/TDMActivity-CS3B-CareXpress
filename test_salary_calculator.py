import unittest
from io import StringIO
import sys
from Base_Salary_Deduction_Code import SalaryCalculator  # Import the class from your main script

class TestSalaryCalculator(unittest.TestCase):

    def test_valid_salary(self):
        """Test with a valid salary."""
        calculator = SalaryCalculator(30000)
        self.assertEqual(calculator.gross_salary, 30000)
        self.assertEqual(calculator.sss_deduction, 1200)
        self.assertEqual(calculator.pagibig_deduction, 100)
        self.assertEqual(calculator.tax_deduction, 1875)
        self.assertAlmostEqual(calculator.philhealth_deduction, (30000 * 0.05) / 2)
        self.assertAlmostEqual(calculator.total_deductions, 1200 + 100 + 1875 + (30000 * 0.05) / 2)
        self.assertAlmostEqual(calculator.net_salary, 30000 - calculator.total_deductions)

    def test_zero_salary(self):
        """Test with zero salary (should raise ValueError)."""
        with self.assertRaises(ValueError):
            SalaryCalculator(0)

    def test_negative_salary(self):
        """Test with a negative salary (should raise ValueError)."""
        with self.assertRaises(ValueError):
            SalaryCalculator(-10000)

    def test_non_numeric_salary(self):
        """Test with a non-numeric salary (should raise TypeError)."""
        with self.assertRaises(TypeError):
            SalaryCalculator("Thirty thousand")

    def test_extremely_high_salary(self):
        """Test with an extremely high salary."""
        calculator = SalaryCalculator(100000000)
        self.assertEqual(calculator.gross_salary, 100000000)
        self.assertAlmostEqual(calculator.philhealth_deduction, (100000000 * 0.05) / 2)
        self.assertAlmostEqual(calculator.total_deductions, 1200 + 100 + 1875 + (100000000 * 0.05) / 2)
        self.assertAlmostEqual(calculator.net_salary, 100000000 - calculator.total_deductions)

    def test_display_salary_details(self):
        """Test if salary details are correctly printed."""
        calculator = SalaryCalculator(50000)
        expected_output = "\n--- Salary Breakdown ---\n" \
                          "Gross Salary: 50000.00\n" \
                          "SSS Deduction: 1200.00\n" \
                          f"PhilHealth Deduction: {(50000 * 0.05) / 2:.2f}\n" \
                          "Pag-IBIG Deduction: 100.00\n" \
                          "Tax Deduction: 1875.00\n" \
                          f"Total Deductions: {1200 + 100 + 1875 + (50000 * 0.05) / 2:.2f}\n" \
                          f"Net Salary: {50000 - (1200 + 100 + 1875 + (50000 * 0.05) / 2):.2f}\n"

        # Capture printed output
        sys.stdout = StringIO()
        calculator.display_salary_details()
        output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__  # Reset standard output

        self.assertEqual(output.strip(), expected_output.strip())

if __name__ == "__main__":
    unittest.main()
