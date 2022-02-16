#Basic str print
print("Hello World")
print("Python's favorite food is perl")#
print('I said "Jaeyun is a smart boy"')

#str print with %s plus \t(tab)
str1 = "Hello World"
print("answer is %s\t" %str1)

#str addition
str2 = "Water"
str3 = "Drink"
print(str3 + " "+ str2)\

#print str len, str indexing, str slicing
str4 = "abcde"
print(len(str4))
print(str4[1])
print(str4[-1])# -1 = last index
print(str4[4:])
print(str4[len(str4)-1])

#str slicing
str5 = "Life is too short"
print(str5[0:4])
print(str5[5:12])
print(str5[12:])

#str addition + str slicing
str6 = "20211208Sunny"
print('"Year = str6[0:4], month = str6[4:6], day = str6[7], weather = str[8:]"')
year = str6[0:4]
month = str6[4:6]
day = str6[7]
weather = str6[8:]
print("Year = %s," %year + " month = %s," %month + " day = %s," %day + " weather = %s" %weather)

#str edit
str7 = "pithon"
char1 = 'y'
print(str7[0] + char1 + str7[2:])

#str count,find,index
str8 = "AAbbCCddEEff"
print(str8.count('C'))
print(str8.find('d'))
print(str8.index('d'))

#str upper, lower
upper1 = str8.upper()
print(upper1)
lower1 = str8.lower()
print(lower1)