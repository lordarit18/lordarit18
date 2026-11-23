#Code here
#Function
def analyse_string(s):
    vowels=0
    consonants=0

    for ch in s.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels+=1
            else:
                consonants+=1
    cleaned=" ".join(ch.lower() for ch in s if ch.isalnum())
                
    if cleaned==cleaned[::-1]:
        palindrome='Yes'
    else:
        palindrome='No'

    return vowels, consonants, palindrome
text=input('Enter a string:')
v, c, p=analyse_string(text)
print('Number of vowels=', v)
print('Number of consonants=', c)
print('Is the string palindrome?=', p)