import string
"""
with open("input.txt") as file:
    score = 0
    for line in file.readlines():
        line = line.strip("\n")
        middle = int(len(line)/2)
        for char in line[0:middle]:
            if char in line[middle:]:
                score += string.ascii_lowercase.index(char.lower()) + (26 if char.isupper() else 0) + 1
                break

print(score) """

# part 2

with open("input.txt", "r") as file:
    score = 0
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        for char in lines[i]:
            if char in lines[i+1] and char in lines[i+2]:
                score += string.ascii_lowercase.index(char.lower()) + (26 if char.isupper() else 0) + 1
                break
print(score)