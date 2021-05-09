import math
while True:
    try:
        num1 = float(input("Enter your first number (This will be the nuber that will be squared or square rootted): "))
        break;
    except ValueError:
        print ("Dat aint a number you idiot")
while True:
    try:
        num2 = float(input("Enter your second number: "))
        break;
    except ValueError:
        print ("Dat aint a number you idiot")
while True:
    try:
        oper = int(input("What is your operator:\n 1.division \n 2.multiplication \n 3.addition \n 4.subtraction\n 5.square\n 6.square root\n 7. Other exponentiation\n"))
        break;
    except ValueError:
        print ("Dat aint a number you idiot")
if oper == 1:
    print (num1 / num2)
elif oper == 2:
    print (num1 * num2)
elif oper == 3:
    print (num1 + num2)
elif oper == 4:
    print (num1 - num2)
elif oper == 5:
    print (num1 ** 2)
elif oper == 6:
    print (math.sqrt(num1))
elif oper == 7:
    print (num1 ** num2)