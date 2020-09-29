import re
from time import sleep
def s(slep): sleep(slep)
print('Hello, I am a bot. Please Enter your name')
name = input('What is your name? ').strip().capitalize()
s(0.5)
if len(name.split()) == 2:   name = name.split()[0]
howareyou = input(f'Hi {name}, How are you?\n>').lower().strip()
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
            print('That\'s not good')
            f = True
            break
        elif re.search(grep,howareyou):
            print('That\'s good')
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
print('Thank you and goodbye')
quit()
