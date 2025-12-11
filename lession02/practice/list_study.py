# numbers = [1,2,3,4,5]
# mixed = [1, 'hello', 1.3, True]
# empty = []

# colors = ["red", "green", "blue"]
# print("green" in colors) # True
# print("yellow" in colors) # False

# nums = [4, 7, 1, 9]
# print(len(nums)) # số phần tử
# print(sum(nums)) # tổng
# print(sorted(nums)) # trả về list mới đã sort
# print(nums)

# nums = [4, 7, 1, 9]
#
# for x in nums:
#     print(x)
#
# for i in range(len(nums)):
#     print(i, nums[i])
#
# for i, value in enumerate(nums, start=1):
#     print(i, value)

# students = ["A", "B", "C", "D"]
# math = [9.0, 7.5, 8.0]
# english = [8.5, 6.0, 9.0]
#
# for s, m, e in zip(students, math, english):
#     print(s, m, e)

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Cách truyền thống
# new_list = []
# for n in nums:
#     new_list.append(n + 1)

# # Tăng mỗi số lên 1
# new_list = [n + 1 for n in nums]
# print(new_list)

# # Lọc phần tử theo điều kiện
# evens = [x for x in nums if x % 2 == 0]
# print(evens) # [0, 2, 4, 6, 8]

# # Nested list comprehension
# pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
# print(pairs) # [(1, 3), (1, 4), (2, 3), (2, 4)]
# a = [1, 2, 3]
# b = a
# b[0] = 100
# print(a) # bị thay đổi theo!
#
# # hoặc
# b = a.copy()
# # Copy đúng cách
# b = a[:]

a = [1, 2, 3, 4]
for x in a:
    a.remove(x) # gây lỗi logic

a = [1, 2, 3, 4]
for x in a[:]: # dùng bản copy
    a.remove(x)

