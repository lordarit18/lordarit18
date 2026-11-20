#Find the length of a given string without using the len() function.
s=input('Enter the email:')
L=[]
temp=' '
for i in s:
    if i!=' ':
        temp=temp+i
    else:
        L.append(temp)
        temp=' '
L.append(temp)
print(L)