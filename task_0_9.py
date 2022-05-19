vowels = "aeiou"

def checkVowels(words):
    final = []
    for vowel in words:
        if vowel in vowels:
            final += vowel
            
    print(final)

