with open("input.txt", "r") as file:
    maximum_calories = [0]
    calories = 0
    for line in file.readlines():
        line = line.strip("\n")
        if line == "":
            calories = 0
            continue
        calories += int(line)
        if calories > maximum_calories[0]:
            maximum_calories.append(calories)
            maximum_calories.sort()
            if len(maximum_calories) > 3:
                del maximum_calories[0]

print(sum(maximum_calories))