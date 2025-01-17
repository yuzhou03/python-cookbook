def delimiter(sep: str = "-", repeat: int = 80):
    print(sep * repeat)


def pad_text(text, size=80, padding="-"):
    # 使用 str.center() 将 text 居中，并在两端添加 padding 字符，直到总长度为 size
    return text.center(size, padding)


def main():
    print(pad_text("-", 80))
    result = pad_text("hello", 11, "-")
    print(result)  # 输出: ***hello***
    print(pad_text("-", 80))


if __name__ == "__main__":
    main()
