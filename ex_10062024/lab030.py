# operators
# assignment operator is single opeartor
# assignment operator(single equal too sign "=")
# assign the value from right to left
name = "vijaya"

# comparison or compaerator -denoted by ("==double equal too sign")
# it will always return a boolean value
v1 = (1 == True)
print(v1)
v2 = (2 == False)
print(v2)
v3=(0==False)#0 equals false,right so its true
print(v3)


#unary operator:
#1.Arithmetic operator
age=+65#->arithmetic operator,the output will not display +sign as it is self explanatory and removed
print(age)
num=-33#->here - sign needs to specifically typed
print(num)

r=age+num#(65+(-33))- sign is specifically considered,+automatically cancels and replaced by - sign,BODMAS is applied
print(r)


#Not operator-works only with booleans
#is_married=True
#print(is_married)
is_married=True
print(not is_married)#->not operator is used to reverse the boolean value

#Is operator->identity operator->it returns boolean value
#Is operator will be mostly used in list
a=1
b=3
c=False
print(a is b)

my_lists=[1,2,3]
my_lists2=[1,2,3]
print(my_lists is my_lists2)
#even though the elements are same but they are stored in different locations,so it returns false
#is operatot is mostly used in conditions
