def calculate_sss_deduction(gross_salary):
    """Calculate SSS deduction (fixed value)."""
    SSS_DEDUCTION = 1200
    return SSS_DEDUCTION

def calculate_pagibig_deduction(gross_salary):
    """Calculate Pag-IBIG deduction (fixed value)."""
    PAGIBIG_DEDUCTION = 100
    return PAGIBIG_DEDUCTION

def calculate_tax_deduction(gross_salary):
    """Calculate tax deduction (fixed value for simplicity)."""
    TAX_DEDUCTION = 1875
    return TAX_DEDUCTION

def calculate_philhealth_deduction(gross_salary):
    """Calculate PhilHealth deduction (5% of salary divided by 2)."""
    philhealth_deduction = (gross_salary * 0.05) / 2
    return philhealth_deduction

def calculate_total_deductions(gross_salary):
    """Calculate total deductions."""
    sss_deduction = calculate_sss_deduction(gross_salary)
    philhealth_deduction = calculate_philhealth_deduction(gross_salary)
    pagibig_deduction = calculate_pagibig_deduction(gross_salary)
    tax_deduction = calculate_tax_deduction(gross_salary)
    total_deductions = sss_deduction + philhealth_deduction + pagibig_deduction + tax_deduction
    return total_deductions

def calculate_net_salary(gross_salary):
    """Calculate net salary."""
    total_deductions = calculate_total_deductions(gross_salary)
    net_salary = gross_salary - total_deductions
    return net_salary

def calculate_deductions(gross_salary):
    """Calculate individual salary deductions and return total deductions & net salary."""
    sss_deduction = calculate_sss_deduction(gross_salary)
    philhealth_deduction = calculate_philhealth_deduction(gross_salary)
    pagibig_deduction = calculate_pagibig_deduction(gross_salary)
    tax_deduction = calculate_tax_deduction(gross_salary)
    total_deductions = calculate_total_deductions(gross_salary)
    net_salary = calculate_net_salary(gross_salary)

    return {
        "gross_salary": gross_salary,
        "SSS": sss_deduction,
        "PhilHealth": philhealth_deduction,
        "Pag-IBIG": pagibig_deduction,
        "Tax": tax_deduction,
        "Total Deductions": total_deductions,
        "Net Salary": net_salary
    }

def display_salary_details(salary_details):
    """Display salary breakdown in a structured format."""
    print("\n--- Salary Breakdown ---")
    print(f"Gross Salary: {salary_details['gross_salary']:.2f}")
    print(f"SSS Deduction: {salary_details['SSS']:.2f}")
    print(f"PhilHealth Deduction: {salary_details['PhilHealth']:.2f}")
    print(f"Pag-IBIG Deduction: {salary_details['Pag-IBIG']:.2f}")
    print(f"Tax Deduction: {salary_details['Tax']:.2f}")
    print(f"Total Deductions: {salary_details['Total Deductions']:.2f}")
    print(f"Net Salary: {salary_details['Net Salary']:.2f}")

def main():
    """Main function to handle user input and process salary deductions."""
    try:
        gross_salary = float(input("Enter your monthly salary: "))

        if gross_salary < 0:
            print("Error: Salary must be a positive number.")
            return

        salary_details = calculate_deductions(gross_salary)
        display_salary_details(salary_details)

    except ValueError:
        print("Error: Invalid input. Please enter a numeric value for salary.")

if __name__ == "__main__":
    main()