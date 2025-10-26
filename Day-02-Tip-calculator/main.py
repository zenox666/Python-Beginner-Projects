print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip = bill * tip/100
each_should_pay = (bill+tip)/people
bill_per = round(each_should_pay,2)
print(f"Each person should pay: {bill_per}")
