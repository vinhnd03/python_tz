#### BTTH1: Kiểm tra tuổi

# age = int(input("Nhập tuổi: "))
#
# if age < 11:
#     print("Trẻ con")
# elif age < 17:
#     print("Thiếu niên")
# elif age < 30:
#     print("Thanh niên")
# else:
#     print("Người già")


#### BTTH2: Kiểm tra chẵn lẻ - Dùng toán tử 3 ngôi

# numb = int(input("Nhập 1 số: "))
#
# result = "Even" if (numb%2==0) else "Odd"
# print(result)


#### BTTH3: Kiểm tra năm nhuận

# year = int(input("Nhập năm: "))
#
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} là năm nhuận")
# else:
#     print(f"{year} không phải là năm nhuận")


#### BTTH4: Tính tổng từ 1 đến n

# num = int(input("Nhập 1 số: "))
# result = 0
# while num > 0:
#     result += num
#     num -= 1
# print(result)


#### BTTH5: Đếm số ký tự 'a' trong chuỗi

# str1 = input("Nhập một chuỗi: ")
# cnt = 0
#
# for character in str1:
#     if character.lower() == 'a':
#         cnt+=1
# print(cnt)


#### BTTH6: In các hình sau

# 6a. Hình chữ nhật rỗng
# row, col = 5, 6
# for i in range(row):
#     for j in range(col):
#         if j == 0 or j == col-1 or i == 0 or i == row-1:
#             print('*', end=" ")
#         else:
#             print(" ", end=" ")
#     print("")

# 6b. Hình tam giác vuông cân
# for i in range(6):
#     for j in range(i):
#         if j <= i:
#             print("*", end=" ");
#         else:
#             break
#     print()

