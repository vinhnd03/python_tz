def read_file_content(filename: str) -> str:
    file_content = ""

    try:
        with open(filename, "r", encoding="utf-8") as f:
            file_content = f.readlines()

    except FileNotFoundError:
        print("Không tìm thấy file.")
    except Exception:
        print("Có lỗi xảy ra.")
    return file_content


def count_word_frequency(text: str) -> dict[str, int]:
    punctuation_marks = ".,;:?!()[]"
    words= get_word_list(text)

    # code tham khảo
    # words = ["".join([char for char in word if char not in punctuation_marks]) for word in words]

    for word in words:
        for char in word:
            if char in punctuation_marks:
                word = word.replace(char, "")

    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    top_ten_words = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10])

    return top_ten_words

def count_word (text: str) -> int:
    words = get_word_list(text)
    return len(words)

def get_word_list (text: str) -> list[str]:
    word_list = []
    for line in text:
        word_list = line.lower().split()
    return word_list