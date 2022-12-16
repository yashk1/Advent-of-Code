#https://adventofcode.com/2022/day/1

def get_calories(file_name):
    with open(file_name) as file:
        calories = []
        calorie = 0
        for line in file:
            if line == "\n":
                calories.append(calorie)
                calorie = 0
            else:
                calorie += int(line)

    return calories


if __name__ == '__main__':
    max_calories = max(get_calories("./input/day1.txt"))
    print(f"The Elf with most calories has {max_calories} calories")

    #challenge two
    top3 = sorted(get_calories("./input/day1.txt"), reverse = True)[:3]
    print(f"The top 3 elfs has total {sum(top3)} calories")

