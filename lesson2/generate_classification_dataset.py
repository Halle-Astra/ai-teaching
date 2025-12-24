import numpy as np
import pandas as pd

np.random.seed(42)

def generate_classification_dataset():
    # 生成三个类别的二维散点数据
    n_samples_per_class = 100
    
    # 类别1: 左下角区域
    class1_x = np.random.normal(2, 0.8, n_samples_per_class)
    class1_y = np.random.normal(2, 0.8, n_samples_per_class)
    class1_label = np.ones(n_samples_per_class, dtype=int) * 0
    
    # 类别2: 右上角区域
    class2_x = np.random.normal(6, 0.8, n_samples_per_class)
    class2_y = np.random.normal(6, 0.8, n_samples_per_class)
    class2_label = np.ones(n_samples_per_class, dtype=int) * 1
    
    # 类别3: 右下角区域
    class3_x = np.random.normal(6, 0.8, n_samples_per_class)
    class3_y = np.random.normal(2, 0.8, n_samples_per_class)
    class3_label = np.ones(n_samples_per_class, dtype=int) * 2
    
    # 合并所有数据
    x = np.concatenate([class1_x, class2_x, class3_x])
    y = np.concatenate([class1_y, class2_y, class3_y])
    labels = np.concatenate([class1_label, class2_label, class3_label])
    
    # 创建DataFrame
    df = pd.DataFrame({
        'x': x,
        'y': y,
        'label': labels
    })
    
    # 随机打乱数据
    df = df.sample(frac=1).reset_index(drop=True)
    
    return df

if __name__ == "__main__":
    # 生成数据集
    dataset = generate_classification_dataset()
    
    # 保存为CSV
    dataset.to_csv('classification_dataset.csv', index=False)
    
    print("数据集已生成并保存为 'classification_dataset.csv'")
    print(f"数据集包含 {len(dataset)} 个样本，3个类别")
    print("数据集预览:")
    print(dataset.head(10))
    print("\n类别分布:")
    print(dataset['label'].value_counts().sort_index())