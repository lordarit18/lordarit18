#Code here
s='PyNative'
upper=' '
lower=' '

for i in s:
    if i.islower():
        lower=lower+i
    else:
        upper+i
print(lower+upper)