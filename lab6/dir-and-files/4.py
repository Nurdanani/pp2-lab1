def count_lines(filename):
    with open(filename, 'r') as f:
        line_count = 0
        for lines in f:
            line_count += 1
    return line_count

file_name = '3.txt'

num_lines = count_lines(file_name)
if num_lines is not None:
    print(f"Number of lines in '{file_name}': {num_lines}")