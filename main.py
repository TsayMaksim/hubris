import logging

logging.basicConfig(filename='text.log', level=logging.CRITICAL, format='%(asctime)s || %(levelname)s || %(message)s')


def addition(a: int, b: int) -> dict:
    dict1 = {'addition': a + b}
    return dict1

try:
    print(addition(1, 2))

except NameError:
    print(':(')
    logging.critical('line14')


def subtraction(a: int, b: int) -> dict:
    dict2= {'subtraction': a - b}
    return dict2

try:
    print(subtraction(5, 1))

except NameError:
    print(':(')
    logging.critical('line25')

def multiplication(a: int, b:int) -> dict:
    dict3 = {'multiplication': a * b}
    return dict3

try:
    print(multiplication(2, 3))

except NameError:
    print(':(')
    logging.critical('line35')