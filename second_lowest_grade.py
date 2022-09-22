"""
BY OKOYE-EZEH JULES
"""
"""
Given the names and grades for each student in a 
class of 'N' students, store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, 
    order their names alphabetically and print each name on a new line.
"""

#import time for delayed outputs
import time

#handle the inputs
N=int(input("Number of students?> "))
students = [[input("Name>"), float(input("score"))] for x in range(N)]

#loopn through the students' nessted list and create a list of just the scores
#which will be handled to contain only unique values
y=[]
for x in students:
    y.append(x[1])
yy=list(set(y))
yy.sort()
yy.pop(-1)
time.sleep(3)
print("\n")
names = []
#Handle the names of the students with the second lowest score
#and print them out
for pp in students:
    if pp[1]==yy[-1]:
        names.append(pp[0])
names.sort()
for x in names:
    print(x)
    time.sleep(1)