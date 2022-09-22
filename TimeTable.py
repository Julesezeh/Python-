import random
import datetime
DAYS=[' Monday ',' Tuesday ',' Wednesday ',' Thursday ',' Friday ',' Saturday ',' Sunday ']
COURSES=['J.Script','SQl','Python & Django','Pygame','HTML & CSS','RUBY']
creationdate = datetime.datetime(2021,10,6)
currentdate = datetime.datetime.now()
while True:
    pot = currentdate-creationdate
    if pot.days >= 7:
        random.shuffle(COURSES)
        print(f"{DAYS[0]}-- {COURSES[0]},{DAYS[1]}-- {COURSES[1]},{DAYS[2]}-- {COURSES[2]}, {DAYS[3]}-- {COURSES[3]},{DAYS[4]}-- {COURSES[4]} ,{DAYS[5]}-- {COURSES[5]},{DAYS[6]}-- {COURSES[random.randint(0,5)]}")
        ask=input("New stuff, let's get this shit? ")
        if ask.upper() == 'YES' or 'Y':
            break
        else:
            continue
    else:
        print(f"{DAYS[0]}-- {COURSES[0]},{DAYS[1]}-- {COURSES[1]},{DAYS[2]}-- {COURSES[2]}, {DAYS[3]}-- {COURSES[3]},{DAYS[4]}-- {COURSES[4]} ,{DAYS[5]}-- {COURSES[5]},{DAYS[6]}-- {COURSES[random.randint(0,5)]}")
        ask = input("Let's get this shit? ")
        if ask.upper() == "YES" or "Y":
            break
        else:
            continue