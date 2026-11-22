#Code here
import math
number=145

original_num=number
total_sum=0

while number>0:
    digit=number%10
    total_sum+=math.factorial(digit)
    number//=10

if total_sum==original_num:
    print(f"{original_num} is a stong number")
else:
    print(f"{original_num} is NPT a strong number")