import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from urllib.request import urlretrieve
import os

def setup_chinese_font():
    # 下载开源中文字体 Noto Sans CJK SC
    font_url = 'https://github.com/googlefonts/noto-cjk/raw/main/Sans/SubsetOTF/SC/NotoSansCJKsc-Regular.otf'
    font_path = '/tmp/NotoSansCJKsc-Regular.otf'
    
    try:
        print("正在下载中文字体...")
        urlretrieve(font_url, font_path)
        
        # 将字体添加到matplotlib
        fm.fontManager.addfont(font_path)
        plt.rcParams['font.sans-serif'] = ['Noto Sans CJK SC', 'DejaVu Sans']
        plt.rcParams['axes.unicode_minus'] = False
        
        print(f"字体已下载到: {font_path}")
        print("matplotlib已配置为使用中文字体")
        return True
        
    except Exception as e:
        print(f"下载字体失败: {e}")
        print("将使用英文标签")
        return False

if __name__ == "__main__":
    setup_chinese_font()