#Whats your name
Po = input('Who are you?')
print('Hello', Po)
if Po == str('Aadi'):
    print('Welcome writer')
# convertind eup to usa floors
frog = input('Welcome to the elevator, Enter Europe floor and I will convert it to a USA floor for u')
try:
    YT = int(frog) + 1
    print('Usa floor - ' , YT)
    if YT > 1000 :
        print('You,ve gotta be kiddin me ', Po, 'I think what you need to be in is an airplane and not an elevator')
    else :
        print('Good job')
    print('I am done, catch ya later')
except:
    print('Sorry only digits can be entered')

# New greater than 50 code
print('Hello', Po,'this is a new program which says if your number is greater equal or smaller than 50.')
flop = input('Please enter your number here.')
try :
    floppy = float(flop)
    if floppy > 50 :
        print('Bigger than 50.')
        if floppy > 100 :
            print('Its also bigger than hundred')
            if floppy > 1000 :
                print('Wow', Po,'Thats a big number')
                if floppy > 10000 :
                    print('Woah. You just coudnt think of a bigger number could you.')
    if floppy == 369 :
        print('But Hey', Po,'Thats my number!!!')
    if floppy == 50 :
        print('Come on man, Dont tell me that You dont know that 50 is equal to 50.')
    if floppy < 50 :
        print('This is smaller than 50')
        if floppy < 25:
            print('Smaller than 25 tooooooooooooo')
            if floppy == 0 :
               print('Thats a zero, add a 5 to the left.')
except :
    print('Sorry only numbers allowed')
print('Thank you and Goodbye.')
