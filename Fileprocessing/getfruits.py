myfile = open("files/fruits.txt")
content = myfile.read()
print(f'Long method: \n{content} \n')
#Cursor is at end of text file now, so print(myfile.read()) will not work two times

#Close file after done using it
myfile.close()
#Printing myfile.read() will now give error

#EASIER WAY TO DO THIS WHOLE THING   (Closes file auto)
with open("files/fruits.txt") as myfile:
    newcontent = myfile.read()
print(f'Short method: \n{newcontent}\n')



#Creating file and writing text
with open("files/vegetables.txt","w") as writefile:
    writefile.write("Tomato\nCucumber\nOnion")

#Dont overwrite existing file
with open("files/fruits.txt","a") as notoverwrite:
    notoverwrite.write('\nOkra')
    #reset cursor
    notoverwrite.seek(0)