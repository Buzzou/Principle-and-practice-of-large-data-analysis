import re


def textcreat(name, text):
    some_file = open(name + '.txt', 'w')
    some_file.write(text)
    some_file.close()


textcreat('name', 'something')


def Replace(explicit='暴力', sentence='暴力执法'):
    filtered = re.sub(explicit, '**', sentence)
    # print(filtered)
    return filtered


Replace()


def rewrite(name='filtered.txt'):
    filtered_file = open(name, 'w')
    filtered_file.write(Replace())
    filtered_file.close()


rewrite()
