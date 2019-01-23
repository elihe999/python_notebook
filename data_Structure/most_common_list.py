words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)

print(word_counts['not'])

print(word_counts['eyes'])


morewords = ['why','are','you','not','looking','in','my','eyes']

for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes'])



a = Counter(words)
b = Counter(morewords)

print("a: ", a)
print("b: ", b)

c = a + b
print(c)

d = a - b
print(d)

