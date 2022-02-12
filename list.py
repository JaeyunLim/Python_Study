#printing num_list
num_list = [1,2,3,4,5]
print(num_list)

#printing str_list
str_list = ['Hello', 'World']
print(str_list)

#printing str,num_list
mix_list = [1,2,3, "Hello"]
print(mix_list)

#plus, multiple list
print(mix_list[0] + mix_list[2])
print(mix_list[1] * 2)
print(mix_list[-1])

#list indexing
double_list = [1,2,3, [1,2,3]]
print(double_list[-1])
print(double_list[-1][1])
print(double_list[-1][-1])

#list slicing
print(num_list[2:])

#list sort,reverse
odd_list = [1,3,5,7,9]
even_list = [2,4,6,8,10]
total_list = odd_list + even_list
print(total_list)
total_list.sort()
print(total_list)
total_list.reverse()
print(total_list)

#multiplying list
print(odd_list * 2)

#list len
print(len(total_list))

#list addition
simple_list = [1,2,3]
simple_list[2] = 4
print(simple_list)
print("Hello" + " " + str(simple_list[-1]))

#deleting list
del simple_list[-1]
print(simple_list)

#methods for list
easy_list = [1,2,3]
print(easy_list)
easy_list.append(4)
print(easy_list)
easy_list.append([5,6])
print(easy_list)
easy_list.reverse()
print(easy_list)
easy_list[0].reverse()
print(easy_list)
print(easy_list.index(3))
easy_list.insert(0,9)
print(easy_list)
easy_list.pop()
print(easy_list)


aaalist = [1,2,3,4,5]
aaalist.pop(-1)
print(aaalist)

print("---------------------------------------------")

list_A = [1,2,3,4,5]

print(list_A.index(2))
