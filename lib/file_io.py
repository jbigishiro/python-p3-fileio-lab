def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as file:
        content=file.write(file_content)
    return content

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as file:
        content=file.write(append_content)
    return content

def read_file(file_name):
    with open(f'{file_name}.txt', 'r') as file:
        content = file.read()
    return content
