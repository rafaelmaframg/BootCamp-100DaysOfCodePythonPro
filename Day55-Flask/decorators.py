

def logging_decorator(function):
    def log_function(*args):
        return f"you called {function.__name__}{args}\n"\
                f"it returned {function(args[0], args[1])} "

    return log_function


@logging_decorator
def add(num22, num2):
    return num22 + num2

if __name__ == "__main__":
    print(add(2, 4))