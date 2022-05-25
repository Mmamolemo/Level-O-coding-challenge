def check_vowels(words):
    vowels = "aeiou"
    final = []
    words = words.lower()
    for vowel in words:
        if vowel in vowels:
            final += vowel

    final = list(dict.fromkeys(final))    
    name = ', '.join(final)      
    print("Vowels:",name)
check_vowels("UMUZI")


