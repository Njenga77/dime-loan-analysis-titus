# LOAN REPAYMENT CALCULATOR
# Author: Titus Njenga
# Date: [Insert Date]
# Purpose: Calculate monthly loan repayments, total interest, and generate a repayment schedule.

import pandas as pd
from datetime import datetime

# ====== LOAN CALCULATION FUNCTIONS ======
def calculate_monthly_payment(principal, annual_rate, months):
    """
    Calculate monthly payment using the loan amortization formula.
    Formula: PMT = P * (r*(1+r)^n) / ((1+r)^n - 1)
    """
    monthly_rate = annual_rate / 12 / 100  # Convert annual % to monthly decimal
    payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return round(payment, 2)

def generate_repayment_schedule(principal, annual_rate, months):
    """
    Generate a month-by-month repayment schedule.
    Returns a DataFrame with payment details.
    """
    monthly_rate = annual_rate / 12 / 100
    payment = calculate_monthly_payment(principal, annual_rate, months)
    balance = principal
    schedule = []

    for month in range(1, months + 1):
        interest = balance * monthly_rate
        principal_payment = payment - interest
        balance -= principal_payment
        schedule.append({
            "Month": month,
            "Payment": payment,
            "Principal": round(principal_payment, 2),
            "Interest": round(interest, 2),
            "Remaining Balance": round(abs(balance), 2)
        })

    return pd.DataFrame(schedule)

# ====== USER INPUT & OUTPUT ======
def main():
    print("\n=== LOAN REPAYMENT CALCULATOR ===")
    
    # Get user input
    principal = float(input("Enter loan amount (KES): "))
    annual_rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter loan term (years): "))
    months = years * 12

    # Calculate repayment details
    monthly_payment = calculate_monthly_payment(principal, annual_rate, months)
    total_payment = monthly_payment * months
    total_interest = total_payment - principal

    # Generate schedule
    schedule = generate_repayment_schedule(principal, annual_rate, months)
    
    # Save results to CSV
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"loan_schedule_{timestamp}.csv"
    schedule.to_csv(filename, index=False)

    # Print summary
    print("\n=== RESULTS ===")
    print(f"Monthly Payment: KES {monthly_payment}")
    print(f"Total Interest: KES {round(total_interest, 2)}")
    print(f"Repayment schedule saved to: {filename}\n")

if __name__ == "__main__":
    main()
