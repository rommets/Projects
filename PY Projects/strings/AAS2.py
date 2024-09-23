directory = "C:/Users/hjas/Projects/personal/romina_projects/PY Projects/strings"
from array import array


def read_file(fileName):
    file = open(directory + "/" + fileName)
    lines = file.read().split("\n")
    return lines


def count_words():
    lines = read_file("input.txt")
    for line in lines:
        words = line.split()
        count = len(words)
        print("word counts in \"" + line + "\" is " + str(count))


def remove_element():
    input_array = array('i')
    lines = read_file("numbers.txt")
    remove_number = int(lines.pop(0))
    lines.pop(0)

    for line in lines:
        input_array.append(int(line))

    output_array = array('i')

    for num in input_array:
        if num != remove_number:
            output_array.append(num)
    print(output_array)


count_words()
remove_element()

# for line in lines:
#     int_array.append(int(line))
# print(int_array)

# print("2) Enter as many numbers as you please (If you're done, type q):")
# while True:
#     current = input()
#     if current == "q":
#         break
#     else:
#         int_array.append(int(current))

# remove_number = int(input("Enter number to remove:"))


report_card=dict()
flag=True
print('3)')
while flag:
    names=input("Enter student,s name\n(type 'done' when you,re done): ")
    if 'done' in names:
        break
    scores=float(input("Enter student,s score: "))
    report_card[names] = scores
    if report_card== {}:
        print("Please enter at least 1 name")
        flag=True
N=float(input("Now enter your chosen score: "))
for names , scores in report_card.items():
    if N == scores:
        print(names.upper(),"received that score")
    if N != scores:
        print("-")
print(end='\n')
# +++++++++++++++++
list2=[]
flag=True
print('4)')
while flag:
    list2.append(float(input("Enter your inputs here\n (type '-1' when you,re done): ")))
    if -1 in list2:
        flag=False
print(list2)
list2.remove(-1)
print("your list: ",list2)
selected_input=float(input("Enter a input so i can tell you its index: "))
print("index =", list2.index(selected_input))