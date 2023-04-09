def list_compre():
    """
    列表生成式用法
    :return:
    """
    L1 = ['Hello', 'World', 18, 'Apple', None]
    return [x.lower() for x in L1 if x is not None and isinstance(x, str)]
