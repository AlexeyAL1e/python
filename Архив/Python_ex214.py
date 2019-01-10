import statistics
nums = [1, 5, 33, 12, 46, 33, 2]

# среднее
p = statistics.mean(nums)

# медиана
b = statistics.median(nums)

# мода
v = statistics.mode(nums)

print(p)
print(b)
print(v)
