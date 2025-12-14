from lession03.homework.bai_tap_2.student import Student

def load_student_from_file(file_name: str) -> list[Student]:
    student_list = []
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            lines = f.readlines()
            is_title = True
            for line in lines:
                if line.strip():
                    if is_title:
                        is_title = False
                        continue
                    info_line = line.strip("\n").split(",")
                    try:
                        student = Student(info_line[0], int(info_line[1]), float(info_line[2]))
                        student_list.append(student)
                    except ValueError:
                        print(f"Không thể parse {info_line} thành thông tin của student do sai dữ liệu")
                    except IndexError:
                        print(f"Không thể parse {info_line} thành thông tin của student do thiếu dữ liệu")

        # print(student_list)
    except FileNotFoundError:
        print("File không tồn tại")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

    return student_list

def calc_avg_score(students: list[Student]) -> float:
    if len(students) < 1:
        return 0

    sum_score = 0
    for student in students:
       sum_score += student.score
    return sum_score / len(students)

def find_top_student(students: list[Student]) -> Student | None:
    if len(students) < 1:
        return None

    top_student = students[0]
    for student in students[2:]:
        if top_student.score < student.score:
            top_student = student
    return top_student


def filter_failed(students: list[Student]) -> list[Student]:
    fail_students = []

    for student in students:
        if not student.is_passed():
            fail_students.append(student)

    return fail_students