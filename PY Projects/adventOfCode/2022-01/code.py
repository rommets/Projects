file=open("input.txt") 
data=file.read()
def part1(data):
    elf_list=data.split('\n\n')
    max_sum = 0
    for elf in elf_list:
        sum=0
        foods=elf.split('\n')
        for food in foods:
            sum += int(food)
        max_sum = max(sum, max_sum)

    return max_sum

print(f'part1: {part1(data)}')
