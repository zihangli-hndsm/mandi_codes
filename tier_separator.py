import textgrid
import os

# This script removes the second tier of textgrid files, which is used to process the results of the first model

def remove_second_tier(input_file, output_file):
    # 读取 TextGrid 文件
    tg = textgrid.TextGrid.fromFile(input_file)

    # 检查是否有两个或以上的 tier
    if len(tg.tiers) < 2:
        print("Error: The TextGrid file has less than 2 tiers.")
        return

    # 移除第二个 tier（index 1 表示第二个 tier）
    tg.tiers.pop(1)

    # 将修改后的 TextGrid 写入新的文件
    tg.write(output_file)
    print(f"Modified TextGrid saved as {output_file}")


# 示例使用

input_files = os.listdir('./')
for fn in input_files:
    if fn.endswith('.TextGrid'):
        output_file = './output/' + fn
        remove_second_tier(fn, output_file)
