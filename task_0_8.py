def time(numbers):
    number = int(input)
    hours = 0
    minutes= 0
    if number < 59:
        minutes = number
        if minutes == 1:
            print(minutes, ' minute')
        elif (minutes == 0 or minutes > 1):
            print(minutes, ' minutes')
            
    elif number > 59:
        hours = number//60
        minutes = number - (hours * 60)
        
        if hours == 1 and minutes == 0:
            print(hours, ' hour, ', minutes, ' minutes')
        elif hours == 1 and minutes == 1:
            print(hours, ' hour, ', minutes, ' minute')
        elif hours > 1 and minutes == 1:
            print(hours, ' hours, ', minutes, ' minute')
        elif hours == 1 and minutes > 1:
            print(hours, ' hour, ', minutes, ' minutes')
        else:
            print(hours, ' hours, ', minutes, ' minutes')

time()
