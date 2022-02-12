# adding two numbers
a=123
b=123.45
print(a+b)      # general print
print("answer is %d" %(a+b))   # print in int type
print("answer is %.2f" %(a+b)) # print in float type

print("---------------------------------------------------------")

# power of num
c=2
answer=c**3
print(answer)

print("---------------------------------------------------------")

# string + \n
print('c**3\n')

print("---------------------------------------------------------")

# number + \n
print("answer is %d\n" %answer)

print("---------------------------------------------------------")

# Remainder
num1 = 10
num2 = 15
print(num1%2)
print(num2%2)
print("answer is %d" %(num1%2)) #숫자(정수)로 출력할때
print("answer is %f" %(num2%2)) #숫자(실수)로 출력할때
print("answer is %.2f" %(num2%2)) #숫자(실수), 하지만 소수점 뒤 2자리 까지 출력하고 싶을때
print("answer is %s" %(num2%2)) #문자열로 출력하고싶을떄

print("---------------------------------------------------------")

# print string
print("Hello World")

print("Python's favorite language is Perl.")

print('I said "jaeyun is smart boy".')

str1 = "jaeyun"
str2 = " is kind"
print(str1 + str2)

str3 = "python"
str4 = str3 *3
print(str4)

print("---------------------------------------------------------")
print("---------------------------------------------------------")
# len(string)
str5 = "abcdefg"
print("answer is %d" %len(str5))
print(str5[0])
print(str5[2])
print(str5[-1])

