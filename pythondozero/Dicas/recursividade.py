print('recursiva')

num = 0
def autoIncremento(num):

    print(num)

    num += 1

    if (num < 10):
        return autoIncremento(num)

    return 

autoIncremento(num)

