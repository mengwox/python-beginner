from beginner.oop.person import Person


class Student(Person):
    def __init__(self, name, score) -> None:
        """
        初始化函数
        :param name: 姓名,继承自Human
        :param score: 分数
        """
        super().__init__(name)
        self.__score = score

    def print_obj(self) -> None:
        """
        打印Student对象属性
        """
        print()
        print('name:%s,score:%d' % (self.get_name(), self.__score))

    def get_grade(self) -> str:
        if self.__score < 60:
            return '%s get %s' % (self.get_name(), 'C')
        elif self.__score < 80:
            return '%s get %s' % (self.get_name(), 'B')
        elif self.__score < 100:
            return '%s get %s' % (self.get_name(), 'A')
        else:
            return '%s get %s' % (self.get_name(), 'SUPER')

    def get_score(self) -> int:
        return self.__score

    def set_score(self, score) -> None:
        self.__score = score
