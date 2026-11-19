salary=float(input('Enter your salary:'))
experience=int(input('Enter years of experience:'))
rating=float(input('Enter performane rating(1-5):'))

if experience<2:
    bonus=0
else:
    if experience<=5:
        if rating>=4:
            bonus=salary*0.10
        else:
            bonus=salary*0.05
    else:
        if rating>=4:
            bonus=salary*0.15
        elif rating>=3:
            bonus=salary*0.10
        else:
            bonus=salary*0.05

print('Bonus=', bonus)
print('Total salary=', salary+bonus)