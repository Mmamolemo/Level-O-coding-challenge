def time():
    x = int(input('Enter a number:'))
    h = 0
    m = 0
    if x < 59:
        m = x
        if m == 1:
            print(m, ' minute')
        elif (m == 0 or m > 1):
            print(m, ' minutes')
            
    elif x > 59:
        h = x//60
        m = x - (h * 60)
        
        if h == 1 and m == 0:
            print(h, ' hour, ', m, ' minutes')
        elif h == 1 and m == 1:
            print(h, ' hour, ', m, ' minute')
        elif h > 1 and m == 1:
            print(h, ' hours, ', m, ' minute')
        elif h == 1 and m > 1:
            print(h, ' hour, ', m, ' minutes')
        else:
            print(h, ' hours, ', m, ' minutes')

time()
