count = 0
list_1 = [1,2,3,4,5,6]
for A in list_1:
    if A in list_1:
        print("%d is in the list_1" %A)
        count = count + 1

print("---------------------------------------------")

count_1 = 0
list_2 = [82,84,24,8,50,51]
for B in list_2:
    if B <= 60:
        print("%d is under 60" %B)
        count_1 = count_1 + 1
        print("-> %dth counted" %count_1)
    else:
        print("%d is above 60" %B)
        count_1 = count_1 + 1
        print("-> %dth counted" %count_1)

print("---------------------------------------------")

list_3 = [(1,2),(3,4),(5,6)]
for (first,second) in list_3:
    print(first + second)

print("---------------------------------------------")

count_2 = 0
for C in range(10):
    count_2 = count_2 + C
    print(count_2)

print("---------------------------------------------")

count_3 = 0
list_4 = [64,78,61,59,90]
for D in list_4:
    if D >= 61:
        count_3 = count_3 + 1
        print("%dth student passed" %count_3)
    else:
        count_3 = count_3 + 1
        print("%dth student is not passed" %count_3)

print("---------------------------------------------")