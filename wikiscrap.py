import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('https://en.wikipedia.org/wiki/The_Doon_School')
for line in fhand:
    print(line.decode().strip())
