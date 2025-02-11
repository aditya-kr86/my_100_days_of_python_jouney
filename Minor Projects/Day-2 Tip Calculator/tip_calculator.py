print("Welcome to thw tip calculator.")
bill_amount = float(input("What was the total bill? ₹"))
tip_percentage = int(input("What percentage tip whould you like to give? 10,12, or 15? "))
total_people = int(input("How many people to split the bill? "))
amnt_by_each_man = (bill_amount + (bill_amount * tip_percentage)/100) /total_people
print(f"Each person should pay : ₹{amnt_by_each_man:.2f}")
