def solution(n, numlist):
    result = []
    for i in numlist:
        if i % n == 0:
            result.append(i)
    answer = result

    return answer


# for i in numlist:처럼 리스트를 순회하고 있을 땐 그 리스트를 그대로 수정하면 안 됨.
# def solution(n, numlist):
#     for i in numlist:
#         if i%n == 0:
#             continue
#         else:
#             numlist.remove(i)
#             answer = numlist
# return answer (원래 작성한 코드)
