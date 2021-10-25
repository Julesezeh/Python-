'''
CREDIT CARD VALIDATOR BY OKOYE-EZEH JULES
'''

#This code, uses the required constraints, to detect if a number or numbers entered as inputs are valid credit cards
#so you'll be handling 'N' credit cards. Verify whether the credit card numbers are valid or not.
#A valid credit card must have the following characteristics:
#1.It must start with a 4,5 or a 6.
#2.It must contain exactly 16 digits, either together or separated by  hyphens,'-'.
#3.It must also only consist of digits  0-9.
#4.It must not have four or more consecutive repeated digits.

#import the necessary modules
import re




#handle the inputs
N=int(input("How many numbers are you checking  > "))
inputs = [input() for x in range(N)]

#define a function to check for repeating consecutive digits
def consec(xx):
    new=''.join(xx.split('-'))
    if len(new)==16:
        for x in range(len(new)-3):
            if new[x] == new[x+1] and new[x] == new[x+2] and new[x] == new[x+3]:
                return False
        return True
#define a function to handle the starting syntax
def order(xx):
    mike= None
    pattern1 = re.compile(r"[4-6][0-9]{15}")
    pattern2 = re.compile(r"[4-6][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}")
    if type(pattern1.match(xx) or pattern2.match(xx)) == type(mike):
        return False
    else:
        return True

for items in inputs:
    if (consec(items) and order(items)) == True:
        print("Valid")
    else:
        print("Invalid")