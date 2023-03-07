#3 is good, 5 is better, 15 is the best
def solution(numbers):
    good = []
    better = []
    best = []
    for i in numbers:
        if i % 15 == 0:
            best.append(i)
            continue
        if i % 3 == 0:
            good.append(i)
        if i % 5 == 0:
            better.append(i)
    return best, better, good
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(solution(numbers))