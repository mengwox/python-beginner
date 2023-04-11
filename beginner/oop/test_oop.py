from unittest import TestCase

from beginner.oop.student import Student


class Test(TestCase):
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
