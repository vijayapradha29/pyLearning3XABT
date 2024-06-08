#Take the 2 numbers from the userand we want to add them
num1=input("Enter the first number:")
num2=input("Enter the second number:")
result=num1+num2
print(result)

#input function reads string from standard input
#we need to do type conversion,convert str to int
number1=int(input("Enter the first Number:"))
number2=int(input("Enter the second number:"))
result=number1+number2
print(result)
#or
number1=input("Enter the first number:")
number2=input("Enter the second number:")
result=int(number1)+int(number2)
print(result)

#in python strings will concatenate with each other but they wont sum
#but if 2 and 3 comes,they will sum and becomes 5
# +-> comes in intger it sums(do add operation)
# +-> comes in string it does concatenation
#if we want to convert any integer to string,then we should use str()
#if we want to convert string to interger,then we use int()
print(type(int(number1)))