print ("hello World")

userage = 0

userAge, userName= 30, "Peter"

print(userAge , userName)
    
x = 5
y = 10
y = x
print("x = ", x)
print("y = ", y)
    
print(userName.upper())    

brand = "Apple"
exchangeRate = 1.235235245
messege = 'the price of this %s laptop is %d USD'\
          ' and the exchange rate is %4.2f USD to 1 EUR'\
          %(brand, 1299 , exchangeRate)
    
print(messege)


brand,cost,exchangeRate  = "Apple", 1299, 1.235235245 
print(f'the price of this {brand} laptop is {cost} USD and the exchange rate is {exchangeRate} USD to 1 EUR')

messege = 'the price of this {0} laptop is {1} USD and the exchange rate is {2} USD to 1 EUR'.format('Apple', 1299, 1.235235245)
print(messege)

listName = [21,22,23,24,25]

listName.append(int(47))
print(listName)

#список

myLis = [1,2,3,4,5, "Hello"]
print(myLis[2])
print(myLis[1:5])
myLis[1] = 20
print(myLis)

myLis.append("How are you")
print(myLis)

del myLis[-2]
print(myLis)


#кортеж
monthOfYear = ("jan", "feb", "dec")
print(monthOfYear)


#Словарь

myDict = {"peter:38", "john:51", "peter:14"}
print(myDict)


