my_list = [2, 56, 21, 15, 97, 34, 81]
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new_list)