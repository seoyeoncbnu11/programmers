def solution(numbers):
    num_list = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            num_list.append(numbers[i] * numbers[j])

    answer = max(num_list)

    return answer
