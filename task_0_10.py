def common(str1,str2):
    same = []
    str1, str2 = str1.lower(), str2.lower()

    letter = 0
    if len(str1) >= len(str2):
        while letter < len(str1):
            letters = 0
            while letters < len(str2):
                if str1[letter] == str2[letters]:
                    same += str1[letter]
                letters = letters + 1
            letter = letter + 1
            same = list(dict.fromkeys(same))
            name = ', '.join(same).lower()
    else:
        while letter < len(str2):
            letters = 0
            while letters < len(str1):
                if str2[letter] == str1[letters]:
                    same += str2[letter]
                letters = letters + 1
            letter = letter + 1
    same = list(dict.fromkeys(same))
    name = ', '.join(same).lower()
    print("Common letters:",name)






