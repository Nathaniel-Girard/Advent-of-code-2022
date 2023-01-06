

with open("input.txt", "r") as file:
    lines = file.readlines()
    top_max = list(map(int, lines[0][1:-1]))
    visible_count = 2*len(lines[0].strip("\n")) + 2*(len(lines)-1) - 4
    
    # calculate right and bottom max every single time since we are reading from left to right, top to down

    for i, line in enumerate(lines[1:-1]):
        line = line.strip("\n")
        top_max = [max(int(char), top_max[i]) for i, char in enumerate(line[1:-1])]
        left_max = int(lines[i+1][0])
        for j, char in enumerate(line[1:-1]):
            visible = False
            to_evaluate = int(char)
            right_max = max(list(map(int, lines[i+1][1:][j+1:-1])))
            bottom_max = max(*[int(temp_line[j+1]) for temp_line in lines[i+1:]])
            if to_evaluate > left_max:
                left_max = to_evaluate
                visible = True
            
            if to_evaluate > top_max[j]:
                top_max[j] = to_evaluate
                visible = True
            
            
            if to_evaluate > right_max:
                visible = True
            
            
            if to_evaluate > bottom_max:
                visible = True


            if visible:
                visible_count += 1
            else:
                print(f"not visible: {str(i)}, {str(j)} ({char}). top-bottom: {str(top_max[j])}, {str(bottom_max)}. left-right: {str(left_max)}, {str(right_max)}")
                print([int(temp_line[j+1]) for temp_line in lines[i+1:]])


print(visible_count)

        

