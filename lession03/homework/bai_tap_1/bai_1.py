### Bài tập 1: Dict tần suất từ trong file (Module + File I/O + Exception)

from file_utils import read_file_content, count_word_frequency, count_word

# article.txt
file = input("Nhập tên file cần phân tích: ")

content = read_file_content(file)

top_ten_words = count_word_frequency(content)

total_word = count_word(content)

print(f"Tổng số từ: {total_word}")
print(f"Top 10 từ xuất hiện")

for key, value in top_ten_words.items():
    print(f" - {key}: {value}")

