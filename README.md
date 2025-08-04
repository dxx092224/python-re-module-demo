# Python 正则表达式 re 模块学习示例

这个仓库包含了 Python 正则表达式 re 模块的学习示例和格式化代码。

## 文件说明

- `re_module.py` - 格式化后的 re 模块学习代码，包含详细的注释和示例

## 内容概览

### 1. re.match 方法
- 从字符串起始位置匹配规则
- 只能匹配开头的字符串，不能从中间匹配
- 语法：`re.match(pattern, string, flag=0)`

### 2. 常用标志位
- `re.I` / `re.IGNORECASE` - 忽略大小写
- `re.M` / `re.MULTILINE` - 多行匹配模式
- `re.S` / `re.DOTALL` - 使 . 匹配包括换行符在内的所有字符
- `re.X` / `re.VERBOSE` - 允许编写更具可读性的正则表达式
- `re.L` / `re.LOCALE` - 根据当前区域设置解释字符
- `re.A` / `re.ASCII` - 只匹配 ASCII 字符

### 3. group 方法
- `group(num)` - 获取匹配的数据
- `groups()` - 返回包含所有被匹配小组字符串的元组

## 运行示例

```bash
python re_module.py
```

## 学习要点

1. 正则表达式用于检索和替换符合特定模式的字符串
2. re.match 只能从字符串开头匹配
3. 使用标志位可以控制匹配行为
4. group 方法用于获取匹配结果

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个学习示例！