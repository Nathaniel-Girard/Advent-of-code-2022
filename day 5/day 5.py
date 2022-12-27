import re
from itertools import repeat

with open("input.txt", "r") as file:
    stacks = [[] for _ in range(9)]
    
    lines = file.readlines()
    for i, line in enumerate(lines):
        if i < 10:
            # initialisation
            if i < 8:
                for j in range(9):
                    item = lines[7-i][1+4*j]
                    if item != " ":
                        stacks[j].append(item)
        else:
            move_begin = line.index("move") + 5
            move = int(line[move_begin: move_begin + line[move_begin:].index(" ")])
            from_stack = int(line[line.index("from") + 5]) - 1
            to_stack = int(line[line.index("to") + 3]) - 1
            print("moving " + str(move) + " times from " + str(from_stack + 1) + " to " + str(to_stack + 1))
            # part 1
            # for _ in range(move):
                # stacks[to_stack].append(stacks[from_stack].pop())

                # print("from stack: " + str(stacks[from_stack]))
                # print("to stack " + str(stacks[to_stack]))

            # part 2
            stacks[to_stack] += stacks[from_stack][-move:]
            del stacks[from_stack][-move:]


                

print()
# [print(stack) for stack in stacks]
answer = "".join([stack.pop() for stack in stacks])





print(answer)