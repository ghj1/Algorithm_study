a = 70
first = 10
def func(x,y):
    try:
        third =  x + y
        return third
    except ZeroDivisionError:
        third = a
        pass

def func_02(x,y):
    try:
        fir = x * y
        sec = x / y
        return fir, sec
    except ZeroDivisionError:
        third = first
        pass

if __name__ == '__main__':
    print(func(50,20))
    print(func_02(10,0))
    try:
        pass
    except Exception as e:
        pass