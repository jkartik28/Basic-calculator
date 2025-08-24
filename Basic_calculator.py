print("1 : Multiplication")
print("2 : Addition")
print("3 : Subtraction")
print("4 : Division")

num = int(input("Select an option(1-4) : "))

num1 = int(input("Enter a First number : "))
num2 = int(input("Enter a Second number : "))

if num == 1  :
    sum1 = num1 * num2
    print("Multiplication of",num1,"or",num2,"=",sum1)
    
elif num == 2  :
    sum2 = num1 + num2
    print("Addition of",num1,"or",num2,"=",sum2)

elif num == 3  :
    sum3 = num1 - num2
    print("Subtraction of",num1,"or",num2,"=",sum3)
    
elif num == 4  :
    sum4 = (num1 / num2)
    print("Division of",num1,"or",num2,"=",sum4)
    
else :
    print("It is not valid number")