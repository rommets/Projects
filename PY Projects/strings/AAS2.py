Input=input("1) Please enter your phrase: ")
list=Input.split()
print("your phrase has",len(list),"words")
print(end='\n')
# +++++++++++++++++
# import array
# array2=('d',[])
# flag=True
# while flag:
#     a=input("2) Enter as many numbers as you please (If you,re done, type 0): ")
#     array2.append(a)
#     if '0' in array2:
#         flag=False
# print(array2)
# special_nummer= float(input("Enter your cursed nummer: "))
# flag2=True
# while flag2:
#     if special_nummer in array2:
#         array2.remove(special_nummer)
#     else:
#         flag2=False
# print(array2)
# +++++++++++++++++
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
# To be continued...
