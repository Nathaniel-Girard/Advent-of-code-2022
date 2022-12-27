import re

with open("input.txt", "r") as file:
    pairs = 0
    for line in file.readlines():
        assignment_pattern = re.compile("[0-9]+-[0-9]+")
        assignments = assignment_pattern.findall(line)
        border_pattern = re.compile("[0-9]+")
        first_borders = list(map(int, border_pattern.findall(assignments[0])))
        second_borders = list(map(int, border_pattern.findall(assignments[1])))
        
        """ 
        part 1
        # first contains the other
        if first_borders[0] <= second_borders[0] and first_borders[1] >= second_borders[1]:
            pairs+=1
        # second contains other
        elif second_borders[0] <= first_borders[0] and second_borders[1] >= first_borders[1]:
            pairs += 1
        """
        # part 2

        # first borders contained
        if first_borders[0] >= second_borders[0] and first_borders[0] <= second_borders[1]:
            pairs += 1
        elif first_borders[1] >= second_borders[0] and first_borders[1] <= second_borders[1]:
            pairs += 1
        # second borders contained
        elif second_borders[0] >= first_borders[0] and second_borders[0] <= first_borders[1]:
            pairs += 1
        elif second_borders[1] >= first_borders[0] and second_borders[1] <= first_borders[1]:
            pairs += 1


print(pairs)