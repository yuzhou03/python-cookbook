# 编写一个函数，接受一个字符串作为参数，返回该字符串中的所有数字和英文单词。分别存储在两个列表中。
#
# 例如，输入字符串 "Hello你好 123\nWorld世界 456"，返回两个列表 [123, 456] 和 ["Hello", "World"]。


def extract_numbers_and_words(input_string):
    import re

    numbers = re.findall(r"\d+", input_string)
    words = re.findall(r"\b[a-zA-Z]+\b", input_string)
    return numbers, words


def test_extract_numbers_and_words():
    input_string = "Hello(你好) 123\nWorld（世界） 456"
    print("输入字符串为:")
    print(input_string)
    numbers, words = extract_numbers_and_words(input_string)
    print("提取到的数字列表为:", numbers)
    print("提取到的单词列表为:", words)

    assert numbers == ["123", "456"]
    assert words == ["Hello", "World"]


if __name__ == "__main__":
    test_extract_numbers_and_words()
