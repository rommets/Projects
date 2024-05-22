file=open("fileAdventOfCode.txt") 
data=file.read()
food=data.split('\n')
elf=data.split('\n\n')
sum=0
for food in elf:
    sum += int(food)
max(int(sum))
print(max)
