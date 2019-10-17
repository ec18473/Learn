def solution(A):
    # write your code in Python 3.6

    length = len(A)
    res = []

    summ = 0
    for elem in A:
        if elem>0:
            # # tuple = (A.index(elem),A.index(elem))
            # # print(A.index(elem),A.index(elem))
            # tup = (A.index(elem),A.index(elem))
            # res.append(tup)
            pass
        else:
            duple = (A.index(elem)-2,A.index(elem)-1)
            tup = (A.index(elem)-2,A.index(elem)-1)
            res.append(tup)



    print(res)

    for elem in res:
        elem = tuple(elem)



        temp = A[elem[0]] + A[elem[1]]
        print(temp)

        if temp > summ:
            summ = temp

    return summ

    # return summ






    pass





A = [1,2,-3,4,5,-6]

B = [-8,3,0,5,-3,12]

print(solution(B))
# print(solution(B))

