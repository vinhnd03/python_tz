## BTTH1 – Bắt lỗi nhập số
loop = True

while loop:
    try:
        number = int(input("Nhập số: "))
        if number < 0:
            print("Nhập sai, vui lòng nhập lại")
            continue
        print(f"Bạn đã nhập: {number}")
        loop = False
    except ValueError:
        print("Nhập sai, vui lòng nhập lại")

### BTTH2 – Tạo menu và xử lý lỗi lựa chọn
menu = """
    1. Xin chào
    2. Tính chỉ số BMI
    3. Thoát
"""
loop = True

while loop:
    try:
        print(menu)
        choose = int(input("Lựa chọn: "))


    except ValueError:
        print("Lựa chọn không hợp lệ")

