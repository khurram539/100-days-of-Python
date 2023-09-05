def add(**args):
    print(args[1])
    
    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(3, 5, 6, 7, 8, 9, 10))

def calucate(**kwargs):
    print(kwargs)
    # for ket, value in kwargs.items():
    #     print(key)
    #     print(value)

    print(kwargs["add"])



