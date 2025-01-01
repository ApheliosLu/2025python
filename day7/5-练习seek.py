import os


def seek_start():
    """
    相对于开头（文件起始位置）进行偏移
    :return:
    """
    file = open('file1', mode='r+', encoding='utf8')
    file.seek(6, os.SEEK_SET)  # 相对于开头偏移6个字节，注意汉字的偏移是3的整数倍
    text = file.read(5)
    print(text)
    file.close()


def seek_end():
    """
    相对于文件尾部进行偏移
    :return:
    """
    file = open('file1', mode='r+', encoding='utf8')
    file.seek(0, os.SEEK_END)
    text = file.read(5)
    print(text)  # 读不到内容，是空字符串
    file.close()


def seek_cur():
    """
    相对于当前位置不动
    :return:
    """
    file = open('file1', mode='r+', encoding='utf8')
    file.seek(0, os.SEEK_CUR)
    text = file.read(5)
    print(text)
    file.close()


def seek_b_cur():
    """
    在b模式下，读取到的是字节流，读取图片，音频，视频
    :return:
    """
    file = open('file1', mode='rb+')
    file.seek(5, os.SEEK_CUR)
    file.seek(-2, os.SEEK_CUR)
    file.seek(-3, os.SEEK_END)
    b = file.read()  # 得到的是字节流
    print(b)
    file.close()


def copy_file():
    file1 = open('baidu.png', mode='rb+')
    file2 = open('baidu_copy.png', mode='wb')
    b = file1.read()
    file2.write(b)
    file1.close()
    file2.close()


def modify_movie():
    file1 = open('baidu.png', mode='rb+')
    file1.seek(10, os.SEEK_SET)

    b = file1.read(1)
    inverted_b = bytes([~b[0] & 0xFF])  # 按位取反后限制在0-255范围内

    print("取反字节：", inverted_b)
    print(b)

    file1.seek(10, os.SEEK_SET)
    # 写回取反后的字节
    file1.write(inverted_b)
    file1.close()


if __name__ == '__main__':
    # seek_start()
    # seek_end()
    # seek_cur()
    # seek_b_cur()
    # copy_file()
    modify_movie()
