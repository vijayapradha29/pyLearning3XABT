#ternary operator
vijaya_marks=90
pradha_marks=97
#x>y ->do something->print("vijaya"
#x<y->do something else->print("pradha")
print("vijaya is winner" if vijaya_marks > pradha_marks else "pradha is winner")#single line if else condition
#or
if vijaya_marks>pradha_marks:
    print("vijaya is winner")
else:
    print("pradha is winner")