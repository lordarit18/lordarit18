str1 = "This is a string."
str2 = "Apna College"
str3 = """This is a string with triple quotes.It can span multiple lines."""
"This is a apnacollege's tutorial on strings in Python. Strings are sequences of characters and can be defined using single quotes, double quotes, or triple quotes. They are immutable, meaning that once a string is created, it cannot be changed. You can perform various operations on strings such as concatenation, slicing, and formatting. Additionally, Python provides a wide range of built-in methods for string manipulation, making it a powerful tool for text processing."
str3 = "This is a string."
print(str1)
str4 = "This is a string. \n we are creating it in Python."
print(str4)
str1 = "apna"
str2 = "college"
final_str = str1 + str2
print(final_str)
print(len(str1))
len2 = len(str2)
print(len2)
final_str = str1 + " " + str2
print(final_str)
str = "apna college"
print(str[5:12])
print(str[:4])
str = "apple"
print(str[-5:-1])
str = "i am studing python from apna college"
print(str.endswith("ege"))
print(str.capitalize())
print(str)
str = str.capitalize()
print(str)
print(str.replace("python", "java"))
print(str.find("from"))
print(str.count("fr"))
str = "Hi I am the $ symbol $99.9"
print(str.count("$"))
age = 21
if age>=18:
    print("Can vote and apply for license")
    print("Can drive")
light = "green"

if(light== "red"):
    print("stop")
elif(light== "yellow"):
    print("wait")
else:
    print("go")

print("end of the program")

num = 5
if num>3:
    print("Greater than 3")
elif num>3:
    print("Greater than 3")
    age = 24
if age>=18:
    print("Can vote")
else:
    print("Cannot vote")
    #Grade on their marks
    marks=90
    if marks>=90:
        print("A grade")
    elif marks>=80 and marks<90:
        print("B grade")
    elif marks>=70 and marks<80:
        print("C grade")
    else:
        print("D grade")

num = 60
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")



