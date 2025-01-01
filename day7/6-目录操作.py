import os


def use_rename():
    """
    理解相对路径，绝对路径
    :return:
    """
    os.rename('dir2/dir3/file4', 'dir2/dir3/file5')
    os.remove('dir2/dir3/file5')


def use_dir_func():
    file_list = os.listdir('.')
    print(file_list)

    # os.mkdir('dir3')
    os.rmdir('dir3')
    print(os.getcwd())
    os.chdir('dir2')
    file = open('file1', 'w', encoding='utf8')
    file.write('写入file1')
    file.close()


def change_dir():
    """
    改变路径
    :return:
    """
    print(os.getcwd())
    os.chdir('dir2')  # 类似于进入这个目录
    print(os.getcwd())


def scan_dir(current_path, width):
    """
    深度优先遍历
    :param current_path:
    :return:
    """
    file_list = os.listdir(current_path)  # 得到当前文件夹下的所有文件
    for file in file_list:
        print(' ' * width, file)  # 打印文件名,width代表多少个空格
        new_path = current_path + '/' + file  # 把当前路径和文件名拼接到一起
        if os.path.isdir(new_path):
            scan_dir(new_path, width + 4)


def use_stat(file_path):
    """
    文件大小
    :param file_path:
    :return:
    """
    file_info = os.stat(file_path)
    print('size{},uid{},mode{:x},mtime{}'.format(file_info.st_size, file_info.st_uid,
                                                 file_info.st_mode, file_info.st_mtime))

    from time import strftime
    from time import gmtime
    gm_time = gmtime(file_info.st_mtime)
    # 把秒数转为字符串时间
    print(strftime("%Y-%m-%d %H:%M:%S", gm_time))


if __name__ == '__main__':
    # use_rename()
    # use_dir_func()
    # change_dir()
    # scan_dir('.', 0)
    use_stat('file4')
