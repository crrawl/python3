from datetime import datetime

def timer(function):
    """return execution time of the function"""
    def inner():
        
        before = datetime.now()
        result = function()
        print(datetime.now() - before)

        return result
    return inner

@timer
def eval():
    return [n for n in range(10000) if n % 2 == 0]


print(eval())