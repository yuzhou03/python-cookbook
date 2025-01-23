def align():
    """
    对齐
    str.center(width[, fillchar])：居中对齐。
    str.ljust(width[, fillchar])：左对齐。
    str.rjust(width[, fillchar])：右对齐。
    """

    s = "hello"
    print(s.center(10, "-"))  # "--hello---"
    print(s.ljust(10, "*"))  # "hello*****"
    print(s.rjust(10, "."))  # ".....hello"


if __name__ == "__main__":
    align()
