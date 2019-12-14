#!/usr/bin/env python
# _*_ coding:utf-8 _*_


# 导入需要用到的package
import numpy as np
import json
import matplotlib.pyplot as plt


# 读入训练数据
def load_data():
    # 从文件导入数据
    datafile = './work/housing.data'
    data = np.fromfile(datafile, sep=' ')

    # 每条数据包括14项，其中前面13项是影响因素，第14项是相应的房屋价格中位数
    feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', \
                     'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
    feature_num = len(feature_names)

    # 将原始数据进行Reshape，变成[N, 14]这样的形状
    data = data.reshape([data.shape[0] // feature_num, feature_num])

    # 将原数据集拆分成训练集和测试集
    # 这里使用80%的数据做训练，20%的数据做测试
    # 测试集和训练集必须是没有交集的
    ratio = 0.8
    offset = int(data.shape[0] * ratio)
    training_data = data[:offset]

    # 计算train数据集的最大值，最小值，平均值
    maximums, minimums, avgs = training_data.max(axis=0), training_data.min(axis=0), \
                               training_data.sum(axis=0) / training_data.shape[0]

    # 对数据进行归一化处理
    for i in range(feature_num):
        # print(maximums[i], minimums[i], avgs[i])
        data[:, i] = (data[:, i] - avgs[i]) / (maximums[i] - minimums[i])

    # 训练集和测试集的划分比例
    training_data = data[:offset]
    test_data = data[offset:]
    return training_data, test_data


class Network(object):
    def __init__(self, num_of_weights):
        # 随机产生w的初始值
        # 为了保持程序每次运行结果的一致性，此处设置固定的随机数种子
        np.random.seed(0)
        # 第一层的参数 为了保证第二层的输入为 (1*13) 第一层的输入权重应为（13*13） （1*13） * （13*13） = (1*13)
        self.w0 = np.random.randn(num_of_weights, num_of_weights)
        self.b0 = np.zeros(num_of_weights)

        self.w1 = np.random.randn(num_of_weights, 1)
        self.b1 = 0.

    def forward0(self, x):
        x = np.dot(x, self.w0) + self.b0
        return x

    def forward1(self, x):
        x = np.dot(x, self.w1) + self.b1
        return x

    def loss(self, z, y):
        error = z - y
        num_samples = error.shape[0]
        cost = error * error
        cost = np.sum(cost) / num_samples
        return cost

    def gradient(self, x, y, z):
        N = x.shape[0]
        gradient_w = 1. / N * np.sum((z - y) * x, axis=0)
        gradient_w = gradient_w[:, np.newaxis]
        gradient_b = 1. / N * np.sum(z - y)
        return gradient_w, gradient_b

    def update0(self, gradient_w, gradient_b, eta=0.01):
        self.w0 = self.w0 - eta * gradient_w
        self.b0 = self.b0 - eta * gradient_b

    def update1(self, gradient_w, gradient_b, eta=0.01):
        self.w1 = self.w1 - eta * gradient_w
        self.b1 = self.b1 - eta * gradient_b

    def train(self, x, y, iterations=100, eta=0.01):
        losses = []
        for i in range(iterations):
            out0 = self.forward0(x)
            out1 = self.forward1(out0)
            L = self.loss(out1, y)

            gradient_w1, gradient_b1 = self.gradient(out0, y, self.forward1(out0))
            self.update1(gradient_w1, gradient_b1, eta)

            gradient_w0, gradient_b0 = self.gradient(x, out0, self.forward1(x))
            self.update0(gradient_w0, gradient_b0, eta)

            losses.append(L)
            if (i + 1) % 10 == 0:
                print('iter {}, loss {}'.format(i + 1, L))
        return losses


# 获取数据
train_data, test_data = load_data()
x = train_data[:, :-1]
y = train_data[:, -1:]
# 创建网络
net = Network(13)
num_iterations = 300
# 启动训练
losses = net.train(x, y, iterations=num_iterations, eta=0.01)

# 画出损失函数的变化趋势
plot_x = np.arange(num_iterations)
plot_y = np.array(losses)
plt.plot(plot_x, plot_y)
plt.show()