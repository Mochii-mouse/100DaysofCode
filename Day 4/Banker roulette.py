import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

people = len(names) - 1

choice = random.randint(0, people)

print(f"{names[choice]} is going to buy the meal today!")
