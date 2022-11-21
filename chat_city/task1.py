# 75521545
import sys


def solution(street, houses):
    """
    Принимает строку с количеством домов и строку номеров домов через
    пробел. Возвращает строку с расстояниями всех домов до ближайших пустых
    участков через пробел.
    """
    result = []
    street = int(street)
    houses = list(map(int, houses.split()))

    zero_indxs = [i for i, v in enumerate(houses) if v == 0]
    first_zero = zero_indxs[0]
    zeroes_len = len(zero_indxs)

    if zeroes_len == 1:
        result = [abs(first_zero - i) for i, v in enumerate(houses)]
        return ' '.join(map(str, result))

    if first_zero != 0:
        result = [(first_zero - i) for i, v in enumerate(houses[:first_zero])]

    for i in range(zeroes_len - 1):
        left = zero_indxs[i]
        right = zero_indxs[i + 1]

        result.append(0)
        for j in range(left + 1, right):
            house_to_left = j - left
            house_to_right = right - j
            if house_to_left <= house_to_right:
                result.append(house_to_left)
            else:
                result.append(house_to_right)

        if zeroes_len == i + 2:
            result.append(0)

    last_zero = zero_indxs[zeroes_len - 1]
    if last_zero != street - 1:
        result = result + [(i - last_zero) for i, v in enumerate(
                            houses[last_zero+1:], start=last_zero+1)]

    return ' '.join(map(str, result))


if __name__ == '__main__':
    street = input()
    houses = sys.stdin.readline()
    result = solution(street, houses)
    print(result)
