myDict = {"peter:38", "john:51", "peter:14"}
print(myDict)

userNameAndAge = {"peter:38", "john:51", "alex:14", "alvin:Not Available"}
print(userNameAndAge)

userNameAndAge = dict(peter = 38, john = 51, alex = 14 , alvin = "Not Available")
print(userNameAndAge)


mydict2 = {"one":1.35, 2.5:"two point five",3:"+",7.9:2}
print(mydict2)

print(mydict2["one"])
print(mydict2[7.9])

mydict2["new item"] = "i'm new"
print(mydict2)

del mydict2["one"]
print(mydict2)