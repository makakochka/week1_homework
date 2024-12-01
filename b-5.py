str_numbers = input("データを入力してください(スペース区切り) ").split()
numbers = list(map(int, str_numbers))


def sum_value():
    total = 0
    for n in numbers:
        total += n
    return total


def max_value():
    max_candidate = -10000
    for n in numbers:
        if max_candidate < n:
            max_candidate = n
    if max_candidate == -10000:
        print("You're irregular!")
    else:
        return max_candidate


def min_value():
    min_candidate = 10*10
    for n in numbers:
        if min_candidate > n:
            min_candidate = n
    if min_candidate == 10*10:
        print("You're irregular!")
    else:
        return min_candidate


def mean_value():
    total = 0
    for n in numbers:
        total += n
    return total/len(numbers)


m1 = sum_value()
m2 = max_value()
m3 = min_value()
m4 = mean_value()

print(f"合計値: {m1}")
print(f"最大値: {m2}")
print(f"最小値: {m3}")
print(f"平均値: {m4}")
