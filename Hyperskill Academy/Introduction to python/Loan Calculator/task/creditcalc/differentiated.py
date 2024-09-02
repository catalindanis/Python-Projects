import argparse
from math import ceil

def calculate_differentiated_payments(loan_principal, interest_rate, number_of_payments):
    interest_rate = interest_rate / (12 * 100)
    total_payment = 0
    for m in range(1, number_of_payments+1):
        payment_value = ceil(loan_principal / number_of_payments + interest_rate * (loan_principal - (loan_principal * (m-1)) / number_of_payments))
        total_payment += payment_value
        print("Month " + str(m) + ": payment is " + str(payment_value))
    return total_payment

def run_differentiated():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", default=-1)
    parser.add_argument("--payment", default=float('inf'))
    parser.add_argument("--principal", default=float('inf'))
    parser.add_argument("--periods", default=float('inf'))
    parser.add_argument("--interest", default=float('inf'))

    args = parser.parse_args()

    annuity_payment = float(args.payment)  # A
    loan_principal = float(args.principal)  # P
    number_of_payments = int(args.periods)  # n
    interest_rate = float(args.interest)  # i

    number_of_parameters_provided = 0
    if annuity_payment != float('inf'):
        number_of_parameters_provided += 1
    if loan_principal != float('inf'):
        number_of_parameters_provided += 1
    if number_of_payments != float('inf'):
        number_of_parameters_provided += 1
    if interest_rate != float('inf'):
        number_of_parameters_provided += 1

    if (number_of_parameters_provided != 3 or
        annuity_payment != float('inf') or
        interest_rate < 0 or
        annuity_payment < 0 or
        loan_principal < 0 or
        number_of_payments < 0):
        print("Incorrect parameters")
        return

    total_payment = calculate_differentiated_payments(loan_principal, interest_rate, number_of_payments)

    print()
    print("Overpayment = " + str(int(total_payment - loan_principal)))