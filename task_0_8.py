def time(nums):

    number = nums
    hours = 0
    minutes = 0
    if number < 60:
        minutes = number
        if minutes == 1:
            print(f"0 hours, {minutes} minute")
        elif (minutes == 0 or minutes > 1):
            print(f"0 hours, {minutes} minutes")
        
            
    elif number > 59:
        hours = number//60
        minutes = number - (hours * 60)
        
        if hours == 1 and minutes == 0:
            print(f'{hours} hour, {minutes} minutes')
        elif hours == 1 and minutes == 1:
            print(f'{hours} hour, {minutes} minute')
        elif hours > 1 and minutes == 1:
           print(f'{hours} hour, {minutes} minute')
        elif hours == 1 and minutes > 1:
            print(f'{hours} hour, {minutes} minutes')
        else:
           print(f'{hours} hour, {minutes} minutes')


