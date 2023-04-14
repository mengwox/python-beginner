from unittest import TestCase

from beginner.oop.police import Police
from beginner.oop.student import Student


class Test(TestCase):
    def test_police(self):
        pl = Police()
        try:
            pl.score = 101
        except ValueError as e:
            print(e.args[0])
        print(pl.score)
        pass

    def test_student_msg(self):
        sd = Student('123')
        sd2 = Student('456')
        print(sd.msg)
        print(sd2.msg)
        print(Student.msg)
        # 实际上是给sd赋值了一个名为msg的实例属性, Student的类属性msg并没有改变
        # 所以,强烈建议不要给实例赋值与类属性名称一致的实例属性,容易混淆
        sd.msg = '1234'
        Student.msg = 'abc'
        print(sd.msg)
        print(sd2.msg)
        print(Student.msg)

    def test_student_count(self):
        # 测试:
        Student.count = 0
        self.assertTrue(Student.count == 0, '测试失败!')
        bart = Student('Bart')
        # bart.mawenhao = 'mawenhaostr'
        try:
            if hasattr(bart, 'mawenhao'):
                print(getattr(bart, 'mawenhao'))
            else:
                raise AttributeError('当前对象没有名为mawenhao的属性')
        except AttributeError as e:
            print(e.args[0])
        self.assertTrue(Student.count == 1, '测试失败!')
        Student('Bart')
        self.assertTrue(Student.count == 2, '测试失败!')
        print('测试通过')

    def test_student(self):
        """
        测试Student对象
        :return:
        """
        st = Student('mawenhao', 100)
        st.print_obj()
        self.assertTrue(st is not None, '测试通过')
        self.assertTrue(st.get_name() == 'mawenhao', '测试通过')
        self.assertTrue(st.get_score() == 100, '测试通过')

        st2 = Student('martin1', 59)
        self.assertTrue(st != st2, '两个实例不相同')

        st2 = Student('martin1', 59)
        print(st2.get_grade())
        print(Student('martin1', 60).get_grade())
        print(Student('martin2', 80).get_grade())
        print(Student('martin3', 90).get_grade())
        print(Student('martin4', 100).get_grade())
