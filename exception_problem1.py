try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("Type mismatch")
finally:
    print('An error occurred during execution')