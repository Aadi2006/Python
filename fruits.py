#open file
#Even I have no clue whawt this is
myfile = open("fruits.txt")
print(myfile.read())
myfile.close()
#open file in another way
with open('p4e/clown.txt') as myfile:
    content=myfile.read()
print(content)
#Make new file
with open('vegetables.txt',"w") as myfile:
    myfile.write('vegetables\nTomato\nonion\nNot Yummy')
#to add in existing file use "a"

import time
while True:
    with open('fruits.txt') as file:
        print(file.read())
        time.sleep(10)
