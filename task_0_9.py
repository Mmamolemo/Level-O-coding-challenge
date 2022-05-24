
vowels = "aeiou"

def checkVowels(words):
    final = []
    words = words.lower()
    for vowel in words:
        if vowel in vowels:
            final += vowel

    final = list(dict.fromkeys(final))    
    name = ', '.join(final)      
    print(name)


