string=input("Enter the String:").lower()
#string1=print(len(string))
#print(len(string[0]))
#string=0
vowels=0
consonants=0
for i in string:
    if i=='a' or i=='e' or i=='i' or i=='o'or i=='u':
        vowels=vowels+1
    else:
        consonants=consonants+1
print("Vowels:",vowels)
print("Consonants:", consonants)