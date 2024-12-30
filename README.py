from unittest import result


print("1. Addition")    
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
option =int( input("Choose an option: "))
if(option in[1,2,3,4]):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if(option==1):
        print("The sum is: ", num1+num2)
    elif(option==2):
        print("The difference is: ", num1-num2)
    elif(option==3):
        print("The product is: ", num1*num2)
    elif(option==4):
        print("The quotient is: ", num1/num2)
else:
    print("Invalid option")
print("The result of the operation is{}".format(result))