string = 'aabaacfgfh'
dic = {}
unique = []
for i in string:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
for i in string:
    if dic[i] == 1:
        unique.append(i)
print(unique)