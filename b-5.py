str_numbers = input("データを入力してください(スペース区切り) ").split()
numbers = list(map(int, str_numbers))


def sum_value(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def max_value(numbers):
    max_candidate = -10000
    for n in numbers:
        if max_candidate < n:
            max_candidate = n
    if max_candidate == -10000:
        print("You're irregular!")
    else:
        return max_candidate


def min_value(numbers):
    min_candidate = 10 * 10
    for n in numbers:
        if min_candidate > n:
            min_candidate = n
    if min_candidate == 10 * 10:
        print("You're irregular!")
        return None
    else:
        return min_candidate


def mean_value(numbers):
    total = 0
    for n in numbers:
        total += n
    return sum_value(numbers) / len(numbers)


print(f"合計値: {sum_value(numbers)}")
print(f"最大値: {max_value(numbers)}")
print(f"最小値: {min_value(numbers)}")
print(f"平均値: {mean_value(numbers)}")
