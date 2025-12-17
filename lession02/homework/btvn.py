# # Bài tập 1: Quản lý học viên & khóa học
#
# # Danh sách học viên (list các tuple)
# students = [
#     ("SV01", "Nguyen Van A", 20),
#     ("SV02", "Tran Thi B", 21),
#     ("SV03", "Le Van C", 19),
# ]
# #
# # Dict lưu điểm từng môn cho từng sinh viên
# scores = {
#     "SV01": {"math": 8.0, "python": 7.5},
#     "SV02": {"math": 6.5, "python": 8.5},
#     "SV03": {"math": 9.0, "python": 9.5},
# }
# #
# # Set các môn học hiện có
# courses = {"math", "python"}

# ## * Yêu cầu:
# #   * a. Dùng vòng lặp + unpacking tuple để in ra danh sách học viên theo format
# #     ```text
# #         SV01 - Nguyen Van A (20)
# #         SV02 - Tran Thi B (21)
# #         ...
# #     ```
# #   * b. Tạo một list mới `python_scores` chỉ chứa tuple `(student_id, name, python_score)`
# #   * c. Tìm học viên có điểm Python cao nhất từ `python_scores` và in ra: `Top Python: <name> - <score>`
# #   * d. Thêm môn mới `"database"` vào `courses` (dùng set) và gán tạm điểm `database = 0` cho tất cả sinh viên trong `scores`
#
# ## a
# for student_id, name, age in students:
#     print(f"{student_id} - {name} ({age})")
#
# ## b
# python_scores = []
#
# for student in students:
#     student_id, name, age = student
#     python_scores.append((student_id, name, scores.get(student_id)["python"]))
#
# print(python_scores)
#
# ## c
# student_id, name, score = max(python_scores, key=lambda item: item[2])
# print(f"Top python: <{name}> - {score}")
#
# ## d
# courses.add("database")
#
# for student, score in scores.items():
#     score.update(database = 0)
#
# print(courses)
# print(scores)

#######################################################################

# Bài tập 2: Thống kê sản phẩm & hóa đơn
#
# products = [
#     (1, "Ban Phim", 250_000),
#     (2, "Chuot", 150_000),
#     (3, "Man Hinh", 3_000_000),
#     (4, "Tai Nghe", 500_000),
# ]
#
# # Danh sách đơn hàng (list dict)
# orders = [
#     {"order_id": "HD01", "items": [1, 2, 4]},
#     {"order_id": "HD02", "items": [2, 3]},
#     {"order_id": "HD03", "items": [1, 4]},
# ]
# #
# # * Yêu cầu:
# #   * a. Tạo một dict `product_map` từ `products` để tra cứu nhanh theo `product_id` với dạng:
# #     ```text
# #         {
# #             1: {"name": "Ban Phim", "price": 250_000},
# #             2: {"name": "Chuot", "price": 150_000},
# #             ...
# #         }
# #     ```
# #   * b. Với mỗi hóa đơn trong `orders`, hãy tính tổng tiền của hóa đơn đó, lưu vào key mới `"total"` trong từng dict hóa đơn
# #     * Hints:
# #       * items là list các product_id
# #       * tra giá ở product_map (dict)
# #       * cộng dồn
# #   * c. In ra danh sách hóa đơn theo format:
# #     ```text
# #         HD01: 3 san pham, Tong tien = ...
# #         HD02: ...
# #     ```
# #   * d. Tạo một set `all_products_sold` chứa tất cả `product_id` đã từng được bán trong mọi hóa đơn, sau đó in ra:
# #     ```text
# #       So luong san pham khac nhau da ban: <len(all_products_sold)>
# #     ```
#
## a
# product_map = {}
# for product in products:
#     product_id, name, price = product
#     product_map[product_id] = {"name": name, "price": price}
#
# print(product_map)
#
# ## b
# for order in orders:
#     item_list = order.get("items")
#     totalPrice = 0
#     for num in item_list:
#         totalPrice += product_map.get(num).get("price")
#     order.update(total = totalPrice)
#
# print(orders)
#
# ## c
# for order in orders:
#     print(f"{order.get("order_id")}: {len(order.get("items"))} sản phẩm, tổng tiền: {order.get("total")}")
#
# ## d
# sold_items = []
# for order in orders:
#     sold_items.append(set(order.get("items")))
#
# all_product_sold = sold_items[0].copy()
# for items in sold_items[1:]:
#     all_product_sold |= items
#
#
# print(f"Số lượng sản phẩm khác nhau đã bán {len(all_product_sold)}")

#######################################################################

### Bài tập 3: Hệ thống tag bài viết & người dùng

# # Danh sách user: list tuple (user_id, name)
# users = [
#     ("U01", "Alice"),
#     ("U02", "Bob"),
#     ("U03", "Charlie"),
# ]
#
# # Dict bài viết: key là post_id, value là dict thông tin
# posts = {
#     "P01": {
#         "title": "Hoc Python co ban",
#         "author_id": "U01",
#         "tags": {"python", "beginner"},
#     },
#     "P02": {
#         "title": "Lam viec voi List va Dict",
#         "author_id": "U01",
#         "tags": {"python", "data-structure"},
#     },
#     "P03": {
#         "title": "Gioi thieu HTML CSS",
#         "author_id": "U02",
#         "tags": {"web", "frontend"},
#     },
# }
#
# # * Yêu cầu:
# #   * a. Tạo một dict `user_map` từ `users`, map `user_id` sang `name`
# #     ```text
# #         Ví dụ:
# #         {
# #             "U01": "Alice",
# #             "U02": "Bob",
# #             "U03": "Charlie",
# #         }
# #     ```
# #   * b. Dùng vòng lặp duyệt `posts.items()` để in ra:
# #     ```text
# #         [P01] Hoc Python co ban - Alice - Tags: python, beginner
# #         [P02] ...
# #     ```
# #     * Hints:
# #       * lấy `author_id` từ dict `posts`
# #       * tra tên ở `user_map`
# #       * `tags` là set, cần chuyển sang list/sorted trước rồi nối thành chuỗi
# #     * c. Tạo một set `all_tags` chứa toàn bộ tag xuất hiện trong mọi bài viết
# #       * Hints: duyệt từng `post`, lấy `post["tags"]` (set), dùng `update()` để dồn vào `all_tags`
# #     * d. Tạo một dict `tag_counter` để đếm số bài viết chứa mỗi tag
# #       ```text
# #         Ví dụ:
# #         {
# #               "python": 2,
# #               "beginner": 1,
# #               "data-structure": 1,
# #               "web": 1,
# #               "frontend": 1,
# #         }
# #       ```
# #       * Hints:
# #         * Khởi tạo `tag_counter = {}`
# #         * Duyệt từng post, với mỗi tag trong `post["tags"]`:
# #           * nếu tag chưa có trong dict => gán = 1
# #           * nếu đã có => tăng lên 1
#
# ## a
# user_map = [{user_id : name} for user_id, name in users ]
#
# ## b
# for post_id, post_info in posts.items():
#     print(f"[{post_id}] {post_info.get("title")} - {post_info.get("author_id")} - Tags: {", ". join(post_info.get("tags"))}")
#
# ## c
# all_tag = set()
#
# for post_id, post_info in posts.items():
#     tag_set = set(post_info.get("tags"))
#     all_tag.update(tag_set)
#
# print(all_tag)
#
# ## d
# tag_counter = {}
# for post_id, post_info in posts.items():
#     for tag in post_info.get("tags"):
#         if tag not in tag_counter:
#             tag_counter[tag] = 1
#         else:
#             tag_counter[tag] += 1
#
# print(tag_counter)