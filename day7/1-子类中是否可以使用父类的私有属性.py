class A:
    def __init__(self):
        self.__age = 18

    def base_age(self):
        print(self.__age)


class B(A):
    def get_age(self):
        self.base_age()


if __name__ == '__main__':
    zhangsan = B()
    zhangsan.get_age()  # 子类通过调用父类内的方法，使用了父类的私有属性
