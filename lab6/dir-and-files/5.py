def list(my_list, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in my_list:
            f.write(str(i) + '\n')

my_list = ['apple', 'red', 'flower']
file_name = '3.txt'

list(my_list, file_name)
