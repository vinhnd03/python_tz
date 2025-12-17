def read_file_content(filename: str) -> str:
    file_content = ""

    try:
        with open(filename, "r", encoding="utf-8") as f:
            file_content = " ".join(line.rstrip("\n") for line in f)
    except FileNotFoundError:
        print("Không tìm thấy file.")
    except Exception:
        print("Có lỗi xảy ra.")
    return file_content


def count_word_frequency(text: str) -> dict[str, int]:
    punctuation_marks = ".,;:?!()[]"
    words = get_word_list(text)

    # code tham khảo
    words = ["".join(char for char in word if char not in punctuation_marks) for word in words]
    words = [word for word in words if word]

    # for word in words:
    #     for char in word:
    #         if char in punctuation_marks:
    #             word = word.replace(char, "")

    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    top_ten_words = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10])

    return top_ten_words

def count_word (text: str) -> int:
    return len(get_word_list(text))

def get_word_list (text: str) -> list[str]:
    return text.lower().split()

content = read_file_content("article.txt")

# print(content)
# print(type(content))
# print(get_word_list(content))
# print(count_word_frequency(content))
# print((count_word(content)))
