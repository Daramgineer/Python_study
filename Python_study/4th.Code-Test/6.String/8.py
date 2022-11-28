a = input().lower()
a_list = list(a)
check = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
time = 0
for i in a_list:
    if i in check[0]:
        time += 3
    elif i in check[1]:
        time += 4
    elif i in check[2]:
        time += 5
    elif i in check[3]:
        time += 6
    elif i in check[4]:
        time += 7
    elif i in check[5]:
        time += 8
    elif i in check[6]:
        time += 9
    elif i in check[7]:
        time += 10
    elif i in check[8]:
        time += 11

print(time)