""" Python - Bro Code """

op = input("Enter a operator: (+, -, *, /): ")
number1 = float(input("\nEnter the 1st number: "))
number2 = float(input("Enter the 2st number: "))

if op == "+":
    print(round("\n", number1 + number2, 2))
elif op == "-":
    print(round("\n", number1 - number2, 2))
elif op == "*":
    print(round("\n", number1 * number2, 2))
elif op == "/":
    print(round("\n", number1 / number2, 2))
else:
    print(f"\nThe operation {op} is not valid.")