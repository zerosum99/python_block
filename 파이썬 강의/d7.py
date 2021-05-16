
import sys
from types import ModuleType


class MyModule(ModuleType):
    def __repr__(self):
        return 'MyModule'
    
    def __setattr__(self, name, value):
        print(name, "세팅 불가")
        
    @staticmethod
    def func(a, b):
        pass
        
def func(a, b):
    pass
        
sys.modules[__name__].__class__ = MyModule
