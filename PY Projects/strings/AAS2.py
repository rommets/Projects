directory = "C:\\Users\\Lenovo-T570\\Projects\\PY Projects\\strings"
from array import array


def read_file(fileName):
    file = open(directory + "/" + fileName)
    lines = file.read().split("\n")
    return lines


def count_words():
    lines = read_file("test.txt")
    for line in lines:
        khat = len(line.split())
        count = len(line)
        print("1) In \"" + line + "\" we have "+ str(khat) + " and "+ str(count)+" words")


def remove_element():
    input_array = array('i')
    lines = read_file("numbers.txt")
    remove_number = int(lines.pop(0))
    lines.pop(0)
    # why is it removing 12 also
    for line in lines:
        input_array.append(int(line))

    output_array = array('i')

    for num in input_array:
        if num != remove_number:
            output_array.append(num)
    print('2)',output_array,end='\n')

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

# def Report_card():
#     report_card=dict()
#     flag=True
#     lines=read_file("reportcard.txt")
#     report_card.append(lines)
#          scores=float(input("Enter student,s score: "))
#          report_card[names] = scores
#          if report_card== {}:
#             print("Please enter at least 1 name")
#             flag=True
#     N=float(input("Now enter your chosen score: "))
#     for names , scores in report_card.items():
#          if N == scores:
#              print(names.upper(),"received that score")
#          if N != scores:
#              print("-")
#     print(end='\n')

def Index():
    flag=True
    lines=read_file('numbersWOspace.txt')
    print('4)')
    for i in lines:
      print(i,"'s index =",lines.index(i))

count_words()
remove_element()
# Report_card()
Index()