#2.Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
num=2
square=num**2
cube=num**3
print("Square  value is:",square)
print("Cube value is:",cube)

#3.Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

num1=input("Enter the First Number:")
num2=input("Enter the Second Number:")
#print("First Number is greater than second Number" if num1>num2  else "second Number is greater than first number")
#print("First Number is less than Second Number" if num1<num2 else "Secone Number is less than first number")
#print("First Number is equal to Second Number")
if(num1>num2):
    print("Num1 is greater than Num2")
elif(num1<num2):
    print("Num1 is less than Num2")
else:
    print("Num1 is equal to Num2")