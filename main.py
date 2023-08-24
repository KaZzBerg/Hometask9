FILE = open('task9.txt', 'r+')

file_list = [FILE.readline()]

FILE.close()

split_list = file_list[0].split()

for i in split_list:
    if i == 'a':
        i = split_list.remove('a')
    if i == 'an':
        i = split_list.remove('an')
    if i == ',':
        i = split_list.remove(',')
    else:
        pass

new_list = []


def get_words():
    for i in split_list:
        if len(i) >= 7:
            new_list.append(i)
    print(new_list)


print(get_words())
with open('Append.txt', 'w') as file:
    print(new_list, file=file)

file.close()

number_words = len(split_list)
print(f'A number of words are: {number_words}')
