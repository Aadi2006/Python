#program about my classes
monclass = ('Math', 'English', 'Geography', 'Music')
tueclass = ('English', 'Physics', 'Math', 'Art')
wedclass = ('Spanish', 'CST', 'Chemsitry', 'Rockschool mus')
thuclass = ('English', 'Physics', 'History', 'Art')
friclass = ('Hindi', 'Biology', 'Math', 'PE')
satclass = ('Biology', 'Hindi', 'Chemsitry', 'Lifeskills')
classdict = {'Math':'ABT', 'English':'JKA', 'Geography':'ARD', 'Music':'ARK', 'Physics':'RMB', 'Art':'MRD', 'Chemistry':'RKM','CST':'HGT', 'History':'PMV', 'Hindi':'MHF', 'PE':'NTC', 'Biology':'CRK', 'Lifeskills':'UNP'}
sunclass = 'HOOOOOOOLLLLLLLLLIIIIIDDDDDDDDDDAAAAAAAAAAAYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
per = [monclass, tueclass, wedclass, thuclass, friclass, satclass]
allthedays = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','PERIOD']
day = input('This is your timetable,\n please enter what day it is.(Without caps). Or maybe you can write the initials of your teacher and get some info about that. Or if you want to sort them by period please wright period \n>>> ')
if day.upper() not in classdict.values() and not allthedays:
    print('Looks like you havent entered something right. Please try again.')
    exit()
if len(day) < 1:
    print('Please enter something')
    exit()

if day == 'period' :
    whatp = input('Which period do You want to see.The first letter should be capital \n>>> ')
    theteacher = classdict[whatp]
    def peri() :
        if thefinalclass == monclass :
            thetoday = 'Monday'
        if thefinalclass == tueclass :
            thetoday = 'Tuesday'
        if thefinalclass == wedclass :
            thetoday = 'Wednesday'
        if thefinalclass == thuclass :
            thetoday = 'Thursday'
        if thefinalclass == friclass :
            thetoday = 'Friday'
        if thefinalclass == satclass :
            thetoday = 'Saturday'
        if fog == 0:
            thetiming = '10:00 a.m.'
        if fog == 1:
            thetiming = '10:50 a.m.'
        if fog == 2:
            thetiming = '12:00 p.m.'
        if fog == 3:
            thetiming = '3:00 p.m.'
        print('You have the class', whatp,'on',thetoday,'at the time',thetiming,'with the teacher',theteacher)
    if whatp in monclass :
        thefinalclass = monclass
        fog = monclass.index(whatp)
        peri()
    if whatp in tueclass :
        thefinalclass = tueclass
        fog = tueclass.index(whatp)
        peri()
    if whatp in wedclass :
        thefinalclass = wedclass
        fog = wedclass.index(whatp)
        peri()
    if whatp in thuclass :
        thefinalclass = thuclass
        fog = thuclass.index(whatp)
        peri()
    if whatp in friclass :
        thefinalclass = friclass
        fog = friclass.index(whatp)
        peri()
    if whatp in satclass :
        thefinalclass = satclass
        fog = satclass.index(whatp)
        peri()
    quit()
all_of_my_class_days = ['monday', 'tuesday', 'thursday', 'friday', 'saturday']
if day.lower() in all_of_my_class_days:
    print('it is ', day)
    print('You have 4 schools today')
    print('First school starts at 10:00am')
    print('Second school starts at 10:50am')
    print('Third school starts at 12:00')
    print('And your last class is at 3pm')

if day.lower() == 'monday' :
    myclass = monclass
elif day.lower() == 'tuesday' :
    myclass = tueclass
elif day.lower() == 'wednesday' :
        myclass = wedclass
        print('You have 4 schools today')
        print('First school starts at 10:00am')
        print('Second school starts at 10:50am')
        print('Third school starts at 12:00')
        print('The last school is at 9 pm')
elif day.lower() == 'thursday' :
    myclass = thuclass
elif day.lower() == 'friday' :
    myclass = friclass
elif day.lower() == 'saturday' :
    myclass = satclass
elif day.lower() == 'sunday' :
    print(sunclass)
def myvar() :
    period = input('Enter 1 for the first class, 2 for the second class and so on \n>>> ')
    period = int(period)
    period = period - 1
    theclass = myclass[period]
    if theclass in classdict :
        classt = classdict[theclass]
        print('The current class is', theclass,'with teacher', classt)
        quit()
if day.lower() == 'monday' :
    myclass = monclass
    myvar()
elif day.lower() == 'tuesday' :
    myclass = tueclass
    myvar()
elif day.lower() == 'wednesday' :
    myclass = wedclass
    myvar()
elif day.lower() == 'thursday' :
    myclass = thuclass
    myvar()
elif day.lower() == 'friday' :
    myclass = friclass
    myvar()
elif day.lower() == 'saturday' :
    myclass = satclass
    myvar()
for k,v in classdict.items() :
    if day.upper() == v :
        print(v, 'is your', k,' teacher')
        break

def time() :
    periodical = finalclass[fd]
    if finalclass == monclass :
        today = 'Monday'
    if finalclass == tueclass :
        today = 'Tuesday'
    if finalclass == wedclass :
        today = 'Wednesday'
    if finalclass == thuclass :
        today = 'Thursday'
    if finalclass == friclass :
        today = 'Friday'
    if finalclass == satclass :
        today = 'Saturday'
    if fd == 0:
        timing = '10:00 a.m.'
    if fd == 1:
        timing = '10:50 a.m.'
    if fd == 2:
        timing = '12:00 p.m.'
    if fd == 3:
        timing = '3:00 p.m.'
    print('You have a class with', v,'on ',today,'at the timing', timing)


if k in monclass :
    finalclass = monclass
    fd = monclass.index(k)
    time()
if k in tueclass :
    finalclass = tueclass
    fd = tueclass.index(k)
    time()
if k in wedclass :
    finalclass = wedclass
    fd = wedclass.index(k)
    time()
if k in thuclass :
    finalclass = thuclass
    fd = thuclass.index(k)
    time()
if k in friclass :
    finalclass = friclass
    fd = friclass.index(k)
    time()
if k in satclass :
    finalclass = satclass
    fd = satclass.index(k)
    time()

print('All done!')
