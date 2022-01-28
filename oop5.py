class Math:
    
    @staticmethod
    def add5(x):      # no need for "self" as not acting on an object, just running the function
        return x + 5 


print(Math.add5(4))