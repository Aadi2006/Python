# This is a 8ball program. Made by Aadi Jain on the date 9.9.20
#A virtular representation of an 8ball in python

                          # Yes replies
#   As I see it, Yes. : Yes: definately : you may rely on it:without a doubt: signs point to yes: outlook yes
# Outlook good:Most likely:it is decidely so: it is certain:
                          #No replies
#Don't count on it: my reply is no:My sources say no:outlook not so good:very doubtful:No:
                          #Neutral replies
#Better not tell you know: Ask again later:Cannot predict now:Concentrate and ask again:reply hazy try again

import random
from time import sleep
def answer():
    c = 1
    while True:
        noagain = random.randint(0,2)
        for u in range(5):
            print("Shuffle...")
            sleep(0.5)
        if noagain == 0:
            yesrepsa = ['As I see it, Yes', 'Yes','Definately','You may rely on it','without a doubt','signs point to yes','outlook yes','outlook good','Most likely','is is decidely so','it is certain']
            no2again = random.randint(0,10)
            print(yesrepsa[no2again].capitalize())
            sleep(1)
            print(f"There's your answer to the question - '{inp}'")
            break
        elif noagain == 1:
            norepsa = ["Don't count on it","My reply is no","My sources say no","Outlook not so good","very doubtful","No"]
            nono2a = random.randint(0,5)
            print(norepsa[nono2a].capitalize())
            sleep(1)
            print(f"There's your answer to the question - '{inp}'")
            break
        elif noagain == 2:
            newrepsa = ["Better not tell you now","Ask again later","Cannot predict now","Concentrate and ask again","Reply hazy, Try again later"]
            nono3again = random.randint(0,4)
            print(f"The magic 8 ball says - {newrepsa[nono3again].capitalize()}")
            if c == 0: print("Gawd that must be dissapionting")
            sleep(0.5)
            print(f"Do you try asking the question '{inp}' again")
            sleep(0.5)
            inp2 = input('Enter enter for yes')
            sleep(1)
            if len(inp2) != 0: break
            else:
                c = c + 1
                if c == 2: print('Its in a bad mood')
                elif c == 3:print("Wow, that's really bad")
                elif c == 4:
                    print("It's broken, time for you to leave")
                    break
                    quit()
                continue
        else:
            print("Something's wrong")
            sleep(1)
            quit()
        sleep(0.5)
print('Welcome to the Magic 8ball program!\n.\n.')
sleep(1)
print('Please write your question and the program will tell you what the 8ball thinks!\n.\n.\n.')
sleep(1)
while True:
    #Getting the input and other stuff
    inp = input('Enter your question : ')
    inp = inp.strip()
    if len(inp.split()) == 1:
        sleep(0.5)
        print('Kindly elaborate on the question\n.\n.')
        sleep(1)
        inp = input('Enter your question again:\n.\n. ')
    if len(inp) == 0:
        print('You have to write a question\n.\n.')
        quit()
    if 'please' in inp.lower().split() and len(inp.split()) == 2:
        print('Elaborate a bit more on your question\n.\n.')
        sleep(0.5)
        inp = input('Enter your question again:\n.\n. ')
#if 'slap' in inp.lower().split():

    if len(inp) > 50:
        print(f'You just had to write a question..........not something of {len(inp)} words\n.\n.')
    sleep(0.3)
    print('Thinking......')
    sleep(1.5)
#                         Got the input and done the other stuff of input
#Getting the answer
    no1 = random.randint(0,2)
    if no1 == 0:
        no2 = random.randint(0,10)
        yesreps = ['As I see it, Yes', 'Yes','Definately','You may rely on it','without a doubt','signs point to yes','outlook yes','outlook good','Most likely','is is decidely so','it is certain']
        print(yesreps[no2].capitalize())
    elif no1 == 1:
        noreps = ["Don't count on it","My reply is no","My sources say no","Outlook not so good","very doubtful","No"]
        nono2 = random.randint(0,5)
        print(noreps[nono2].capitalize())
    elif no1 == 2:
        newreps = ["Better not tell you now","Ask again later","Cannot predict now","Concentrate and ask again","Reply hazy, Try again later"]
        nono3 = random.randint(0,4)
        print(newreps[nono3].capitalize())
        sleep(2.3)
        print("Do you want to ask the Magic 8 ball the question - \'",inp,"\'again?")
        sleep(0.5)
        yesno = input("Hit Enter if yes, type anything if no")
        sleep(0.5)
        if len(yesno) == 0:
            print('You have chosen to ask another question')
            sleep(0.5)
            answer()
        else:
            print('You have chosen not to ask the question - ',inp,"again")
            sleep(0.5)
    else:
        print('Somethings wrong..............Try again later')
        print('Thank you and goodbye')
#Got the answer and printed it
    sleep(2)
#Going to the top and asking another question
    aq = input(f'Do you want to ask a question again? Press enter if yes, type anything if No\n')
    if len(aq) == 0:
        print('You have chosen to ask another question')
        sleep(1)
        continue
    else:
        print('You have had enough of the Magic 8 ball')
        break
        sleep(0.5)
print('Thank you for playing')
sleep(2)
quit()
