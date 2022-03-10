import math

argument_list = []

for number in range(100):
    argument_list.append(number/10)

formula = input("Enter your formula (ise x as the arg):")

for x in argument_list:
    print(eval(formula))
