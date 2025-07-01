def solution(array, n):
    result = []
    for i in array:
        if i == n:
            result.append(i)
    answer = len(result)

    return answer


# answer = array.count(n)
