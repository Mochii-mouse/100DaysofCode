print("Welcome to the tip calculator!")
bill = float(input("What is the bill total?\n£"))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people will be splitiing the bill?\n"))

tip = (bill / 100) * tip_percentage
total_bill = bill + tip
per_person = total_bill / people
total_per_person = round(per_person, 2)
final_amount = "{:.2f}".format(total_per_person)

print(f"Each person should pay £{final_amount}")
