a=int(input("Enter the first Number "))
b=int(input("Enter the second Number "))

print("Select the action you want to perform:\n" \
"1 for Addition\n" \
"2 for Substraction\n" \
"3 for Multiplication\n" \
"4 for Division")

c=int(input("Enter the number for action "))

if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    if b !=0:
        print(a/b)
    else:
        print("Cannot divide by 0")
else:
    print("The value entered is invalid")