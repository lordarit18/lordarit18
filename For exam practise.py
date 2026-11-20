#Find the length of a given string without using the len() function.
s='Iam 25 years and 10 months old'

res=' '
for i in s:
    if i.isdigit():
        res=res+i

print(res)
