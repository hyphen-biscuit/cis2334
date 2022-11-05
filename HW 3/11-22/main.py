#Dashiell Wendt 2033998

inputt = input()
words = inputt.split()
wordEmpty = []
for wordIndex in words:
    wordEmpty.append(str(wordIndex))
for pos, val in enumerate(wordEmpty):
    print('{} {}'.format(val, wordEmpty.count(wordEmpty[pos])))