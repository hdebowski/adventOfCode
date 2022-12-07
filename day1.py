with open('input1.in') as file:
    data = [i for i in file.read().strip().split("\n")]

max = 0
count = 0
for item in data:
    if item != '':
        count = count + int(item)
    else:
        count = 0
    if count > max:
        max = count

print(max)