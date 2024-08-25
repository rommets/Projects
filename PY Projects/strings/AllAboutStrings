sample = input('please write a phrase: ')
LabRat = sample.upper()
print('1)', LabRat)
# # -------------------
LabRat = sample.lower()
print('2)', LabRat)
# # -------------------
LabRat = sample.startswith("A") or sample.startswith("B") or sample.startswith("C")
# LabRat = sample[0] in ["A", "B", "C"]
if LabRat == False:
    print('3) Is your phrase starts with A,B,C? FALSE')
else:
    print('3) Is your phrase starts with A,B,C? TRUE')
# # -------------------
count = 0
for char_num in sample:
    count += 1
print('4)', count)

dic = {"brand": "Ford", "model": "Mustang", "year": 1964, "maintained": True}

# or-----> print("4)",len(sample))
# -------------------
unique_list = []
for letter in sample:
    if letter not in unique_list:
        unique_list.append(letter)
print('5-1)', len(unique_list))
sorted_string = sorted(sample)
count = 1
for i in range(len(sample) - 1):
    if sample[i] != sample[i + 1]:
        count += 1
print("5-2)", count)
# -------------------
LabRat = sample.replace('o', 'u')
print('6)', LabRat)
# the main form is .replace('sample','LabRat',count) but the count part is optional.
# -------------------
words = sample.split(" ")
capitalized = []
for word in words:
    capitalized.append(word.capitalize())
print('7-1)', " ".join(capitalized))

LabRat = sample.split(' ')
print('7-2) ', end='')
for sentence in LabRat:
    print(sentence.capitalize(), end=' ')
print(end='\n')
# -------------------
count = 0
for i in sample:
    if i == 'o':
        count += 1
print("8) There are %s 'o's in your phrase" % count)