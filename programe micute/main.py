sentence = input()

freq = dict.fromkeys(tuple(sentence.lower().split()), 0)
for word in sentence.split():
    freq[word.lower()] += 1

for key, value in freq.items():
    print(key + " " + str(value))
