import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

def setup_chinese_font():
    """设置中文字体支持"""
    try:
        # 检查系统是否有中文字体
        available_fonts = [f.name for f in fm.fontManager.ttflist]
        chinese_fonts = [f for f in available_fonts if any(keyword in f.lower() 
                        for keyword in ['noto', 'microsoft', 'simhei', 'simkai', 'simsun', 'yahei', 'source', 'droid'])]
        
        if chinese_fonts:
            # 使用系统中找到的第一个中文字体
            plt.rcParams['font.sans-serif'] = chinese_fonts + ['DejaVu Sans']
            plt.rcParams['axes.unicode_minus'] = False
            print(f"使用字体: {chinese_fonts[0]}")
            return True
        else:
            # 使用内置字体，但不会显示中文
            plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
            plt.rcParams['axes.unicode_minus'] = False
            print("未找到中文字体，使用英文标签")
            return False
            
    except Exception as e:
        print(f"字体配置失败: {e}")
        return False

def visualize_classification_dataset():
    # 读取数据集
    df = pd.read_csv('classification_dataset.csv')
    
    # 设置中文字体
    use_chinese = setup_chinese_font()
    
    # 创建图形
    plt.figure(figsize=(10, 8))
    
    # 为不同类别设置不同颜色和标记
    colors = ['red', 'blue', 'green']
    markers = ['o', 's', '^']
    if use_chinese:
        labels = ['类别 0', '类别 1', '类别 2']
        title_text = 'AI分类任务教学数据集\n二维散点分布可视化'
        xlabel_text = '特征 X'
        ylabel_text = '特征 Y'
        info_text = f'总样本数: {len(df)}\n每类样本数: {len(df)//3}\n特征维度: 2'
    else:
        labels = ['Class 0', 'Class 1', 'Class 2']
        title_text = 'AI Classification Dataset\nScatter Plot Visualization'
        xlabel_text = 'Feature X'
        ylabel_text = 'Feature Y'
        info_text = f'Total samples: {len(df)}\nSamples per class: {len(df)//3}\nFeature dimensions: 2'
    
    # 绘制每个类别的散点
    for i in range(3):
        class_data = df[df['label'] == i]
        plt.scatter(class_data['x'], class_data['y'], 
                   c=colors[i], marker=markers[i], 
                   alpha=0.7, s=60, label=labels[i])
    
    # 添加标题和标签
    plt.title(title_text, fontsize=16, fontweight='bold')
    plt.xlabel(xlabel_text, fontsize=14)
    plt.ylabel(ylabel_text, fontsize=14)
    
    # 添加图例
    plt.legend(fontsize=12, loc='upper left')
    
    # 添加网格
    plt.grid(True, alpha=0.3)
    
    # 设置坐标轴范围
    plt.xlim(-1, 8)
    plt.ylim(-1, 8)
    
    # 添加统计信息文本
    plt.text(0.02, 0.98, info_text, transform=plt.gca().transAxes, 
             fontsize=10, verticalalignment='top', 
             bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))
    
    # 调整布局
    plt.tight_layout()
    
    # 保存图像
    plt.savefig('classification_dataset_visualization_fixed.png', dpi=300, bbox_inches='tight')
    print("修复的可视化图像已保存为 'classification_dataset_visualization_fixed.png'")
    
    # 显示统计信息
    print(f"\n数据集统计:")
    print(f"- 总样本数: {len(df)}")
    print(f"- 类别分布: {dict(df['label'].value_counts().sort_index())}")
    print(f"- X坐标范围: [{df['x'].min():.2f}, {df['x'].max():.2f}]")
    print(f"- Y坐标范围: [{df['y'].min():.2f}, {df['y'].max():.2f}]")

if __name__ == "__main__":
    visualize_classification_dataset()