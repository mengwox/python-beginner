class Person(object):
    def __init__(self, name) -> None:
        """
        初始化函数
        :param name: 姓名
        """
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name) -> None:
        self.__name = name
