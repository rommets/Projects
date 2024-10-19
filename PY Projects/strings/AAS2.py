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
        print('-----------------')

def remove_element():
    input_array = array('i')
    lines = read_file("repeated.txt")
    remove_number = int(lines.pop(0))
    lines.pop(0)
    for line in lines:
        input_array.append(int(line))
    output_array = array('i')
    for num in input_array:
        if num != remove_number:
            output_array.append(num)
    print('2) Your first array:',input_array)
    print('   Your second array:',output_array)
    print('-----------------')

def Report_card():
    report_card={}
    lines=(read_file("reportcard.txt"))
    selected_score=float(lines.pop(0))
    lines.pop(0)
    for i in lines:
         name,grade=i.split(" ")
         report_card[float(grade)]=name
    print("3) Your selected grade:",selected_score)
    print('  ',report_card[selected_score], "recieved that score.")
    print('-----------------')

def Index():
    flag=True
    lines=read_file('random.txt')
    print('4) Here are the indexes: ')
    for i in lines:
      print("  ",i,"'s index =",lines.index(i))
    print('-----------------')

def reverse():
    lines=read_file("random.txt")
    input_array2=array('i')
    reversed_array=array('i')
    for numbers in lines:
        input_array2.append(int(numbers))
    length=int(len(input_array2))
    condition=length*-1
    index=-1
    while(index>=condition):
        reversed_array.append(input_array2[index])
        index=index-1
    print('5) Your first array: ',input_array2)
    print('   It,s reversed: ',reversed_array)
    print('-----------------')

def counter():
    lines=read_file("repeated.txt")
    selected_num=int(lines.pop(0))
    lines.pop(0)
    array1=array('i')
    for nums in lines:
       array1.append(int(nums))
    counter=0
    for nums in array1:
        if nums==selected_num:
            counter+=1
    print('6) In your',array1,': there,s',counter, 'existance of',selected_num)



count_words()
remove_element()
Report_card()
Index()
reverse()
counter()