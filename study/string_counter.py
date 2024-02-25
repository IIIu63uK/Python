def string_counter(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return len(lines)

print(string_counter('file.txt'))