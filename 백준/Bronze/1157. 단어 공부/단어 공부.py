import sys

word = sys.stdin.readline().rstrip().upper()
unique_words = list(set(word))

counts = []
for x in unique_words:
    counts.append(word.count(x))

max_count = max(counts)


if counts.count(max_count) > 1:
    print("?")
else:
    max_index = counts.index(max_count)
    print(unique_words[max_index])