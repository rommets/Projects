file = open("mainFile.txt")
data = file.read()


def part1(data):
    elf_list = data.split("\n\n")
    max_sum = 0
    for elf in elf_list:
        sum = 0
        foods = elf.split("\n")
        for food in foods:
            sum += int(food)
        max_sum = max(sum, max_sum)

    return max_sum


def part2(data):
    elf_list = data.split("\n\n")
    sum_list = []
    for elf in elf_list:
        sum = 0
        foods = elf.split("\n")
        for food in foods:
            sum += int(food)
        sum_list.append(sum)

    sum_list.sort()
    return sum_list[-1] + sum_list[-2] + sum_list[-3]


print(f"part1: {part1(data)}")
print(f"part2: {part2(data)}")
