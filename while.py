counter = 5

while counter > 0:
    print('counrer =', counter)
    counter = counter -1
    
j = 0 
for i in range(5):
    j = j + 2
    print('i =', i, 'j =', j)
    if j == 6:
        break
        
        
j = 0 
for i in range(5):
    j = j + 2
    print('\ni =', i, 'j =',j)
    if j == 6:
        continue
    print(' i will be skiooed over if j = 6')