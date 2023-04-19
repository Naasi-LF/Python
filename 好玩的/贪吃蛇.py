# 导入随机数库
import random
 
 
# 女友类
class Girlfriends():
    # 初始化函数，设定了女友的身高体重颜值（属性）
    def __init__(self):
        self.height = random.randint(170, 180)       # 身高必须170朝上，咱们GRQ不喜欢矮的
        self.weight = random.randint(80, 99)         # 体重必须80-90斤，咱GRQ不喜欢胖的
        self.beauty_index = random.randint(90, 100)  # 颜值还用说吗，满分一百，必须A+级别的
 
    # 输出女友信息的函数（方法）
    def print_info(self):
        print('身高：', self.height, '\n体重: ', self.weight, '\n颜值: ', self.beauty_index, '\n')
 
 
# 给GRQ new九十九个女友模块
# 循环99次实例化女友
for i in range(99):
    # new一个女友
    new_girlfriends = Girlfriends()
    # 女友的编号
    print('GRQ第', i + 1, '个女友的身高体重颜值')
    # 调用打印出女友信息的方法
    new_girlfriends.print_info()