import math
import re


# Bài tập 1: Kiểm tra và tìm ngày kế tiếp, ngày trước đó

def yesterday_and_tomorrow() -> None:
    date = input("Nhập ngày (vd: 12/12/2020): ")

    arr = date.split("/")

    if len(arr) != 3:
        print("Nhập sai định dạng ngày")
        return

    year = int(arr[2])
    month = int(arr[1])
    day = int(arr[0])

    yesterday = ""
    tomorrow = ""

    if day - 1 == 0:
        if month - 1 == 0:
            yesterday = f"30/12/{year - 1}"
        else:
            yesterday = f"30/{month - 1}/{year}"
    else:
        yesterday = f"{day - 1}/{month}/{year}"

    if day + 1 > 30:
        if month + 1 > 12:
            tomorrow = f"1/1/{year + 1}"
        else:
            tomorrow = f"1/{month + 1}/{year}"
    else:
        tomorrow = f"{day + 1}/{month}/{year}"

    print(f"Tomorrow: {tomorrow}, Yesterday: {yesterday}")


# yesterday_and_tomorrow()


# Bài tập 2: Tính tổng S = 1 + 1/3! + 1/5! + ... + 1/(2n−1)!

def find_s() -> None:
    n = int(input("Nhập n: "))
    s = 0
    for i in range(1, n + 1):
        s += (1 / math.factorial(2 * i - 1))

    print(f"S = {s}")


# find_s()


# Bài tập 3: Thao tác chuỗi

def str_prettier() -> None:
    str = input("Nhập chuỗi: ")

    arr = str.split()

    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()


    arr[-1] = re.sub(r"\.+$", "", arr[-1]) + "."

    print(" ".join(arr))


# str_prettier()
