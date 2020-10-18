#Normal stuff
x = 5
while x < 100 :
    print(x)
    x = x + 1
print('Hji')

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('e')

oo = ['ko', 'mo', 'o']
for ho in oo :
    print('Yoohoo', ho)
print('Hello ;lkasdhg;lsahjfgo;sjgoswj')

dud = 0
you = 0
for bub in[325464,566436778637, 6876876, 4755757877, 7 ,0.0000000000000001] :
    you = you + 1
    dud = dud + bub
    print('count', you, bub, dud, dud / bub)

jop = 'dudbudhud'
poj = jop[5]
print(poj)
gogo = 36
ogog = jop[gogo - 32]
print(ogog)
opop = len(jop)
print(opop)
type(opop)

fruit = 'aadiaadiadadialfajsfdjj'
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index ,letter)
    index = index + 1

tt = 'fofoadsfodsfosdaojasdl;fjasdl;uklroadljsfsalrkloksfdio;'
vov = 0
for ffff in tt :
    if ffff =='f' :
        vov = vov + 1
    print(vov, tt)

xfile = open('yo.py')
for abb in xfile :
    print(abb)
yocount = 0
theko = 0
for aaaa in abb:
    theko = theko + 1
print('Has these many lines :', theko)
new = xfile.read()
j = len(new)
print(j)
print('Has these many lines :', theko)

dokk = ['asdfasfddddddd', 'adsfasdfd', 1439]
print(dokk)
print(len(dokk))
print(dokk[2])

r = open('aa.html')
aatxt = r.read()        # Using .read() function
r.close()
aatxt
len(aatxt)

tot = list()
tot.append('AAAA')
print(tot)
tot.append(354)
print(tot)
tot.append(9721139)
print('Finally', tot)

dicc = dict()
stuff = ['re', 'reee','re', 'haa', 'terer', 'gaa', 're', 'haa']
for st in stuff:
    if st not in dicc:
        dicc[st] = 1
    else :
        dicc[st]  = dicc[st] + 1
print(dicc)
counts = dict()
names = ['re', 'reee','re', 'haa', 'terer', 'gaa', 're', 'haa']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
