# 作者: 王道 龙哥
# 2024年12月31日16时08分21秒
# xxx@qq.com
import os


def read_conf():
    """
    读取配置
    :return:
    """
    file = open('file6', 'r+', encoding='utf8')
    text_info = file.read()
    print(text_info)
    print(type(text_info))

    my_dict = eval(text_info)
    print(type(my_dict))
    file.close()


if __name__ == '__main__':
    # read_conf()
    # os.system('rm -r file4')
    eval("__import__('os').system('ls')")  # 不要用eval执行前端发过来的任何子串
    # eval将字符串 当成 有效的表达式 来求值 并 返回计算结果
    # pass
