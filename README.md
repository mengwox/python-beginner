# python-beginner

python入门教程

- [廖雪峰Python教程](https://www.liaoxuefeng.com/wiki/1016959663602400)
- [OSSU-Python For Everybody](https://www.py4e.com/)
- [Python官方Tutorial](https://docs.python.org/3/tutorial/index.html)
- [Python编程快速上手-让繁琐工作自动化](https://automatetheboringstuff.com/)
- [OSSU-Introduction-to-computer-science-and-programming-in-python-fall-2016](
  https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)

# python

### python函数类型

- 必填参数(位置参数)
- 默认参数, 有默认值
- 可变参数
- 关键字参数

```python
def param(req_param, def_param='123', *param, **kwargs):
  """
  req_param: 必填参数
  def_param: 默认参数
  *param: 可变参数
  **kwargs: 关键字参数
  """
```

## python的35个关键字

```text
and     continue  finally  is        raise
as      def       for      lambda    return
assert  del       from     None      True
async   elif      global   nonlocal  try
await   else      if       not       while
break   except    import   or        with
class   False     in       pass      yield
```

## 数据类型: 序列Sequence

数据类型为序列的有: string, tuple, list, range

以上4种数据比较见下图:

![string, tuple, list, range](.\images\序列比较.jpg "4种序列类型比较")

### string字符串

string, 实际上是character的array.

python支持索引为负数, 从-1开始计数, 表示倒数第一个

```python
word = 'Python'
# word[0] = P, word[-1] = n
```

#### Slicing切片

字符串切片, 相当于java的string.split.

对于一个字符串s,索引i:

1. 总是有`s[:i] + s[i:] = s`
2. `s[i:j]`的字符长度 = `j-i`
3. 索引越界的index`j`, `s[j]`会报IndexError
4. python string slice,会自动处理索引越界问题, 所以`s[:j]`不会报IndexError
5. slice索引有默认值, 省略的第一个索引默认为0, 省略的第二个索引默认为the end of string
6. string在python中,和java类似(final修饰),string in python也是不可修改(immutable-不可变对象)

### dict(short for Dictionary)

字典, 与java中map一样

结构:

1. k-v序列队(key-value pairs)
2. 用大括号(curly braces)包裹整个序列队

#### dict key

字典key的数据类型必须满足的2个必要条件:

1. 必须实现`__hash__`方法, 用于计算key的hash值
2. 必须实现`__eq__`方法, 用于比较key的hash值是否一致

so: 所有不可变的序列都可以作为dict key, 所有可变的序列都不可以作为dict key

## More Control Flow 流程控制语句

### if语句

结构如:
if True/False
do something
elif True/False (optional)
do something
else True/False (optional)
do something

### for语句

结构如:
for i in collection:
do something

### range()函数

用处: iterate over a sequence of numbers
range class有3个属性:

- start: int, 起始, 非必填
- stop: int, 终止, 必填
- step: int, 迭代步长, 非必填

# OSSU-SICP(Python版)

指定当前python文件编码格式:

![指定当前python文件编码格式](.\images\python指定当前文件编码格式.jpg "Python File Encoding")
