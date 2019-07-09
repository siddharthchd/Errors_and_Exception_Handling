def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number : "))
        except:
            print("Whoops! That is not a number.")
            continue
        else:
            print("Yes, Thank You")
            break
        finally:
            print('End of try - except - finally')

ask_for_int()