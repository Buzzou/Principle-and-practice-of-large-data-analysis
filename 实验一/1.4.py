import collections

novel = open('Walden.txt', 'r')

bag_of_words = []

for line in novel:
    bag_of_words.extend(line.strip().split())

print(collections.Counter(bag_of_words))
