import re
import random
from time import sleep
def s(slep): sleep(slep)
#Asking for their name
print('Hello, I am a bot. Please Enter your name')
name = input('What is your name? ').strip().capitalize()
s(0.5)
if len(name.split()) == 2:   name = name.split()[0]
if len(name) == 2: name=name.upper()
#Asking for how the mood of the user
howareyou = input(f'Hi {name}, How are you doing?\n>').lower().strip()
s(1)
greps = ['good','great','happy','fabulous']
breps = ['bad','not good','unhappy','sad','depressed']
f = False
if re.search('better than you',howareyou):
    print(f"Hahaha, in your dreams")
    f = True
if f is False:
    for grep in greps:
        if re.search(f'not.*{grep}',howareyou):
            print('That\'s bad. Hope you have a fabolous day after this!')
            f = True
            break
        elif re.search(grep,howareyou):
            print('Thats whopping!')
            f = True
            break
        else:
            f = False
            continue
if f is False:
    for brep in breps:
        if re.search(f'not.*{brep}',howareyou):
            f = True
            print("That's great!")
            break
        elif re.search(brep,howareyou):
            print('That\'s not good')
            f = True
            break
        else:
            f = False
            continue
if f is False:
    print('I did not understand')
s(0.5)
#Asking for hobbies, if any
question_for_hobs_randrange = random.randint(1,3)
if question_for_hobs_randrange == 1:
    hobs = input(f"So, {name}.\nWhat are your hobbies?")
elif question_for_hobs_randrange == 2:
    hobs = input("What do you do in your free time mate?")
elif question_for_hobs_randrange == 3:
    hobs = input("What is you favorite pastime?")
hobs=hobs.lower()
stop_asking = False
if re.search("nothing much+",hobs):
    print("You must be doing something worth mentioning")
    RandomNumberForNothingMuch = random.randint(0,1)
    sleep(0.5)
    if(RandomNumberForNothingMuch == 1):
        print("Unlike me :)")
        sleep(0.5)
    print("Really, okay, no prob")
    stop_asking = True
if stop_asking == False:
    if re.search("don't|no|not",hobs) == None:
        if re.search('guitar|read|box|jam|code|coding',hobs):print("Really!, me too")
        else:print('That great!\nThough I personally like to do play the guitar, read, box and code("This program was made by me")')
    else:
        if(re.search('guitar|read|box',hobs)):
            print("That's a pity, as I personally like to do that")
        else:
            print("That's like a pizza, great")
if re.search('read',hobs):
    print("Please recommend me a few books, so that I come to know more books to read!")
    sleep(1)
    print("BTW press enter to stop")
    count = 1
    while True:
        book_question = input(f"Book{count}: ")
        if len(book_question)==0:
            break
        c+=1
    print("Thanks for your help")
print('Thank you and goodbye')
quit()
