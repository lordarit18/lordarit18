# Write code here
sum=0
count=0

while True:
    num=int(input('Enter number:'))
    if num==0:
        break
    sum=sum+num
    count=count+1

print('sum', sum)
print('avg', sum/count)

