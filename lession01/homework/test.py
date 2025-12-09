# is_leap_year = False
# is_30_day = None
# is_february = False
#
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     is_leap_year = True
#
# match (month):
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#         is_30_day = False
#     case 4 | 6 | 9 | 11:
#         is_30_day = True
#     case 2:
#         is_february = True
# if day == 1:
#     if is_30_day is not None:
#         if is_30_day:
