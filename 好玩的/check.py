import math

x = float(input())

if x < 0:
    y = abs(x+1)
elif x >= 0 and x <= 5:
    y = 2 * x + 1
else:
    y = math.sin(x) + 5

# 使用 round() 函数保留两位小数并进行输出
print("x={},y={}".format(round(x,2),round(y,2)))