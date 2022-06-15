#def aadi(name) :
    #if name == 'Aadi' :
    #    y = input('Welcome Aadi whats up')
    #    if y == 'good':
    #        print('Now we are talking')
    #    elif y == ('Bad') :
    #        print('not good')
    #    else :
        #    print('Thats good')
#aadi('Aadi'
#def addtwo(a, b) :
#    added = a + b
#    return added

#    x = addtwo(3, 5)
#    print(x)
#dic = dict()
#count = 0
#for stat in inp :
#    inp = input('Enter you statement')
#    dic['Item', count] = inpu
#    count = count + 1
#    if inp =='ok' :
#        break
#print(dic)
co = 0
x = 0
while x == 0:
    co = co + 1
    print('trial :', co)
import xml.etree.ElementTree as ET


input = '''
<stuff>
<users>
<user "2">
<id>001</id>
<name>Chuck</name>
</user>
<user x="7">
<id> 009</id>
<name>Brent</name>
</user>
</users>
</stuff>'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', items.get("x"))
