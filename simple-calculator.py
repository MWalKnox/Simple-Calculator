"""The objective of this simple calculator is to
    request two numbers from the user and calculate
    them based on the user's input.
"""

"""I used the float command here to more easily
    work with decimals.
"""
numA = float(input("Enter the First Number: "))
action = input("What arithmatic method are we using today +, -, *, or / ? ")
numB = float(input("Enter the Second Number: "))

if action == "+":
    print(numA + numB)
elif action == "-":
    print(numA - numB)
elif action == "*":
    print(numA * numB)
elif action == "/":
    if numB != 0:
        print(numA / numB)
else:
    print("Oops! Something went wrong!")

"""This small and simple program can add, subtract,
    multiply, or divide whole numbers or decimals.
"""
