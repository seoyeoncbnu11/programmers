def solution(n):
    my_list = []
    for i in range(1, n+1):
        if i % 2 == 0:
            my_list.append(i)
    answer = sum(my_list)
    return answer
