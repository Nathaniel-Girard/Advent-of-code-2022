with open("input.txt", "r") as file:
    content = file.read()
    marker_chars = []
    counter = 0
    for char in content:

        
        if char in marker_chars:
            del marker_chars[:marker_chars.index(char)+1]
        marker_chars.append(char)
        counter += 1

        # part 1
        # if len(marker_chars) == 4:
        #     break

        # part 2
        if len(marker_chars) == 14:
            break

print(marker_chars)
print(counter)

