from rich.console import Console
from rich.markdown import Markdown

console = Console()

# Markdown 文本
# 无序列表、有序列表
# 绿色文字
markdown_text = """
# 标题1 - rich Markdown真香
## 标题2 - this is just a demo

这是一段 **加粗** 和 *斜体* 的文本    
这是一段~~删除~~ 的文本  
这是一段 `内联代码` 的文本

*Python代码块*
```python
def hello():
    print('Hello, World!')
```        
*Golang代码块*
```go
package main
import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```




- 无序列表项 1
  - 子项 1   
  - 子项 2
- 无序列表项 2

1. 有序列表项 1
2. 有序列表项 3

> 这是一段引用文本
>> to be or not to be, that is the question.

[Python Rich库](https://github.com/textualize/rich/blob/master/README.cn.md)

表格

| 姓名   | 年龄 | 城市   |
|--------|------|--------|
| 张三   | 25   | 北京   |
| 李四   | 30   | 上海   |


"""

# 创建 Markdown 对象
markdown = Markdown(markdown_text)

# 在控制台中打印 Markdown 文本
console.print(markdown)
