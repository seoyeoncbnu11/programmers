def solution(num_list):
    multiple = 1
    add = 0
    for i in num_list:
        multiple *= i
        add += i
    if multiple < add**2:
        answer = 1
    else:
        answer = 0
    return answer
