import math
import random
import numpy as np

np.seterr(all = 'ignore') #对所有运算错误不做任何操作

# sigmoid函数作为输出层的激活函数
def sigmoid(x):
    return 1/(1+np.exp(-x))

# sigmoid的导数
def dsigmoid(y):
    """输入参数y是sigmoid(x)的值"""
    return y*(1.0-y)
# tanh函数作为隐藏层的激活函数
def tanh(x):
    return math.tanh(x)

def dtanh(y):
    return 1-y*y

class MLP_NeuralNetwork(object):
    """
    神经网络共三部分：输入层，隐藏层，输出层
    接收的数据格式为：
                    [[[x1, x2, x3, ..., xn], [y1, y2, ..., yn]],
                    [[x1, x2, x3, ..., xn], [y1, y2, ..., yn]],
                                           ...
                    [[x1, x2, x3, ..., xn], [y1, y2, ..., yn]]]
    """
    def __init__(self, input, hidden, output, iterations, learning_rate, momentum, rate_decay):
        """
        input : 输入层神经元的个数
        hidden : 隐藏层神经元个数
        output : 输出层神经元个数
        """
        # 初始化参数
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.rate_decay = rate_decay

        # 初始化数组
        self.input = input + 1
        self.hidden = hidden
        self.output = output

        # 创建各层的输出
        self.ai = [1.0] * self.input # 产生一个self.input个1.0的列表
        self.ah = [1.0] * self.hidden
        self.ao = [1.0] * self.output

        # 创建随机权重
        # use scheme from 'efficient backprop to initialize weights
        input_range = 1.0 / self.input ** (1/2)
        output_range = 1.0 / self.hidden ** (1/2)
        # 注意权矩阵的大小，这里采用全连接
        # normal功能：对高斯分布的数据进行随机采样
        # normal参数：loc-数据的均值（中心），scale-标准差（取值范围），size-整数表示采样个数，元组表示采样结果的维度
        self.wi = np.random.normal(loc = 0.0, scale = input_range, size = (self.input, self.hidden))
        self.wo = np.random.normal(loc = 0.0, scale = output_range, size = (self.hidden, self.output))

        # 创建0数组作为层更改的占位符
        # 基于在接下来的迭代中权重需要改变多少
        self.ci = np.zeros((self.input, self.hidden))
        self.co = np.zeros((self.hidden, self.output))

    #构建正向网络过程
    def feedForward(self, inputs) : 
        """
        :param inputs:输入数据
        :return : 更新的激活输出数据
        """
        if len(inputs) != self.input - 1: #传入符合input大小的inputs
            raise ValueError("inputs的值错误")

        for i in range(self.input - 1):
            self.ai[i] = inputs[i]

        for j in range(self.hidden) : # 一次计算每个隐藏神经元的输出值
            sum = 0.0
            for i in range(self.input):
                sum += self.a[i] * self.wi[i][j] # self.wi中每一列表示输入层在该隐藏神经元中的权重 
            self.ah[j] = tanh(sum)

        for k in range(self.output):
            sum = 0.0
            for j in range(self.hidden):
                sum += self.ah[j] * self.wo[j][k]
            self.ao[k] = sigmoid(sum)

        return self.ao[:] #输出多个值
    
    #构造反馈过程
    def backPropagate(self, targets):
        """
        targets: 实际输出值
        """
        if len(targets) != self.output:
                raise ValueError('targets的值错误')
        
        # 计算输出层的输入误差（隐藏层所有神经元在输出层一个神经元的误差和）
        output_deltas = [0.0] * self.output
        for k in range(self.output):
            error = -(targets[k] - self.ao[k])
            output_deltas[k] = dsigmoid(self.ao[k]) * error  #输出层的输入误差

        # 计算隐藏层的输入误差
        hidden_deltas = [0.0] * self.hidden
        for j in range(self.hidden):
            error = 0.0
            for k in range(self.output):
                # 计算第j个隐藏层神经元误差
                # self.wo[j][k]是第j个隐藏层神经元对输出层第k个神经元的误差权重
                error += output_deltas[k] * self.wo[j][k]
            hidden_deltas[j] = dtanh(self.ah[j]) * error
        
        # 更新隐藏层和输出层之间的权重
        for j in range(self.hidden):
            for k in range(self.output):
                change = output_deltas[k] * self.ah[j]
                self.wo[j][k] -= self.learning_rate * change + self.co[j][k] * self.momentum
                self.co[j][k] = change

        # 更新输入层和输出层之间的权重
        for i in range(self.input):
            for j in range(self.hidden):
                change = hidden_deltas[j] * self.ai[i]
                self.wi[i][j] -= self.learning_rate * change + self.ci[i][j] * self.momentum
        
        # 计算均方误差
        error = 0.0
        for k in range(len(targets)):
            error += 0.5 * (targets[k] - self.ao[k]) ** 2
        return error
    
    def test(self, patterns):

        for p in patterns:
            print(p[1], '->', self.feedForward(p[0]))

    def train(self, patterns):
        for i in range(self.iterations):
            error = 0.0
            random.shuffle(patterns)
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.feedForward(inputs)
                error += self.backPropagate(targets)
            with open('error.txt', 'a') as errorfile:
                errorfile.write(str(error) + '\n')
                errorfile.close()
            if i % 10 == 0:
                print('error %-.5f' % error)
            # 减小学习率，提高收敛精度
            self.learning_rate = self.learning_rate * (self.learning_rate / (self.learning_rate + (self.learning_rate * self.rate_decay)))

    def predict(self, X):
        """
        return list of predictions after training algorithm
        """
        predictions = []
        for p in X:
            predictions.append(self.feedForward(p))
        return predictions