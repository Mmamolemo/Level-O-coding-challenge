def time(nums):
    
    number = nums
    hours = 0
    minutes= 0
    
    if number < 59:
        minutes = number
        if minutes == 1:
            print(minutes, 'minute')
        elif (minutes == 0 or minutes > 1):
            print(minutes, 'minutes')
            
    elif number > 59:
        hours = number//60
        minutes = number - (hours * 60)
        
        print(hours, 'hour,', minutes, 'minutes')
   
time()
