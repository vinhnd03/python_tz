from datetime import datetime

from lession03.homework.bai_tap_3.task import Task


def load_tasks(file_name: str) -> list[Task]:
    task_list = []
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            lines = f.readlines()
            is_title = True
            for line in lines:
                if line.strip():
                    if is_title:
                        is_title = False
                        continue
                    info_line = line.strip("\n").split(";")
                    try:
                        due_date = datetime.strptime(info_line[1], "%Y-%m-%d")
                        task = Task(info_line[0], due_date, info_line[2])
                        task_list.append(task)
                    except ValueError:
                        print(f"Không thể parse {info_line} thành thông tin của task do sai dữ liệu")
                    except IndexError:
                        print(f"Không thể parse {info_line} thành thông tin của task do thiếu dữ liệu")

    except FileNotFoundError:
        print("File không tồn tại")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

    return task_list

def write_tasks (file_name: str, tasks: list[Task]) -> None:
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("Mô tả;YYYY-MM-DD;trạng_thái\n")
        for task in tasks:
            task_str = f"{task.description};{task.due_date.strftime("%Y-%m-%d")};{task.status}"
            f.write(task_str + "\n")

def check_all_tasks(task_list: list[Task]) -> None:
    for task in task_list:
        print(task.__str__())

def check_overdue_tasks(task_list: list[Task]) -> None:
    for task in task_list:
        if task.is_overdue():
            print(task.__str__())

def save_tasks(file_name: str, tasks: list[Task]) -> None:
    try:
        desc = input("Nhập mô tả: ")
        date_str = input("Nhập hạn (YYYY-MM-DD): ")
        due_date = datetime.strptime(date_str, "%Y-%m-%d")
        tasks.append(Task(desc, due_date, "todo"))
        write_tasks(file_name, tasks)
        print("Lưu task thành công")
    except ValueError:
        print(f"Sai định dạng ngày YYYY-MM-DD")
    except FileNotFoundError:
        print(f"Không tìm thấy file")


def mark_task_done(file_name:str, tasks: list[Task]) -> None:
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task.__str__()}")

    try:
        select_task = int(input("Nhập task muốn đánh dấu [done]: "))
        if select_task < 1 or select_task > len(tasks) + 1:
            print("không có task yêu cầu")
            return

        tasks[select_task-1].status = "done"
        write_tasks(file_name, tasks)
        print("Cập nhật thành công")
    except ValueError:
        print("Lựa chọn không hợp lệ")


# check_all_tasks(load_tasks("tasks.txt"))
# check_overdue_tasks(load_tasks("tasks.txt"))
# save_tasks("tasks.txt", load_tasks("tasks.txt"))
# mark_task_done("tasks.txt", load_tasks("tasks.txt"))