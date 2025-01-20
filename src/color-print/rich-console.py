from rich.console import Console
from common.text import print_pad


console = Console()

# 普通彩色文本
console.print("[bold red]红色加粗文本[/bold red]")
console.print("[green]绿色文本[/green]")
# 背景色
console.print("[on red]红色背景[/on red]")
# 高亮
console.print("[bold red on yellow]红色加粗文本[/bold red on yellow]")
# 斜体
console.print("[italic]斜体文本[/italic]")
# 下划线
console.print("[underline]下划线文本[/underline]")
# 绿色、斜体
console.print("[green italic]绿色斜体文本[/green italic]")

# 高亮代码
from rich.syntax import Syntax

code = "print('Hello, World!')"
# theme参数可选值
# "monokai"、"github-dark"、"github-light"、"xcode"、"one-dark"、"one-light"、"vs"、"tango"、"monokai"、"gruvbox-dark"、"gruvbox-light"、"material"、"dracula"


def print_code(code, theme, index=1):
    print_pad(f"theme {index}: {theme}")
    syntax = Syntax(code, "python", theme=theme, line_numbers=True, start_line=index)
    console.print(syntax)


themes = [
    "monokai",
    "github-dark",
    "github-light",
    "xcode",
    "one-dark",
    "one-light",
    "vs",
    "tango",
    "monokai",
    "gruvbox-dark",
    "gruvbox-light",
    "material",
    "dracula",
]


for i, theme in enumerate(themes, start=1):
    print_code(code, theme, i)
