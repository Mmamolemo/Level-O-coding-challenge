def maximum_number(num1,num2,num3):
    
    number_list = [num1, num2, num3]
    
    max_num = max_num = number_list[0]

    
    for number in number_list:
        if number > max_num:
            max_num = number
            
    return max_num


        
