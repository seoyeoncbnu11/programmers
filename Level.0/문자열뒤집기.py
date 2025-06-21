def solution(my_string):
    answer = ''
    my_list = list(my_string)
    my_list = my_list[::-1]
    answer = "".join(my_list)
    return answer