def solution(n):
    answer = 0
    my_string = str(n)
    for i in my_string:
        answer += int(i)
    return answer
