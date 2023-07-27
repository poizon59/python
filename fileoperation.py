import os

f = open ('myfile.txt', 'r')

firstline = f.readline()
secondline = f.readline()
print(firstline)
print(secondline)
print(firstline, end = '')

f.close()



f = open ('myfile.txt', 'r')
for line in f:
    print(line, end = '')
    
    


f = open ('myfile.txt', 'a')

f.write('\nThis sentence wikk be appended.')
f.write('\nPython is Fun!')
f.close()

inputfile = open('myfile.txt', 'r')
outputfile = open('myoutputfile.txt', 'w') 
msg =inputfile.read(10)
while len(msg):
    outputfile.write(msg)
    msg = inputfile.read(10)
    
inputfile.close()
outputfile.close()

inputfile = open('myimage.jpg', 'rb')
outputfile = open('myoutputimage.jpg', 'wb') 
msg =inputfile.read(10)
while len(msg):
    outputfile.write(msg)
    msg = inputfile.read(10)
    
inputfile.close()
outputfile.close()

os.rename('myimage.jpg', 'myimage1.jpg' )