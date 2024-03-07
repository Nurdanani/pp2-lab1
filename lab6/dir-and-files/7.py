def copy_file(source_file, destination_file):
        with open(source_file, 'r') as f_source:
            content = f_source.read()

        with open(destination_file, 'w') as f_dest:
            f_dest.write(content)

source_file = '3.txt'
destination_file = '1.txt'

copy_file(source_file, destination_file)