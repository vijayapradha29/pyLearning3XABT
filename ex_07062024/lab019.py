# string
# string is abunch of characters
# it can be used in three forms as ''."",""""""
# """"""-used for long strings
name = 'hi'
print(name)
name = "vijaya"
print(name)
name = """vijaya is a gud girl,she loves to listen to music
she is soft in nature
hfvhfbfkhbfjkf"""
print(name)

# difference between single and double quotes,both are same
# unless

# dir= "c:\nomedir\some dir"
# if use both single and double quotes also,output will be same because computer thinks \n as new line and breaks the string to next line
# to avoid this we use raw(r) string
dir = r'c:\nomedir\some dir'
# this is the way to provide directory path in python
print(dir)

# format of the string
first_name = "vijaya"
second_name = "pradha"
print(first_name, second_name)
print(first_name + "" + second_name)
print(first_name, "", second_name)
print(f'Your Full Name is {first_name} {second_name}')
#f->is used for formatting-it will replace values of the variables
#{}->placeholders


