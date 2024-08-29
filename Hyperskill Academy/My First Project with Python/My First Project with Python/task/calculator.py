item_names = ["Bubblegum",
              "Toffee",
              "Ice cream",
              "Milk chocolate",
              "Doughnut",
              "Pancake"]

earned_amount_per_item = [202,
                          118,
                          2250,
                          1680,
                          1075,
                          80]

income = 0.0
print("Earned amount:")
for i in range(0, len(item_names)):
    print(item_names[i] + ":", "$" + str(earned_amount_per_item[i]))
    income += earned_amount_per_item[i]

print("\nIncome: &" + str(income))

staff_expenses = int(input("Staff expenses:\n"))

other_expenses = int(input("Other expenses:\n"))
print("Net income: $" + str(income - staff_expenses - other_expenses))