import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
from matplotlib.pyplot import MultipleLocator
from dateutil.parser import parse

matplotlib.rcParams['font.family'] = 'KaiTi'  # 更改默认设置，可以显示中文，其中‘KaiTi’是楷体字
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
df = pd.read_excel('C:\\Users\\AKSJ\Desktop\\charts.xlsx', "sheet1")  # 读取xlsx文件
scores = df['推荐指数']  # 获得推荐指数
times = df['日期']  # 获得日期
score = []
time = []
test = []
testfi = []
i = 0
for i in range(160):  # 将日期转为字符串类型
    test.append(str(times[i]))
for i in range(160):  # 将时间截断，只保留日。如：2019-06-24，截断后为24
    testfi.append(test[i].strip()[8:10])
for i in range(160):  # 取160个数据
    if (int(testfi[i]) > 0):
        score.append(scores[i])  # 用append将传入的对象附加(添加)到现有列表中
        time.append(testfi[i])
score1 = []  # 存储力荐的分数
score2 = []  # 存储推荐的分数
score3 = []  # 存储还行的分数
score4 = []  # 存储较差的分数
i = 0
while i < 160:  # 获得力荐的数量并存储进score1
    if (scores[i] == '力荐'):
        score1.append(scores[i])
    i = i + 1
j = 0
while j < 160:  # 获得推荐的数量并存储进score2

    if (scores[j] == '推荐'):
        score2.append(scores[j])
    j = j + 1
k = 0
while k < 160:  # 获得还行的数量存储进score3
    if (scores[k] == '还行'):
        score3.append(scores[k])
    k = k + 1
m = 0
while m < 160:  # 获得较差的数量并存储进score4
    if (scores[m] == '较差'):
        score4.append(scores[m])
    m = m + 1
weight1 = len(score1) / 100  # 获得力荐的分数所占比重
weight2 = len(score2) / 100  # 获得推荐的分数所占比重
weight3 = len(score3) / 100  # 获得还行的分数所占比重
weight4 = len(score4) / 100  # 获得较差的分数所占比重
# 创建图形
plt.figure(1)
ax1 = plt.subplot(2, 2, 1)  # 在一个2行2列共4个子图的图中，定位第1个图来进行操作（画图）。最后面那个1表示第1个子图,那个数字的变化来定位不同的子图.
plt.sca(ax1)
weight = [weight1, weight3, weight2, weight4]  # weight来存放存放各部分占比
explode = (0.05, 0.05, 0.05, 0.05)  # 这个是控制分离的距离的，默认的饼图不分离。
labels = '力荐', '还行', '推荐', '较差'  # 饼图标签
plt.title('推荐指数')  # 饼图标题
plt.pie(weight, labels=labels, explode=explode, autopct='%1.3f%%')  # 用pie函数来进行饼图的设定%1.3f'：指小数点后保留三位有效数值
ax2 = plt.subplot(2, 1, 2)
ay = plt.gca()
plt.ylim('较差', '还行', '推荐', '力荐')  # 将坐标进行重新排序
plt.scatter(time, score)
plt.sca(ax2)
plt.xlabel("日期")
# 横坐标标签名
plt.ylabel("推荐指数")
# 纵坐标标签名
ax3 = plt.subplot(2, 2, 2)
plt.scatter(score, time)
plt.sca(ax3)
plt.xlabel("推荐指数")
# 横坐标标签名
plt.ylabel("日期")
# 纵坐标标签名
plt.show()