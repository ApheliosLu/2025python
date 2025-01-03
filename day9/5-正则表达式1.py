# 作者: 陆离ApheliosLu
# 2025年01月03日20时03分32秒
# Leon12097@163.com


import re


def use_greedy():
    s = "This is a number 234-235-22-423"
    ret = re.match(r".+?(\d+-\d+-\d+-\d+)", s)
    print(ret.group(1))
    print(re.match(r"aa(\d+)", "aa2343ddd").group(1))

    print(re.match(r"aa(\d+?)", "aa2343ddd").group(1))

    print(re.match(r"aa(\d+)ddd", "aa2343ddd").group(1))

    print(re.match(r"aa(\d+?)ddd", "aa2343ddd").group(1))


def use_r():
    """
    r的作用, 原生字串
    :return:
    """
    mm = "c:\\a\\b\\c"
    print(mm)
    print(re.match(r"c:\\", mm).group())


def use_option():
    print(re.match(r'\w*','abc函',flags=re.A).group())   # 忽略汉字
    print(re.match(r'a*', 'aA',flags=re.I).group())     # 区分大小写
    print(re.match(r'.*','abc\ndef',flags=re.S).group())    # 匹配上\n

if __name__ == '__main__':
    use_greedy()
    # use_r()
    # use_option()