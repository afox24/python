my_int = 1
my_str = "Hello"
my_float = 2.5
my_list = ['big', 'cuty', 'life']
my_dict = {'country': 'Россия', 'city': 'Москва'}
my_tuple = ('my', 'life', 'be', 'like')
big_list = [my_int, my_str, my_float, my_list, my_dict, my_tuple]
for i in big_list:
    print(f'{i} is {type(i)}')