# 正则表达式：通常被用来检索，替换那些符合某个模式（规则）的字符串文本，匹配和搜索找到目标的数据。

# re模块：
# 1. re.match方法：
# 尝试从字符串的起始位置匹配一个规则，匹配成功就返回match对象。
# 只能匹配以什么什么开头的字符串，不可以从中间匹配
#   （1）语法：re.match(pattern, string, flag=0)
#   （2）参数说明：
#       pattern：匹配的正则规则，就是你要匹配的是啥
#       string：要匹配的字符串
#       flag：标志位，用于控制正则表达式匹配的方式，如：是否区分大小写，多行匹配等。

import re

# 示例一：（无标志位）
str_text = "Python is the best language in the world"

# 匹配成功的情况
res = re.match("P", str_text)  # 不能用小写的p，因为没有定义标志位
res1 = re.match("Python", str_text)
res2 = re.match("Pyth", str_text)

print(res.group())     # group用来表示出来匹配成功的数据，匹配失败的时候是没有的
print(res1.group())
print(res2.group())

# 匹配失败的情况（注释掉）
# res = re.match("t", str_text)  # 匹配不会成功，因为没有从开头开始
# res = re.match("python", str_text)  # 匹配失败，因为大小写不匹配

# 2. 常用的标志位：
# （1）：re.I 或 re.IGNORECASE：使匹配对大小写不敏感
# （2）：re.M 或 re.MULTILINE：多行匹配模式
#      影响 ^ 和 $ 元字符的行为。在默认情况下，^匹配字符串的开头，$ 匹配字符串的结尾
#      使用 re.M后，^还会匹配每一行的开头，$还会匹配每一行的结尾
# （3）：re.S 或 re.DOTALL：使 . 元字符匹配包括换行符在内的所有字符
#      默认情况下，.匹配除换行符之外的任何单个字符
# （4）：re.X 或 re.VERBOSE：允许你编写更具可读性的正则表达式
#      它允许正则表达式包含注释和空白字符（这些空白字符和注释会被忽略）
# （5）：re.L 或 re.LOCALE：根据当前区域设置来解释字母、数字和其他字符的匹配
# （6）：re.A 或 re.ASCII：使 \w, \W, \b, \B, \d, \D, \s 和 \S只匹配ASCII字符
#      而不是全部Unicode字符。这在你只想匹配ASCII范围内的字符时很有用

# 3. 如果同时使用多个标志位：使用|来进行分割，比如：re.I|re.M

# 示例二：（有标志位）
str_text = "Python is the best language in the world"

# 应用re.I之后就会忽略大小写了
result = re.match("p", str_text, re.I)
print(result.group())

result1 = re.match("python", str_text, re.I)
print(result1.group())

# 4. group的方法：
# （1）group(num)方法：
# 可以获取匹配的数据，如果有多个匹配结果的话，那么会以元组的形式放到group对象中，此时我们可以通过下标去获取
# （2）groups：
# 返回一个包含所有被匹配的小组字符串的元组，从1到所含的小组号（也就是下标），返回的是整个匹配结果