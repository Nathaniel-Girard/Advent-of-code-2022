""" def winner(player: str, opponent: str) -> bool:
    difference = player - opponent
    
    match player:
        case 1:
            match opponent:
                case 3:
                    return True
                case 2:
                    return False
        case 2:
            match opponent:
                case 1:
                    return True
                case 3:
                    return False
        case 3:
            match opponent:
                case 2:
                    return True
                case 1:
                    return False

def choice_index(choice: str) -> int:
    if choice in ("A", "X"):
        return 1
    elif choice in ("B", "Y"):
        return 2
    elif choice in ("C", "Z"):
        return 3
    raise Exception

with open("input.txt", "r") as file:
    score = 0
    for line in file.readlines():
        my_shape = choice_index(line[2])
        win = winner(my_shape, choice_index(line[0]))
        if win == None:
            score += 3
        elif win:
            score += 6
        score += my_shape

print(score)
 """

# part 2


def choice_index(choice: str) -> int:
    if choice in ("A", "X"):
        return 1
    elif choice in ("B", "Y"):
        return 2
    elif choice in ("C", "Z"):
        return 3
    raise Exception

with open("input.txt", "r") as file:
    score = 0
    for line in file.readlines():
        match line[2]:
            case "X":
                # finding out what i'll have to play
                score += (choice_index(line[0]) + 2) %3
            case "Y":
                score += choice_index(line[0])
                score += 3
            case "Z":  #3
                score += (choice_index(line[0]) + 1) %3
                score += 6

print(score)

