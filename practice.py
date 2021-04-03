if __name__ == '__main__':
    n = 24
    # n = int(input())

    if n%2 == 1:
        print('Weird')
    else:
        if 5 >= n >= 2 or n > 20:
            print('Not Weird')
        elif 20 >= n >= 6:
            print('Weird')

    a=4
    b=3
    print(a+b)
    print(a-b)
    print(a*b)

    print(a//b)   # The result of the integer division
    print(a/b)