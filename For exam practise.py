def analyze_string(s):
    vowels = 0
    consonants = 0

    for ch in s.lower():
        if ch.isalpha():
            if ch in 'aeiou':
                vowels += 1
            else:
                consonants+=1
    cleaned="".join(ch.lower() for ch in s if ch.isalnum())
    if cleaned==cleaned[::-1]:
        palindrome='Yes'
    else:
        palindrome='No'
    return vowels, consonants, palindrome

text=input('Enter a number:')
v, c, p=analyze_string(text)
print('Vowels=', v)
print('Consonants=', c)
print('Is palindrome=', p)