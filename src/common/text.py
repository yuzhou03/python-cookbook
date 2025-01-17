def delimiter(sep: str = "-", repeat: int = 80):
    print(sep * repeat)


def pad_text(text, size=80, padding="-"):
    # 使用 str.center() 将 text 居中，并在两端添加 padding 字符，直到总长度为 size
    return text.center(size, padding)


def print_pad(text, size=80, padding="-"):
    # 使用 str.center() 将 text 居中，并在两端添加 padding 字符，直到总长度为 size
    print(text.center(size, padding))


def main():
    print_pad("-", 80)
    print_pad("hello", 11, "-")
    print_pad("-", 80)


if __name__ == "__main__":
    main()
