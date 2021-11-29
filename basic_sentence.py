first = 10 
second = 0
try:
    third = first / second
    first = 9
except ZeroDivisionError:
    third = first
    pass
except Exception as e:
    pass

print(third)
pass