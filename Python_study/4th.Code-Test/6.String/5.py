word = input().lower()
word_list = list(set(word))
w = [] 

for i in word_list:
    count = word.count(i)
    w.append(count)

if w.count(max(w)) >= 2:
    print("?")
else:
    print(word_list[(w.index(max(w)))].upper())