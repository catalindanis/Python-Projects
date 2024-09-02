import argparse
from math import log, ceil

def calculate_number_of_monthly_payments(annuity_payment, loan_principal, interest_rate):
    interest_rate = interest_rate / (12 * 100)
    number_of_months =  int(ceil(log(annuity_payment / (annuity_payment - interest_rate * loan_principal)
                                , 1+interest_rate)))
    return [str.format("{} month" if number_of_months == 1 else "{} months", number_of_months) \
        if number_of_months <= 11 else (
            str.format("{} " + ("year" if number_of_months // 12 == 1 else "years"), number_of_months // 12) +
            ("" if number_of_months == 12 else
            str.format(" and {} " + ("month" if number_of_months % 12 == 1 else "months"), number_of_months % 12)
            )), number_of_months]

def calculate_monthly_payment(loan_principal, number_of_payments, interest_rate):
    interest_rate = interest_rate / (12 * 100)
    return ceil( loan_principal * ( (interest_rate * ((1 + interest_rate) ** number_of_payments)) /
                              (((1 + interest_rate) ** number_of_payments) - 1) ))

def calculate_loan_principal(annuity_payment, number_of_payments, interest_rate):
    interest_rate = interest_rate / (12 * 100)
    return int( annuity_payment / ( (interest_rate * ((1 + interest_rate) ** number_of_payments)) /
                                        (((1 + interest_rate) ** number_of_payments) - 1) ) )

def run_annuity():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", default=-1)
    parser.add_argument("--payment", default=float('inf'))
    parser.add_argument("--principal", default=float('inf'))
    parser.add_argument("--periods", default=float('inf'))
    parser.add_argument("--interest", default=float('inf'))

    args = parser.parse_args()

    annuity_payment = float(args.payment)  # A
    loan_principal = float(args.principal)  # P
    number_of_payments = float(args.periods)  # n
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
        annuity_payment < 0 or
        loan_principal < 0 or
        number_of_payments < 0 or
        interest_rate < 0 or
        interest_rate == float('inf')):
        print("Incorrect parameters")
        return

    if annuity_payment == float('inf'):
        annuity_payment = calculate_monthly_payment(loan_principal, number_of_payments, interest_rate)
        print("Your monthly payment = " + str(annuity_payment) + "!")
    elif number_of_payments == float('inf'):
        values = calculate_number_of_monthly_payments(annuity_payment, loan_principal, interest_rate)
        number_of_payments = values[1]
        print("It will take " + values[0])
    else:
        loan_principal = calculate_loan_principal(annuity_payment, number_of_payments, interest_rate)
        print("Your loan principal = " + str(loan_principal)  + "!")

    print()
    print("Overpayment = " + str(int(number_of_payments * annuity_payment - loan_principal)))



