"""
本脚本主要用于表示如何使用One-Class SVM进行异常检测任务。以及进行学习
参考资料： https://scikit-learn.cn/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM

文档中关于y的说明
fit(X, y=None, sample_weight=None)[源代码]
检测样本集 X 的软边界。

参数:
X
shape 为 (n_samples, n_features) 的 {array-like, sparse matrix}
样本集，其中 n_samples 是样本数量，n_features 是特征数量。

y 被忽略
未使用，按照惯例为保持 API 一致性而存在。

sample_weight
shape 为 (n_samples,) 的 array-like, default=None
每个样本的权重。为每个样本重新缩放 C。更高的权重会迫使分类器更加重视这些点。

"""

# 读数据
import pandas as pd 
import numpy as np 
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

from sklearn.svm import OneClassSVM

model_instance = OneClassSVM()
#####假设已经有了模型######################
# breakpoint()
#####求解模型中的参数，训练##########
# 3， 开始训练
model_instance.fit(data[['x','y']], data['label']) #发动训练

print('训练结束')
#####这个时候的模型按理已经是一个可以对没见过的样本数据进行预测的一个模型了，这个时候就只需要考虑怎么用，或者评估
# 4， 更加精确的评估这个模型是不是真的没问题真的好用，即，验证

yy = model_instance.predict(np.array(data[['x','y']]))
print('yy的值', np.unique(yy))
# 绘制决策边界和预测结果
import matplotlib.pyplot as plt
# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'SimHei']  # Linux下用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 创建网格来绘制决策边界
h = 0.02  # 网格步长
xx, yy_grid = np.meshgrid(np.arange(data['x'].min() - 1, data['x'].max() + 1, h),
                         np.arange(data['y'].min() - 1, data['y'].max() + 1, h))

# 在网格上进行预测
grid_points = np.c_[xx.ravel(), yy_grid.ravel()]
Z = model_instance.predict(grid_points)
Z = Z.reshape(xx.shape)

# 创建图形
plt.figure(figsize=(10, 8))

# 绘制决策边界
plt.contourf(xx, yy_grid, Z, levels=[-1, 0, 1], colors=['lightcoral', 'lightblue'], alpha=0.6)
plt.contour(xx, yy_grid, Z, levels=[0], colors='black', linewidths=2)

# 绘制数据点
colors = ['red' if i == -1 else 'green' for i in yy]
plt.scatter(data['x'], data['y'], c=colors, s=50, edgecolors='black', alpha=0.7)

# 添加标签和标题
plt.xlabel('X Feature')
plt.ylabel('Y Feature')
plt.title('One-Class SVM Decision Boundary and Results')
# 创建图例，使用英文避免中文显示问题
outlier_patch = plt.scatter([], [], c='red', label='Outliers')
normal_patch = plt.scatter([], [], c='green', label='Normal Points')
plt.legend(handles=[normal_patch, outlier_patch])

plt.savefig('pics/ocsvm_result_with_boundary.png', dpi=150, bbox_inches='tight')
plt.show()