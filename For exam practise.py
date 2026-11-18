num=int(input('Enter a number:'))
temp=num
total=0
power=len(str(num))
while temp>0:
    digit=temp%10
    total+=digit**power
    temp//=10

if num==total:
    print('Armstrong')
else:
    print('not')