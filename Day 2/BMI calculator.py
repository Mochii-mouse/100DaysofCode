height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

weightsq = float(height) ** 2
bmi = float(weight) / weightsq

print(int(bmi))
