# 作者: 陆离ApheliosLu
# 2025年01月03日09时48分18秒
# Leon12097@163.com

import copy


def use_list():
    a = [1, 2, 3]   # 由于 a 只包含整数（不可变对象），所以浅拷贝和深拷贝的效果是一样的：c 和 a 没有共享任何对象的引用，c 是一个全新的列表。
    b = a
    # c = copy.copy(a)      # 与下一行代码等价
    c = a.copy()
    print(id(a))  # a和b id相同，传递了引用
    print(id(b))
    print(id(c))  # c 使用copy的id不同

    a[0] = 10
    print(a)  # a和b 都变了
    print(b)
    print(c)  # c 没变


def use_copy():
    """
    浅copy，copy的是外层的容器对象，但是内层的元素（a和b）没有copy
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]  # c包含可变类型
    d = copy.copy(c)
    print(id(c))
    print(id(d))  # d与c地址不同

    a[0] = 10
    print(f'c--{c}')  # c和d都引用了a，c和d的值都会改变
    print(f'd--{d}')
    print('-' * 50)
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))  # d 中两个元素的内存地址，应该与 c 中相同


def use_deepcopy():
    """
    递归去copy，不管有多少层，都会新做一个空间，把数据拿进来
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c))
    print(id(d))  # 深copy，c和d的地址不同
    a[0] = 10
    print(f'c--{c}')  # c的值随着a的值改变，d的值不变
    print(f'd--{d}')
    print('-' * 50)
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))


class Hero:
    def __init__(self, name, blood):
        self.name = name
        self.blood = blood
        self.equipment = ['鞋子', '指环']


def use_copy_own_obj():
    """
    实际对于自定义对象的练习
    :return:
    """
    old_hero = Hero('蚂蚁', 90)
    new_hero = copy.deepcopy(old_hero)
    new_hero.blood = 80  # 新对象修改后，原对象不会受到任何影响
    new_hero.equipment.append('药水')
    print(old_hero.blood)
    print(old_hero.equipment)
    print(new_hero.blood)
    print(new_hero.equipment)


if __name__ == '__main__':
    use_list()
    # use_copy()
    # use_deepcopy()
    # use_copy_own_obj()
