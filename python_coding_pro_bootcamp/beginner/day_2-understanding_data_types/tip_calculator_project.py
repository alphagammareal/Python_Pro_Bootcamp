print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
# my Calculation
new_bill = bill + bill * (tip/100)
Amount_each = round(new_bill/people, 2)
# print(Amount_each)
print(f"The total bill including tip is {new_bill} and therefore everyone will be paying {Amount_each}GHS")