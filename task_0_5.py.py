def area_of_traingle(a,b,c):
     semiperemeter = (a+b+c)/2
     area = (semiperemeter*(semiperemeter-a)*(semiperemeter-b)*(semiperemeter-c)) ** 0.5
     return area
