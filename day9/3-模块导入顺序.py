# 作者: 陆离ApheliosLu
# 2025年01月03日10时58分58秒
# Leon12097@163.com

import sys

sys.path.insert(0, 'module')
print(sys.path)
print('-' * 50)
import my_module    # 插入后可import

my_module.test1()
