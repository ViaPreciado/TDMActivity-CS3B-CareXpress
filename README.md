# Salary Calculator

## Overview
This Python program calculates salary deductions, including SSS, PhilHealth, Pag-IBIG, and tax deductions. The net salary is computed by subtracting the total deductions from the gross salary.

## Features
- Computes salary deductions (SSS, PhilHealth, Pag-IBIG, Tax)
- Structured output displaying a salary breakdown
- Modular functions for maintainability
- Object-Oriented Programming (OOP) structure for better code management
- Input validation and error handling
- Test script for automated testing

---

## **Commit History & Changes**

### **1. Base Code - Initial Implementation**
**Commit: [Initial Version]**
- Basic function to compute deductions
- Hardcoded values for SSS, PhilHealth, Pag-IBIG, and tax
- Directly prints salary breakdown
- No input validation or error handling

### **2. Improve Code Readability - PRECIADO**
**Changes:**
- Replaced hardcoded calculations with descriptive constants
- Improved function naming for clarity
- Introduced a dictionary to return salary details instead of printing directly
- Added `display_salary_details()` function for structured output
- Introduced basic input validation

### **3. Converted to Modular Functions - SEDORIOSA**
**Changes:**
- Broke down deductions into separate functions: `calculate_sss_deduction()`, `calculate_philhealth_deduction()`, `calculate_pagibig_deduction()`, `calculate_tax_deduction()`
- Introduced `calculate_total_deductions()` and `calculate_net_salary()` for better modularity
- Improved maintainability by reducing redundancy
- Simplified calculations by reusing modular functions

### **4. Implemented with OOP Structure - ZARATE**
**Changes:**
- Refactored the program into a class-based approach (`SalaryCalculator`)
- Encapsulated attributes and methods to improve code maintainability
- Made the program more scalable and extensible for future modifications

### **5. Added Input Validation, Error Handling, & Test Script - KHAN**
**Changes:**
- Added error handling for invalid and negative salary inputs
- Implemented a `get_valid_salary()` function to handle incorrect inputs
- Ensured `SalaryCalculator` raises errors for non-numeric and negative inputs
- Created a test script (`test_salary_calculator.py`) to validate computations
- Used `unittest` to ensure all functions work as expected

---

## **Technical Debt Identified**

1. **Lack of Input Validation (Fixed in KHAN's Commit)**
   - Early versions lacked input validation, which could cause crashes.

2. **Hardcoded Deduction Values (Fixed in Modularization by SEDORIOSA)**
   - Earlier versions used fixed values within calculations instead of separate functions.

3. **Code Duplication (Refactored in Modular Functions & OOP by SEDORIOSA & ZARATE)**
   - The same calculations were repeated across different sections of the code.

4. **Scalability Issues (Fixed in OOP by ZARATE)**
   - As more features get added, the non-OOP approach would have led to difficult maintenance.

5. **Lack of Automated Testing (Fixed in KHAN's Commit)**
   - Before unit tests were introduced, changes could break previous functionality.

6. **Poor Naming Conventions (Improved in PRECIADO's Commit)**
   - Early function names lacked clarity, making the code harder to read and maintain.
   - Improved by using more descriptive function and variable names.

---

## **Challenges Faced & Solutions**

| **Challenge** | **Solution** |
|--------------|-------------|
| Ensuring salary input is numeric | Implemented `get_valid_salary()` to repeatedly prompt the user until valid input is provided |
| Preventing code duplication | Introduced modular functions and later transitioned to an OOP structure |
| Handling different salary values (negative, high, zero) | Used exception handling and conditions to prevent incorrect inputs |
| Ensuring code correctness after multiple refactors | Introduced `unittest` to verify calculations and program output |
| Maintaining readability while optimizing for scalability | OOP refactoring allowed better maintainability and extensibility |

---

## **How to Run the Program**

### **Requirements**
Ensure you have **Python 3.7 or later** installed on your system.

### **Running the Program**
1. Save the script as `salary_calculator.py`.
2. Open a terminal or command prompt in the same directory as the script.
3. Run the program using:
   ```sh
   python salary_calculator.py
   ```
4. Enter your monthly salary when prompted.
5. View the salary breakdown in the console output.

---

## **Running the Test Script**

### **Steps to Run Tests**
1. Ensure `salary_calculator.py` is in the same directory.
2. Save the test script as `test_salary_calculator.py`.
3. Open a terminal or command prompt and navigate to the script directory.
4. Run the test using:
   ```sh
   python -m unittest test_salary_calculator.py
   ```
   or for detailed output:
   ```sh
   python -m unittest -v test_salary_calculator.py
   ```

### **Expected Output**
If all tests pass, you should see an output similar to:
```
test_display_salary_details (test_salary_calculator.TestSalaryCalculator) ... ok
test_extremely_high_salary (test_salary_calculator.TestSalaryCalculator) ... ok
test_negative_salary (test_salary_calculator.TestSalaryCalculator) ... ok
test_non_numeric_salary (test_salary_calculator.TestSalaryCalculator) ... ok
test_valid_salary (test_salary_calculator.TestSalaryCalculator) ... ok
test_zero_salary (test_salary_calculator.TestSalaryCalculator) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```

If a test fails, the error message will indicate which function needs fixing.

---
