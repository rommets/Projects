file=open("fileAdventOfCode.txt") 
data=file.read()
sum=0
elf=data.split('\n\n')
for food in elf:
    food=data.split('\n')
    sum += int(food)
max(int(sum))
print(max)
