#Write a program that will calculate two quadratic equations (6x² + 11x - 35 = 0. and 5x² - 2x - 9 = 0.)
 # at the same time, set all the parameters of the equation in variables. (multiprocessing)
#import threading
import threading
import math


def equations(a, b, c):
    dis = (b ** 2) - (4 * a * c)

    if dis > 0:
        firstValue = (-b - math.sqrt(dis)) / (2 * a)
        secondValue = (-b + math.sqrt(dis)) / (2 * a)
        print(f'Result: {firstValue} and {secondValue}')
    elif dis == 0:
        firstValue = secondValue = -b / (2 * a)
        print(f'Result: {firstValue} and {secondValue}')
    elif dis < 0:
        firstValue = ((-1) * b + math.sqrt(dis))
        secondValue = ((-1) * b - math.sqrt(dis))
        print(f'Result: {firstValue} and {secondValue}')



thread1 = threading.Thread(target=equations(6, 11, -35))
thread2 = threading.Thread(target=equations(5, -2, -9))

thread1.start()
thread2.start()