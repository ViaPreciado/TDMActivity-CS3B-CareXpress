def calculate_deductions(gross_salary):
    """Calculate individual salary deductions and return total deductions & net salary."""
    
    SSS_DEDUCTION = 1200
    PAGIBIG_DEDUCTION = 100
    TAX_DEDUCTION = 1875  # Assuming fixed value for simplicity

    # Compute PhilHealth deduction (5% of salary divided by 2)
    philhealth_deduction = (gross_salary * 0.05) / 2

    # Total deductions calculation
    total_deductions = SSS_DEDUCTION + philhealth_deduction + PAGIBIG_DEDUCTION + TAX_DEDUCTION

    # Compute net salary
    net_salary = gross_salary - total_deductions

    return {
        "gross_salary": gross_salary,
        "SSS": SSS_DEDUCTION,
        "PhilHealth": philhealth_deduction,
        "Pag-IBIG": PAGIBIG_DEDUCTION,
        "Tax": TAX_DEDUCTION,
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
