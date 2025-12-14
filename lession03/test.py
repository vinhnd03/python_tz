word = "hello."
punctuation_marks = ".,;:?!()[]"

for char in word:
    if char in punctuation_marks:
        word = word.replace(char, "")
    print(char)

print(word)