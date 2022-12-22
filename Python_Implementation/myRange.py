"""
General Idea:
In python2, range generated a list of values we require and this could lead to 
huge amount of memory usage. In python3 this is solved but I want to re-implement
myself. 
This MyRange class are using generator function to ensure the integer in the
range we required are returned one by one. 
First it checked the start parameter when we initialize the class.
After that we will check if stop parameter exists. If not, the default range is (0, start)
If s

"""
### Using generator functions for a more complete range() re-implementation:
class MyRange():
    def __init__(self, start: int, stop=None, step=None):
        if stop is None:
            # if not isinstance(start, int):
            #     raise TypeError("'" + start.__class__.__name__ + "' object cannot be interpreted as an integer")
            self.start = 0
            self.stop = start
            self.step = 1
        elif step is None:
            if not isinstance(stop, int):
                raise TypeError("'" + stop.__class__.__name__ + "' object cannot be interpreted as an integer")
            self.start = start
            self.stop = stop
            self.step = 1
        else:
            if not isinstance(stop, int):
                raise TypeError("'" + stop.__class__.__name__ + "' object cannot be interpreted as an integer")
            if not isinstance(step, int):
                raise TypeError("'" + step.__class__.__name__ + "' object cannot be interpreted as an integer")
            if step == 0:
                raise ValueError('MyRange() arg 3 must not be zero')
            self.start = start
            self.stop = stop
            self.step = step
            # if (
            #     (self.step > 0 and self.start > self.stop) 
            #     or (self.step < 0 and self.start < self.stop)
            # ):
            #     raise ValueError('MyRange(' + self.start + ',' + self.stop + ')' + "is not valid value")
        
        i = self.start
        if self.step > 0:  # step arg is increasing
            while i < self.stop:
                yield i
                i += self.step
            return
        elif self.step < 0:  # step arg is decreasing
            while i > self.stop:
                yield i
                i += self.step  # Adding a negative to decrease
            return