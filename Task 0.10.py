def common_character(string1,string2):
    
    cm = []
    
    for a in string1:
        if a in string2:
            cm.append(a)
    return(cm)
