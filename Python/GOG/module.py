from math import fabs
from kilo import hello

hello()

def main():
    num = float (input ("Enter the num: "))
    #fabs is used to get absolute value will only result a float value
    #abs will return appropriate value say integer as integer or float as float
    num = fabs (num)˜
    print (num)

if __name__=="__main__":
    main()