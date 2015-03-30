__author__ = 'Sergey'
import re
words = {}
fileName = 'const.txt'
file = open(fileName, 'rt')
for line in file:
    line = re.sub('[^0-9a-zA-Z|\s]+', '', line)
    lineWords = line.split()
    for word in lineWords:
        if word.lower() not in words:
            words[word.lower()] = 1
        else:
            words[word.lower()] += 1
file.close()

wordsByCount = sorted(words.items(), key=lambda x: x[1], reverse=True)

for word in wordsByCount:
    print(word[0], word[1])

