my_list = [1, 2, 3, 4, "Naveen", 7.9, 89]

print(my_list[0])
print(my_list[-1])

print(my_list[1:4])

my_list[2] = 99
print(my_list)

my_list.append(500)
print(my_list)

my_list.remove(4)
print(my_list)

popped_element = my_list.pop()
print(my_list)
print(popped_element)

print(len(my_list))

num_list = [10, 5, 30, 25, 15]
num_list.sort()
print(num_list)

my_list.reverse()
print(my_list)
