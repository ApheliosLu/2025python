# 作者: 陆离ApheliosLu
# 2025年01月02日14时07分38秒
# Leon12097@163.com


import random
import time
import sys

sys.setrecursionlimit(1000000)  # 增加递归深度


class Sort:
    def __init__(self, n):
        """
        n是排序的数的数量
        :param n:
        """
        self.len = n  # 被排序的列表的长度
        # self.arr = [3, 87, 2, 93, 78, 56, 61, 38, 12, 40]
        self.arr = [0] * n
        self.random_data()

    def random_data(self):      # 生成随机列表
        for i in range(self.len):
            self.arr[i] = random.randint(0, 99)

    def partition(self, left, right):
        arr = self.arr
        k = i = left
        random_pos = random.randint(left, right)  # 如何避免陷入最坏时间复杂度
        arr[random_pos], arr[right] = arr[right], arr[random_pos]   # 先把pivos放右边
        for i in range(left, right):
            if arr[i] < arr[right]:  # 某个位置的值小于分割值，就拿它和k指向的位置交换
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick_sort(self, left, right):  # logn层递归，每一层工作量O(n)
        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def adjust_max_heap(self, pos, arr_len):
        """
        把某个子树调整为大根堆
        :param pos: 被调整的元素位置，是父亲
        :param arr_len: 当时列表总长度
        :return:
        """
        arr = self.arr
        dad = pos
        son = 2 * dad + 1
        while son < arr_len:  # 左孩子小于列表长度
            if son + 1 < arr_len and arr[son] < arr[son + 1]:  # 判断右孩子存在，且右孩子大于左孩子
                son += 1
            if arr[son] > arr[dad]:
                arr[dad], arr[son] = arr[son], arr[dad]
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap_sort(self):  # 建堆O(n)，调整堆O(logn)
        # 把列表调整为大根堆
        for parent in range(self.len // 2 - 1, -1, -1):
            self.adjust_max_heap(parent, self.len)
        arr = self.arr
        arr[0], arr[self.len - 1] = arr[self.len - 1], arr[0]  # 堆顶元素和最后一个元素交换
        for arr_len in range(self.len - 1, 1, -1):
            self.adjust_max_heap(0, arr_len)
            arr[0], arr[arr_len - 1] = arr[arr_len - 1], arr[0]

    def test_time_use(self, sort_func, *args, **kwargs):
        """
        回调函数
        :param sort_func:
        :param args:
        :param kwargs:
        :return:
        """
        start = time.time()
        sort_func(*args, **kwargs)
        end = time.time()
        print(f'总计用时{end - start}')


if __name__ == '__main__':
    count = 100000
    my_sort = Sort(count)   # 生成待排序列表
    print(my_sort.arr)

    # my_sort.quick_sort(0, count - 1)
    # print(my_sort.arr)

    my_sort.heap_sort()
    print(my_sort.arr)
    my_sort.test_time_use(my_sort.heap_sort)    # 堆排用时

