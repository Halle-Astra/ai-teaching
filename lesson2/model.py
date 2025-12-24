# 读数据
import pandas as pd 
#import torch 
# from torch import nn # neural network 
import os 
print(os.path.abspath(os.path.curdir))
# 1， 数据问题
data = pd.read_csv('./classification_dataset.csv') # .. 上级文件夹， . 当前文件夹 ./a==a.  /a!=a
# data[data['label']==2] = 0
# SVM, ANN, back propagation, BP-神经网络, logistic 
# 2， 选择并实现一个分类方法/模型
###########################
# 放模型代码 

# class Model:
#     def __init__(self):
#         #pass 
#         ...
    
#     def train(self):
#         ...

from sklearn.svm import LinearSVC

model_instance = LinearSVC()
#####假设已经有了模型######################
# breakpoint()
#####求解模型中的参数，训练##########
# 3， 开始训练
model_instance.fit(data[['x','y']], data['label']) #发动训练

print('训练结束')
#####这个时候的模型按理已经是一个可以对没见过的样本数据进行预测的一个模型了，这个时候就只需要考虑怎么用，或者评估
# 4， 更加精确的评估这个模型是不是真的没问题真的好用，即，验证

yy = model_instance.predict([[1.631489 , 1.010439],
                                [0,0],
                                [1,1],
                                [5.639948  ,1.479486]])
print('预测值为:', yy)
# 5， 只需要考虑怎么用了


# breakpoint()
print("执行开始")
print("执行结束")

# ANN
# 算出正确的ANN的参数 ———— 训练
    # 批量注释 ctrl + /
    # 条件：
    #     优化器：梯度下降的配置

# 保存正确的ANN参数
print("执行结束")