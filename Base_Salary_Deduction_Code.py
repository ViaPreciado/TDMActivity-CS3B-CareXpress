class SalaryCalculator:
    def __init__(self, gross_salary):
        if not isinstance(gross_salary, (int, float)):
            raise TypeError("Salary must be a number.")
        if gross_salary <= 0:
            raise ValueError("Salary must be a positive number.")

        self.gross_salary = gross_salary
        self.sss_deduction = self.calculate_sss_deduction()
        self.philhealth_deduction = self.calculate_philhealth_deduction()
        self.pagibig_deduction = self.calculate_pagibig_deduction()
        self.tax_deduction = self.calculate_tax_deduction()
        self.total_deductions = self.calculate_total_deductions()
        self.net_salary = self.calculate_net_salary()

    def calculate_sss_deduction(self):
        """Calculate SSS deduction (fixed value)."""
        return 1200

    def calculate_pagibig_deduction(self):
        """Calculate Pag-IBIG deduction (fixed value)."""
        return 100

    def calculate_tax_deduction(self):
        """Calculate tax deduction (fixed value for simplicity)."""
        return 1875

    def calculate_philhealth_deduction(self):
        """Calculate PhilHealth deduction (5% of salary divided by 2)."""
        return (self.gross_salary * 0.05) / 2

    def calculate_total_deductions(self):
        """Calculate total deductions."""
        return (
            self.sss_deduction + self.philhealth_deduction +
            self.pagibig_deduction + self.tax_deduction
        )

    def calculate_net_salary(self):
        """Calculate net salary."""
        return self.gross_salary - self.total_deductions

    def get_salary_details(self):
        """Return salary details as a dictionary."""
        return {
            "Gross Salary": self.gross_salary,
            "SSS Deduction": self.sss_deduction,
            "PhilHealth Deduction": self.philhealth_deduction,
            "Pag-IBIG Deduction": self.pagibig_deduction,
            "Tax Deduction": self.tax_deduction,
            "Total Deductions": self.total_deductions,
            "Net Salary": self.net_salary
        }

    def display_salary_details(self):
        """Display salary breakdown in a structured format."""
        details = self.get_salary_details()
        print("\n--- Salary Breakdown ---")
        for key, value in details.items():
            print(f"{key}: {value:.2f}")


def get_valid_salary():
    """Function to get valid salary input from the user."""
    while True:
        try:
            gross_salary = input("Enter your monthly salary: ").strip()
            
            # Ensure it's a valid number
            if not gross_salary.replace('.', '', 1).isdigit():
                raise ValueError("Invalid input. Please enter a valid numeric salary.")
            
            gross_salary = float(gross_salary)
            
            # Ensure salary is positive
            if gross_salary <= 0:
                raise ValueError("Salary must be a positive number.")
            
            return gross_salary
        except ValueError as e:
            print(f"Error: {e}. Please try again.")


def main():
    """Main function to handle user input and process salary deductions."""
    gross_salary = get_valid_salary()
    
    calculator = SalaryCalculator(gross_salary)
    calculator.display_salary_details()


if __name__ == "__main__":
    main()
