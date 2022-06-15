#total = 0
#count = 0
#while True :
#    inp = input('You number for finding the average of a number')
 #   if inp == 'done': break
  #  val = float(inp)
  #  total = total + val
  #  count = count + 1
#av = total / count
#print(av)

#Program about couting letters, words and stuff like that.
name = input('Hello I am Aadi, this program asks you to write a couple of words and then will print out the number of word you say \n What is you name? : \n')
print('Hello' ,name,)
hh = input('How are you? \n >>')
grep = ['good', 'fine', 'not bad', 'eh', 'great', 'excellent','awesome', 'happy','cool','ecstatic']
brep = ['bad', 'not good', 'sad', 'depressed', 'unhappy','Okay']
hh = hh.strip().lower()
if hh in grep :
    print("That's jolly good", name)
elif hh in brep :
    print(' That"s Not good, but lets continue')
elif hh == 'better than you':
    print('Too bad')
else :
    print('I did not understand what you meant by this')
start = input('Anyways enter your sentence \n >')
if len(start) < 1:
    start = 'Hello, my name is aadi. How are you. This sentence is a tester and is there only for testring stuff and for testing a bit more stuff if I im in the mood. Please enter enter to enter'
peices = start.split()
counts = dict()
for rel in start:
    sp = rel.split()
    for word in sp:
        counts[word] = counts.get(word,0) + 1
#bigcount = None
#bigword = None
#for word,counting in counts.items() :
#    if bigcount is None or counting > bigcount :
 #       bigcount = word
  #      bigword = counting
#print(bigword, bigcount)
print('This is your sentence \n', peices)
lee = len(peices)
kew = len(start)
print('There are', lee,'words in the sentence written by you and there are', kew,'letters')
x = input('enter the number of the word you want to examin. for ex. 1 for the first word, 2 for the second word and so on. \n')
z = int(x)
z = z - 1
qw = peices[z]
print('This is the word selected by you - ', qw)
le = len(qw)
print('There are', le,'letters in this word')
print('Now you need to enter a letter and the program will tell you how many times that specific letter has been used in your sentence')
let = input('Enter you letter \n')
apeice = start.split(let)
counter = 1
for ter in apeice :
    print('your letter along with the count.', counter, '.', ter)
    counter = counter + 1
counter = counter - 1
print('Your letter has been repeated', counter,'times along the statement')
print('Now maybe you want to do the same thing with a specific word')
ops = input('Enter your number')
ops = int(ops)
ops = ops - 1
nume = peices[ops]
print('You have selected this word.', nume)
letter = input('Enter the letter you want to see: ')
print("You have selected the string : ", nume, "\n and looking for : ", letter)
res = None
for i in range(0, len(nume)):
    if nume[i] == letter:
        res = i + 1
        break
if res == None:
    print("No such charater is available in the string")
else:
    print("Character {} is present at {} position".format(letter, str(res)))
print('Thank you & goodbye!!')
