class Police(object):
    def __init__(self):
        self.__score = 0

    @property
    def score(self) -> int:
        """
        @property,将score()函数,转变为一个score可读属性
        :return:
        """
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between [0~100]')
        self.__score = value
