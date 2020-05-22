
string = 'aabaacfgfh'
dic = {}
unique = []
for i in string:
    if i not in dic:
        dic[i] = 1
        unique.append(i)
    else:
        dic[i] += 1

print(unique)
