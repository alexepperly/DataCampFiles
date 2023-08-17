#!/usr/bin/env python3

# Student Loan Interest Program Script
def calculate_daily_interest(principal, apr):
    daily_interest_rate = apr / 36500  # Convert APR to daily rate
    daily_interest_amount = principal * daily_interest_rate
    return daily_interest_amount

def main():
    principal_aa = float(input("Enter the principal for Loan AA: "))
    apr_aa = 6.21
    daily_interest_aa = calculate_daily_interest(principal_aa, apr_aa)
    print(f"Daily interest on Loan AA: ${daily_interest_aa:.2f}")

    principal_ac = float(input("Enter the principal for Loan AC: "))
    apr_ac = 5.84
    daily_interest_ac = calculate_daily_interest(principal_ac, apr_ac)
    print(f"Daily interest on Loan AC: ${daily_interest_ac:.2f}")

if __name__ == "__main__":
    main()
