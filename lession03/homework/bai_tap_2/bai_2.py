### Bài tập 2: Quản lý điểm sinh viên với File I/O + OOP + Exception
from lession03.homework.bai_tap_2.student_service import load_student_from_file, find_top_student, calc_avg_score, filter_failed

#  students.txt
file = input('Nhập tên file: ')

student_list = load_student_from_file(file)

print([str(student) for student in student_list])

print(f'Điểm trung bình của lớp là: {calc_avg_score(student_list)}')

print(f"Sinh viên có điểm cao nhất là: {str(find_top_student(student_list))}")

print(f"Danh sách sinh viên bị rớt là: {[str(student) for student in filter_failed(student_list)]}")



