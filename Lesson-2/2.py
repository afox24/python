my_list = ['1', '2', '3', '4', '5']
i = 1
while i < len(my_list):
    tmp = my_list[i]
    my_list[i] = my_list[i-1]
    my_list[i-1] = tmp
    i += 2
print(my_list)