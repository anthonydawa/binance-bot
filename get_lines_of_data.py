arr = []

with open('lines_of_data', 'r') as f:
    for lines in f.readlines():
        arr.append(lines)

print(arr[2][0])