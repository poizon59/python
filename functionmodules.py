print('hello world');

newString = 'hello world'.replace('world', 'universe')
print(newString)

def checkIfPrime (numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck%x == 0):
            return False
        return True
    

answer = checkIfPrime(13)
print(answer)



messege1 = 'global variable'

def myFunction():
    print('\nInside the function')
    # Глобальные переменные доступны внутри функции
    print(messege1)
    # Объявление  локальной переменной
    messege2 = 'Local variable'
    print(messege2)
    
def myFunction2():
    print('\noutside the function')
    # Глобальные переменные доступны внутри функции
    print(messege1)
    # Объявление  локальной переменной

    print(messege2)
    
#myFunction2()


messege1 = 'Global Variable ( shares same name as a local variable)'

def myFunction():
    messege1 = 'Global Variable ( shares same name as a global variable)'
    print('n\Inside the function')
    print(messege1)
    
myFunction()

print('n\outside the function')
print(messege1)


def someFunction(a,b,c=1,d=2,e=3):
    print(a,b,c,d,e)
    
someFunction(10,20)
someFunction(10,20,30,40)


def addNumber(*num):
    sum = 0
    for i in num:
        sum = sum + i
    print(sum)
    
addNumber(1,2,3,4,5,6,7,8)

def printMemberAge(**age):
    for i,j in age.items():
        print('Name = %s, Age = %s' %(i,j))
        print(f'Name = {i}, Age = {j} ')
        
printMemberAge(peter=5,john=7,kta = 8)