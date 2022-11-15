#WAP togenerate the series of square a number for the given i/p lst =[1,2,3,4].

from secrets import choice
from time import time


def func(lst):
     for i in lst:
         yield i**2
         
if __name__ == '__main__':
     lst = [1,2,3,4]

     g = func(lst)
     print(next(g))
     print(next(g))
     print(next(g))
     print(next(g))


#WAP to generate the random password from the alphabets.


def string_generator():

    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    while True:
        name = ''
        for i in range(6):
            name = name+choice(alphabets)
            yield name

for i in string_generator():
    time.sleep(2)
    print(i)

