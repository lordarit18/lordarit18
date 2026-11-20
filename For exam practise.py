#Find the length of a given string without using the len() function.
n=int(input('Enter the number:'))
binary=[]
while n>0:
    binary.append(n%2)
    n=n//2

for i in binary[::-1]:
    print(i, end=' ')
    