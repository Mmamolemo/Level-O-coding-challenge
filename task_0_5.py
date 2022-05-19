def area_of_traingle(side1,side2,side3):
     semiperemeter = (side1+side2+side3)/2
     area = (semiperemeter*(semiperemeter-side1)*(semiperemeter-side2)*(semiperemeter-side3)) ** 0.5
     return area
