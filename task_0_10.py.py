def common(str1,str2):
    same = []

    i = 0
    if len(str1) >= len(str2):
        while i < len(str1):
            j = 0
            while j < len(str2):
                if str1[i] == str2[j]:
                    same += str1[i]
                j = j + 1
            i = i + 1

        return same
    else:
        while i < len(str2):
            j = 0
            while j < len(str1):
                if str2[i] == str1[j]:
                    same += str2[i]
                j = j + 1
            i = i + 1

    return same

print(common('house','computers'))
    
