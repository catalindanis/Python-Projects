import random

try:
    number_of_people = int(input("Enter the number of friends joining (including you): "))
    if number_of_people <= 0:
        raise Exception
except Exception:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    people = {}
    for i in range(number_of_people):
        people[input()] = 0

    total_bill_value = int(input("Enter the total bill value:"))

    use_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if use_lucky != "Yes" :
        print("No one is going to be lucky")
        split_bill_value = round(total_bill_value / number_of_people, 2)
        for name in people:
            people[name] = split_bill_value
    else:
        lucky_name = random.choice(list(people.keys()))
        print(lucky_name + " is the lucky one!")
        split_bill_value = round(total_bill_value / (number_of_people-1), 2)
        for name in people:
            if name != lucky_name:
                people[name] = split_bill_value
    print(people)
