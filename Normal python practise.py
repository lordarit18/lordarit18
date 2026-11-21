#Code here
import math
number=145
original_number=number
total_sum=0
while number>0:
    digit=number%10
    digit=number%10
    total_sum+=math.factorial(digit)

if total_sum==original_number:
    print(f"{original_number} is a strong Number")
else:
    print(f"{original_number} is NOT a strong Number")