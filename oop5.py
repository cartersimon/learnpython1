# Put static methods into a class to keep them together and so that they can easily be reused

class Math:
    
    @staticmethod
    def add5(x):      # no need for "self" or "cls" as not acting on an object (they don't have access), just runs as a function
        return x + 5 

print(Math.add5(4))