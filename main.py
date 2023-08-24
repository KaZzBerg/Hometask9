import re

FILE = open('task9.txt', 'r+')

result = [FILE.readline()]

new_result = result[0].replace(',', ' ').split()
new_list = []


def get_words():
    for i in new_result:
        if len(i) >= 7:
            new_list.append(i)
    print(new_list)


print(get_words())
with open('Append.txt', 'w') as file:
    print(new_list, file=file)

words = len(new_result)
print(f'A number of words are: {words}')
