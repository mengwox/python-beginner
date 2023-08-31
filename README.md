# python-beginner

python入门教程

- [廖雪峰Python教程](https://www.liaoxuefeng.com/wiki/1016959663602400)
- [OSSU-Python For Everybody](https://www.py4e.com/)
- [Python官方Tutorial](https://docs.python.org/3/tutorial/index.html)

# python

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

## string字符串

string, 实际上是character的array.

python支持索引为负数, 从-1开始计数, 表示倒数第一个

```python
word = 'Python'
# word[0] = P, word[-1] = n
```

### Slicing切片

字符串切片, 相当于java的string.split.

对于一个字符串s,索引i:

1. 总是有`s[:i] + s[i:] = s`
2. `s[i:j]`的字符长度 = `j-i`
3. 索引越界的index`j`, `s[j]`会报IndexError
4. python string slice,会自动处理索引越界问题, 所以`s[:j]`不会报IndexError
5. slice索引有默认值, 省略的第一个索引默认为0, 省略的第二个索引默认为the end of string
6. string在python中,和java类似(final修饰),string in python也是不可修改(immutable-不可变对象)

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