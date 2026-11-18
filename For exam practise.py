students=[]
num=int(input('Enter a number:'))
for i in range(num):
    print('Number of', i+1,'applicants')
    name=input('Enter your name:')
    h_ed=input('Enter your higher education:')
    p_skill=input('Enter your p skills:')
    yog=input('Enter years of graduation:')

    students.append((name,h_ed,p_skill,yog))

required_skill=input('Enter req skill:')
required_hed=input('Enter required higher education:')
required_yog=input('Enter req year of graduation:')

flag=False
for i in students:
    if i[1]==required_hed and i[2]==required_skill and i[3]==required_yog:
        print(i)
        flag=True
if flag==False:
    print('No such candidates')