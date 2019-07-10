try:
    x = 5
    y = 0
    z = x/y

except ZeroDivisionError:
    print('You cannot divide a number by 0')
finally:
    print('All done')