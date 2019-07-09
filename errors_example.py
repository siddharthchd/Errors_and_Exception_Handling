try:
    f = open('testfile', 'r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except IOError: # or just except:
    print("Hey you have an IO error")
finally:
    print('This block is always executed')