import time
 
def timer(func):
    def inner():
        start=time.time()
        func()
        end=time.time()
        diff=end-start
        print("The execution time is ",diff)
    return inner

@timer
def my_fuction():
    a=89+78
    time.sleep(2)

my_fuction()