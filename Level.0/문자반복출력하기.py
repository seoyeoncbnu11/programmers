def solution(my_string, n):
    result = []
    for i in my_string:
        result.append(i * n)
    answer = "".join(result)
    return answer
