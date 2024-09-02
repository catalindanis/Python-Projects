import argparse
from annuity import run_annuity
from differentiated import run_differentiated

parser = argparse.ArgumentParser()
parser.add_argument("--type", default=-1)
parser.add_argument("--payment", default=float('inf'))
parser.add_argument("--principal", default=float('inf'))
parser.add_argument("--periods", default=float('inf'))
parser.add_argument("--interest", default=float('inf'))

args = parser.parse_args()

if args.type == "annuity":
    run_annuity()
elif args.type == "diff":
    run_differentiated()
else:
    print("Incorrect parameters")