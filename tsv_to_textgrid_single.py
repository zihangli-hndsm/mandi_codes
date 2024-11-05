import pandas as pd
from praatio import textgrid
import os

def tsv_to_textgrid(tsv_file_path, textgrid_file_path):
    # 读取 TSV 文件
    df = pd.read_csv(tsv_file_path, sep='\t')
    df = df.fillna('spn')
    # 将时间从毫秒转换为秒
    interval_list = []
    for index, row in df.iterrows():
        start_time = row['start'] / 1000.0  # 转换为秒
        end_time = row['end'] / 1000.0      # 转换为秒
        text = row['text']
        
        interval_list.append((start_time, end_time, text))
    
    # 创建 TextGrid 对象并添加 tier
    tg = textgrid.Textgrid()
    tier = textgrid.IntervalTier("word", interval_list, 0, str(interval_list[-1][1]))
    
    tg.addTier(tier)
    
    # 将 TextGrid 写入到文件
    tg.save(textgrid_file_path, format="long_textgrid", includeBlankSpaces=True)
    print('finished')
list_dir = os.listdir('./')
for f in list_dir:
    print('considering', f)
    if f.endswith('.tsv') and 'WL1' not in f:
        tsv_to_textgrid(f, './op/' + f[:-4] + '.TextGrid')