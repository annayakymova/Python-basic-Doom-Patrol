#2*. Rewrite the decorator "logger" from fifth task to use Class instead of function and without passing args to decorator.

import time
from datetime import datetime


# homework use Class instead of function and without passing args to decorator

class Logger:
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        log = f'{func.__name__} with was executed at {datetime.now()}\n'
        print(log)
        with open(self.logfile, 'a') as file:
            file.write(log)


@Logger()
def my_func():
    """
    This is my func
    """
    print(f"{my_func().__name__} is running")


log = Logger()