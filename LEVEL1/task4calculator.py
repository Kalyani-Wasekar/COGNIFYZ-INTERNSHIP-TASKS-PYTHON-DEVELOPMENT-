print("CALCULATOR")
#Get the input from the user
n1=float(input("Enter first number="))
operator=input("Enter an operator you want(+,-,*,/,%):")
n2=float(input("Enter second number="))
#Do the operation based on user input and display the result
if(operator=="+"):
    print(n1+n2)
elif(operator=="-"):
    print(n1-n2)
elif(operator=="*"):
    print(n1*n2)
elif(operator=="/"):
    print(n1/n2)
elif(operator=="%"):
    print(n1%n2)
else:
    print("You choose an invalid operator...Please enter +,-,*,/ or %)")
        


        


