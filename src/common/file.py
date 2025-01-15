def read_file(file_path):
    """
    读取指定文件并显示其内容。

    :param file_path: 文件路径
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"错误: 文件 '{file_path}' 未找到。")
    except PermissionError:
        print(f"错误: 没有权限读取文件 '{file_path}'。")
    except Exception as e:
        print(f"发生错误: {e}")
