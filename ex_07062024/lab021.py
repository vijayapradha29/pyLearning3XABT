#Strings
#Inbuilt Functions
#function->repeat a task-you can use a function
#set of statements,predefined code
#functions->print(),input(),type(),max(),min(),id(),format(),sum(),avg()->these are common functions

#Strings
name="vijaya"
print(name)
print(type(name))
#id is  a function
print(id(name))
#id->means it returns the identity of the object
#id->where it is stored memory address
#id->gives you memory address where it is stored
#id->some random numbers will be shown for id
#len is a function
print(len(name))
#len always starts from 1
#uppercase->returns a copy of the string converted to uppercase
name=name.upper()
print(name)
#lower case->string will be shown in lower case
#name=name.lower()
#print(name)
#count->counts the number of particular characters in the string
#if count character is small then mention in small letter
#if count character is capital letter then mention in capital
#name=name.count("a")
#print(name)
b=name.count("V")
print(b)
#takes value from the last converted ones

#vijaya is stored in a representation as index no.0,index no.1,index no.2,index no.3,index no.4,index no.5
#index no.0->v
#index no.1->i
#index no.2->j
#index no.3->a
#index no.4->y
#index no.5->a
#it is stored in the form of arrays,stored continuously in the memory
#index starts from 0

#index
print(name[1])
#print(name[6])-index value for the above string is 0 to 5 only
#so for 6 it throws the error message as string index out of range

#python->index are immutable in nature meaning it cant be changed
#name[0]= "z"#->str operator does not support item assignment
#once the location is allocated for a string,it cannot change the same memory for another charcater

