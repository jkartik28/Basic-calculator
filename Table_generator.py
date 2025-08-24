# Write a table of given number

n = int(input("Enter a number : "))

print(f"Table of {n}")

for i in range (1,11) :
    print(n,"X",i,"=",n*i)