# Дан список целых чисел. Найти второе по величине число в списке.
# Дано:
# numbers = [15, 7, 28, 10, 21]
# Результат:
# 21
# Дано:
# numbers = [4, 6, 2, 11, 1, 11, 5]
# Результат:
# 6


# Решение:
# numbers = [15, 7, 28, 10, 21]

# a = max(numbers)
# b = 0
# for number in numbers:
    # if b < number < a:
        # b = number
# print(b)


# альтернативный вариант для 2 примера

numbers = [15, 7, 28, 10, 21]
numbers.sort()
print(numbers[-2])

# numbers = [4, 6, 2, 11, 1, 11, 5]
# numbers.sort()
# print(numbers[-2])