### Bài tập 3: To-do List theo ngày với DateTime + File + OOP + Exception

from lession03.homework.bai_tap_3.task_service import load_tasks, check_all_tasks, check_overdue_tasks, save_tasks, \
    mark_task_done


def display_menu() -> None:
    file_name = input("Nhập tên file: ")

    exit_flag = False
    while not exit_flag:

        task_list = load_tasks(file_name)
        if len(task_list) == 0:
            file_name = input("Danh sách trống, Xin mời nhập lại: ")
            continue



        print("""
===============================
1. Xem tất cả task
2. Xem các task quá hạn
3. Thêm task mới
4. Đánh dấu task là done
5. Thoát
===============================
    """)

        try:
            choice = int(input("Lựa chọn: "))
            if choice not in range(1, 6):
                print("Lựa chọn không hợp lệ")
                continue
            match choice:
                case 1:
                    print("1. Xem tất cả task")
                    check_all_tasks(task_list)
                case 2:
                    print("2. Xem các task quá hạn")
                    check_overdue_tasks(task_list)
                case 3:
                    print("3. Thêm task mới")
                    save_tasks(file_name, task_list)
                case 4:
                    print("4. Đánh dấu task là done")
                    mark_task_done(file_name, task_list)
                case 5:
                    print("5. Thoát")
                    exit_flag = True
        except ValueError:
            print("Lựa chọn không hợp lệ")

#  tasks.txt

display_menu()