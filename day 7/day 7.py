from pathlib import Path


with open("input.txt", "r") as file:
    working_dir = Path("/")
    dirs = {working_dir: 0}
    solved = {working_dir: False}
    solving = False

    for line in file.readlines():
        if line[0] == "$":
            if line[2:4] == "cd":
                if solving:
                    solved[working_dir] = True
                    solving = False
                if line[5:7] == "..":
                    working_dir = working_dir.parent
                else:
                    working_dir = working_dir / line[5:-1]
            if line[2:4] == "ls" and not solved.get(working_dir, False):
                dirs[working_dir] = 0
                solved[working_dir] = solved.get(working_dir, False)
                solving = True
        else:
            dir = working_dir
            if line[0].isdigit() and not solved[dir]:
                while dir != Path("/"):
                    dirs[dir] += int(line[0:line.index(" ")])
                    dir = dir.parent
                dirs[dir] += int(line[0:line.index(" ")])
                

    # part 1
    # total = 0
    # for dir in dirs:
    #     if dirs[dir] <= 100000:
    #         total += dirs[dir]

    # part 2
    needed_space = 30000000 - (70000000 - dirs[Path("/")])
    chosen_dir = dirs[Path("/")]
    possible_dirs = []
    for dir in dirs:
        if dirs[dir] >= needed_space:
            possible_dirs.append(dirs[dir])
    chosen_dir = min(*possible_dirs)


# print(total)
print(chosen_dir)

