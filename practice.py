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

import numpy

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
    #
    # a=4
    # b=3
    # print(a//b)   # The result of the integer division
    # print(a/b)
    #
    # list_comprehension(1,1,2,3)
    #
    # print(runner_up_score([2,3,6,6,5]))
    #
    # a=4
    # b=3
    # print(a//b)   # The result of the integer division
    # print(a/b)
    #
    # list_comprehension(1,1,2,3)
    #
    # print(runner_up_score([2,3,6,6,5]))

    # nested list
    N=5
    names = ['Harry','Berry', 'Tina', 'Akriti', 'Harsh']
    scores = [37.21, 37.21, 37.2, 41, 39]
    lists = []
    for i in range(N):
        name = names[i]
        score = scores[i]
        lists.append([name, score])

    sorted_scores = sorted(scores)
    print(sorted(scores))
    min_score = sorted_scores[0]
    for i in range(N):
        if sorted_scores[i] > min_score:
            second_score = sorted_scores[i]
            break
    print(second_score)

    second_name =[]
    for i in range(N):
        if lists[i][1] == second_score:
            second_name.append(lists[i][0])
    print(sorted(second_name))

    # finding the percentage
    student_marks = {'Krishna':[67,68,69],'Arjun':[70,98,63],'Malika':[52,56,60]}
    mark = student_marks['Malika']
    sum = 0
    for i in range(len(mark)):
        sum += mark[i]
    average = sum/len(mark)
    print('{:.2f}'.format(average))

    # min and max - array

    # N, M = map(int, raw_input().split())
    # my_array = numpy.array([map(int, raw_input().split()) for i in range(N)])

    n=4
    m=2
    my_array = numpy.array([[2,5],[3,7],[1,3],[4,0]])
    min_axis1 = numpy.min(my_array, axis=1)
    print(max(min_axis1))
    print(my_array)


    #