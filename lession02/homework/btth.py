# ### BTTH1: Cho list điểm `scores = [7.5, 8.0, 6.5, 9.0, 8.5]
# scores = [7.5, 8.0, 6.5, 9.0, 8.5]
#
# avgN = 0
# maxN = scores[0]
# minN = scores[0]
# sumN = 0
#
# for score in scores:
#     sumN += score
#     if minN > score:
#         minN = score
#     if maxN < score:
#         maxN = score
#
# avgN = sumN / len(scores)
# print(f"AVG: {avgN}, MIN: {minN}, MAX: {maxN}")
#
# avgN = sum(scores) / len(scores)
# maxN = max(scores)
# minN = min(scores)
# print(f"AVG: {avgN}, MIN: {minN}, MAX: {maxN}")
######################################################################
# #### BTTH2: Xóa tất cả số âm khỏi list
#
# nums = [5, -2, 8, -1, 0, 3, -10]
#
# newArr = [num for num in nums if num >= 0]
#
# print(newArr)
#
#######################################################################
# #### BTTH3: Làm phẳng list lồng nhau
# matrix = [[1,2,3],[4,5],[6]]
#
# newArr = []
#
# for arr in matrix:
#     for num in arr:
#         newArr.append(num)
#
# print(newArr)
#
# newArr = [x for sub in matrix for x in sub]
# print(newArr)
######################################################################
#### BTTH4: Unpacking tuple
# student_info = ("Nguyen Van A", 20, "Python Core")
#
# name, age, course = student_info
#
# print(f"name: {name}, age: {age}, course: {course}")
######################################################################
#### BTTH5: Hàm trả về nhiều giá trị
# scores = [7.5, 8.0, 6.5, 9.0, 8.5]
#
# def calculate_status(your_list: list[float]) -> tuple[float, float, float]:
#     max_value = your_list[0]
#     min_value = your_list[0]
#     sum_value = 0
#
#     for score in your_list:
#         sum_value += score
#         if min_value > score:
#             min_value = score
#         if max_value < score:
#             max_value = score
#
#     avg_value = sum_value / len(your_list)
#     return avg_value, min_value, max_value
#
# new_list = calculate_status(scores)
# print(new_list)
######################################################################

#### BTTH6: Danh sách học viên (Kết hợp list + tuple)
# students = [
#     ("Nguyen Van A", 20, 8.5),
#     ("Tran Thi B", 19, 7.0),
#     ("Le Van C", 21, 9.0),
# ]
# ## a
# for student in students:
#     name, age, score = student
#     print(f"name: {name}, age: {age}, score: {score}")
#
# ## b
# scores = [student[2] for student in students]
# print(scores)
#
# ## c
# max_score = students[0][2]
#
# for student in students:
#     if max_score < student[2]:
#         max_score = student[2]
#
# print(max_score)

######################################################################
# #### BTTH7: Thông tin sinh viên
# from typing import Any
#
# student: dict[str, Any] = {
#     "name": "Nguyen Van A",
#     "age": 20,
#     "scores": [7.5, 8.0, 6.5, 9.0],
# }
#
# for key in student:
#     print(f"{key} : {student.get(key)}")
#
#######################################################################
# #### BTTH8: Đếm tần suất xuất hiện ký tự
# s = "hello world"
#
# newDict = {}
#
# for character in s:
#     if character not in newDict:
#         newDict[character] = 1
#     else:
#         newDict[character] += 1
#
# print(newDict)
#######################################################################
# #### BTTH9: Quản lý danh sách sinh viên bằng dict
#
# from typing import Any
#
# students: dict[str, dict[str, Any]] = {
#     "SV01": {"name": "Nguyen Van A", "age": 20},
#     "SV02": {"name": "Tran Thi B", "age": 21},
# }
#
# newStudent = {"name": "vinh", "age": 22}
#
# students['SV03'] = newStudent
# students['SV01']['age'] += 1
#
# for student_id, info in students.items():
#     print(f"{student_id} : {info}")

#######################################################################

### BTTH10: Loại bỏ trùng lặp trong list

# nums = [1, 2, 2, 3, 4, 4, -1, 5]
#
# unique_nums = sorted(set(nums), reverse=True)
# print(unique_nums)

#######################################################################

### BTTH11: Kiểm tra phần tử thuộc tập cho phép

# allowed_roles = {"admin", "editor", "viewer"}
# user_role = input("Nhap role nguoi dung: ")
#
# if user_role in allowed_roles:
#     print("Hop le")
# else:
#     print("Khong hop le")

#######################################################################

### BTTH12: Phân tích học viên giữa 2 lớp

# class_A = {"SV01", "SV02", "SV03", "SV04"}
# class_B = {"SV03", "SV04", "SV05"}
#
# ## a. Tìm học viên học cả 2 lớp (giao)
# print(class_A & class_B)
#
# ## b. Tìm học viên chỉ học lớp A (hiệu)
# print(class_A - class_B)
#
# ## c. Tìm tất cả học viên (hợp) của 2 lớp
# print(class_A | class_B)
#
# ## d. Tìm học viên chỉ học 1 trong 2 lớp (hiệu đối xứng)
# print(class_A ^ class_B)
