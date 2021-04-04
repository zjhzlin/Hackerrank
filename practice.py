def list_comprehension(x,y,z,n):
    new_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(new_list)

def runner_up_score(list):
    list_sorted = sorted(list)
    max = list_sorted[-1]
    index = -2
    next = list_sorted[index]
    while next == max:
        index -= 1
        next = list_sorted[index]
    runner_up_score = next
    return runner_up_score


if __name__ == '__main__':
    # n = 24
    # n = int(input())
    #
    # if n%2 == 1:
    #     print('Weird')
    # else:
    #     if 5 >= n >= 2 or n > 20:
    #         print('Not Weird')
    #     elif 20 >= n >= 6:
    #         print('Weird')

    a=4
    b=3
    print(a//b)   # The result of the integer division
    print(a/b)

    list_comprehension(1,1,2,3)

    print(runner_up_score([2,3,6,6,5]))