directory = "C:\\Users\\Lenovo-T570\\Projects\\PY Projects\\strings\\files"
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
        print("1) In \"" + line + "\" we have "+ str(khat) + " lines" + " and "+ str(count)+" words.")


def remove_element():
    input_array = array('i')
    lines = read_file("repeated.txt")
    remove_number = int(lines.pop(0))
    for line in lines:
        input_array.append(int(line))
    output_array = array('i')
    for num in input_array:
        if num != remove_number:
            output_array.append(num)
    print('2)',output_array,end='\n')

def Report_card():
    report_card={}
    lines=(read_file("reportcard.txt"))
    selected_score=float(lines.pop(0))
    lines.pop(0)
    for i in lines:
         name,grade=i.split(" ")
         report_card[float(grade)]=name
    print("3)",report_card[selected_score], "recieved that score.")

def Index():
    flag=True
    lines=read_file('random.txt')
    print('4) Here are the indexes: ')
    for i in lines:
      print(i,"'s index =",lines.index(i))

# def reverse():
#     lines=read_file("random.txt")
#     input_array2=array('i')
#     for i in lines:
#         input_array2.append(int(i))
#     print(input_array2[])


count_words()
remove_element()
Report_card()
Index()
# reverse()