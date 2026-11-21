#Code here
d='aaabbbbbcccdddeeeffff'
res=' '

for i in d:
    if i not in res:
        res=res+i
print(res)