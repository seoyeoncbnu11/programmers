def solution(my_string):
    answer = ""
    vowel = ["a", "e", "i", "o", "u"]

    for i in my_string:
        flag = False
        for v in vowel:
            if i == v:
                flag = True
                break
        if flag == False:
            answer += i
