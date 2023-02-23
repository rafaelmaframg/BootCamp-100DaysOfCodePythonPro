import time

def delay_decorator(function):
    def delayed_function():
        time.sleep(2)
        function()
    return delayed_function


@delay_decorator
def hello():
    print("hello")

def grettings():
    print("gretttings")

#explained
suggar = delay_decorator(grettings)





if __name__ == "__main__":
    suggar()