import sys

print(type(sys.argv))  # <class 'list'>

print(sys.argv)  # ['D:\\Adds\\day7\\7-python程序如何传参.py', 'file6', 'file7']


def write_hello(file_path):
    file = open(file_path, 'w+', encoding='utf8')
    file.write('hello')
    file.close()


# D:\Python312\python.exe D:\Adds\day7\7-python程序如何传参.py file6 file7
if __name__ == '__main__':
    write_hello(sys.argv[2])  # 将在file7内写入hello
