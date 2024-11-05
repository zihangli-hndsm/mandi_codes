import os

# 定义文件后缀列表
file_suffixes = ['WL1.txt', 'WL2.txt', 'SST.txt']

# 获取当前文件夹路径
current_folder = os.getcwd()

# 输出文件夹路径
output_folder = os.path.join(current_folder, 'op')

# 创建输出文件夹（如果不存在的话）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历当前文件夹中的所有文件
for filename in os.listdir(current_folder):
    # 检查文件是否以指定后缀结尾
    if any(filename.endswith(suffix) for suffix in file_suffixes):
        # 构建文件的完整路径
        input_file_path = os.path.join(current_folder, filename)

        # 打开并读取文件内容
        with open(input_file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if lines:
            # 第一行保持不变
            first_line = lines[0].strip()

            # 后面的行合并成一行，用空格隔开
            combined_lines = ' '.join(line.strip() for line in lines[1:])

            # 将第一行和合并后的行组合
            output_content = first_line + '\n' + combined_lines

            # 构建输出文件的路径
            output_file_path = os.path.join(output_folder, filename)

            # 将结果写入到输出文件
            with open(output_file_path, 'w', encoding='utf-8') as f_out:
                f_out.write(output_content)

print("处理完成，文件已输出到 'op' 文件夹。")
