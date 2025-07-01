def solution(price):
    answer = price
    if price >= 100000:
        answer = price - (price * 5 / 100)
    if price >= 300000:
        answer = price - (price * 10 / 100)
    if price >= 500000:
        answer = price - (price * 20 / 100)

    return int(answer)
