

import warnings

MUTABLE = ['radius']
IMMUTABLE = ['diameter', 'circumference', 'area']

class Circle:
    pi = 3.1415
    
    def __init__(self, r):
        self.radius = r
        
    def diameter(self):
        return self.radius * 2
    
    def circumference(self):
        return self.radius * self.pi * 2
    
    def area(self):
        return (self.radius ** 2) * self.pi
    
    def __setattr__(self, name, value):
        if name in IMMUTABLE:
            warnings.warn("불가")
        return super().__setattr__(name, value)
    
    # __delattr__ 추가
    

c = Circle(10)
print(c.radius)
print(c.diameter())
c.radius = 100
c.area = 123
