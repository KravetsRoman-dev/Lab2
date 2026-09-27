import math


def area(r: float) -> float:
    ''' 
    Возращает площадь круга по заданному радиусу.
       
    Параметры:
        r(float) - радиус круга
    
    Возращаемое значение:
        (float) - площадь круга
     
    '''
    return math.pi * r * r


def perimeter(r: float) -> float:
    ''' 
    Возращает периметр круга по заданному радиусу.
           
    Параметры:
        r(float) - радиус круга
        
    Возращаемое значение:
        (float) - периметр круга
         
    '''
    return 2 * math.pi * r