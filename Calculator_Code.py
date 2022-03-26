def add(x, y):
    return x + y


def subtract(x, y):
    return x - y

#If want to add multiplication and/or division, write same code but change x + y or x - y to x * y or x / y and the variable add or subtract to multiply or divide

print("Select Operation.")
print("1.Add")
print("2.Subtract")

#If to add multiplication and division, add a option for them.

choice = input("Enter choice(1/2): ") #add 3/4 to input choice if multiplication and/or division involved.

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
    
#Add own section as line 24-25 above for division or multiplication but change the sign between num1 and num2.

else:
    print("Invalid Input")
    
