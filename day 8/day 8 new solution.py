with open("input.txt", "r") as file:
    lines = file.read().splitlines()

    top_max = list(map(int, lines[0][1:-1]))
    visible_count = 2*len(lines[0]) + 2*(len(lines)) - 4
    
    i = 0
    for line in lines[1:-1]:
        i += 1
        j = 0
        left_max = int(lines[i][0])
        top_max = [max(top_max[i], element) for i, element in enumerate(list(map(int, lines[i][1:-1])))]

        for char in line[1:-1]:
            j += 1

            char = int(char)

            right_max = max(list(map(int, lines[i][j+1:])))
            bottom_max = max(list(map(int, [element[j] for element in lines[i+1:]])))

            if char > top_max[j-1] or char > left_max or char > right_max or char > bottom_max:
                visible_count += 1 

            if char > left_max:
                left_max = char
            if char > top_max[j-1]:
                top_max[j-1] = char

print(visible_count)

