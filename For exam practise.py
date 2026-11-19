'''Accept an integer and determine whether it is:'''

n=int(input('Enter a number:'))
if n>0:
    print('Positive Number:')

    if n%2==0:
        print('Even Number')

        if n%4==0:
            print('Ddivisible by 4')
        else:
            print('Not divisible by 4')
    else:
        print('Odd Number')

    if n%3==0:
        print('Divisible by 3')
    else:
        print('Not divisible by 3')
elif n<0:
    print('Negative number')

    if n%2==0:
        print('Even negative Number:')
    else:
        print('Odd negative Number')

else:
    print('Zero')