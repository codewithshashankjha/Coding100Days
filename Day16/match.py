x= int(input("Enter the Value of x:- "))

match x:
    case 0:
        print("The value is zero")

    case 3:
        print("The case is one")
    
    case _ if x <8:
        print("The Default value is ",x)
    case _ if x >=8 and x<=15:
            print("Is the Default value is ",x)
    case _:
            print("Default value is ",x)