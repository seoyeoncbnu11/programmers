def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer = answer + i
        if answer > n:
            return answer
