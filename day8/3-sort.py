# 作者: 陆离ApheliosLu
# 2025年01月02日16时02分08秒
# Leon12097@163.com

my_list = "This is a test string from Andrew".split()
print(my_list)


def change_lower(str_name: str):
    return str_name.lower()


# key可以传递一个比较规则的函数,比较规则发生了改变,key就是给它传递一个函数
print(sorted(my_list, key=change_lower))
print('-' * 50)

# sort将改变原列表
my_list.sort(key=change_lower)
print(my_list)
print('-' * 50)

student_tuples = [
    ('jane', 'B', 12),
    ('john', 'A', 15),
    ('dave', 'B', 10),
]

# lambda表达式，就是匿名函数，匿名函数好处，提高编写效率，提高阅读速度
print(sorted(student_tuples, key=lambda x: x[2]))


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        相对于__str__来说，更方便，可以返回非字符串类型
        :return:
        """
        return repr((self.name, self.grade, self.age))


student = Student('john', 'A', 15)
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print('-' * 50)
print(sorted(student_objects, key=lambda student: student.age))

from operator import itemgetter, attrgetter

print('使用operator系列')
print(sorted(student_tuples, key=itemgetter(0)))
print(sorted(student_objects, key=attrgetter('age')))

print('使用operator系列,多列排序')
print(sorted(student_tuples, key=itemgetter(1, 2)))
print(sorted(student_tuples, key=lambda x: (x[1], -x[2])))  # 第一列升序，第二列降序

print(sorted(student_objects, key=attrgetter('grade', 'age'), reverse=True))

print('查看排序稳定性')
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(data, key=itemgetter(0)))

mydict = {'Li': ['M', 7],
          'Zhang': ['E', 2],
          'Wang': ['P', 3],
          'Du': ['C', 2],
          'Ma': ['C', 9],
          'Zhe': ['H', 7]}

print(sorted(mydict.items(), key=lambda x: x[1][1]))

gameresult = [
    {"name": "Bob", "wins": 10, "losses": 3, "rating": 75.00},
    {"name": "David", "wins": 3, "losses": 5, "rating": 57.00},
    {"name": "Carol", "wins": 4, "losses": 5, "rating": 57.00},
    {"name": "Patty", "wins": 9, "losses": 3, "rating": 71.48}]
print('-' * 50)
print(sorted(gameresult, key=lambda x: x['rating']))

print(sorted(gameresult, key=itemgetter("rating", "name")))
