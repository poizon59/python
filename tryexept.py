try:
    answer = 12/0
    print(answer)
except:
    print('an error occurred')
    
try:
    userInput1 = int(input('enter a number '))
    userInput2 = int(input('enter another number'))
    answer =userInput1/userInput2
    print('answer is', answer)
    myfile = open('missing.txt', 'r')
except ValueError:
    print('error: you did not enter a number')
except ZeroDivisionError:
    print('error: cannot divide by zero')
except Exception as e:
    print('unknown error:', e)
    