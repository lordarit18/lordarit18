num1,num2=0,1
for i in range(10):
    print(num1)
    next=num1+num2
    num1=num2
    num2=next
    print(next)
