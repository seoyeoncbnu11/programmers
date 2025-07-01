def solution(hp):
    a = int(hp // 5)
    b = int(hp % 5)
    c = int(b // 3)
    d = int(b % 3)
    answer = a + c + d

    return answer
