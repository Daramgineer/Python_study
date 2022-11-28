num = int(input())
count = 0

for _ in range(num):
    word = input().lower()
    no_count = 0

    for index in range(len(word)-1):
        if word[index] != word[index+1]:
            new_word = word[index+1:]
            if new_word.count(word[index]) > 0:
                no_count += 1

    if no_count == 0:  
        count += 1
        
print(count)