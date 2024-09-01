import os

# 当前目录
current_directory = os.getcwd()
print(f"Current directory: {current_directory}")

# 获取.py文件所在的目录
file_directory = os.path.dirname(os.path.abspath(__file__))
print(f"File directory: {file_directory}")

word_counts = {}


# 循环处理所有.txt文件
for i in range(1, 579):  # 578个文件，从1到578
    txt_filename = os.path.join(file_directory, f'{i}.txt')
    
    # 检查文件是否存在
    if os.path.exists(txt_filename):
        # 读取文本文件内容
        with open(txt_filename, 'r', encoding='utf-8') as file:
            text_content = file.read()
        print(f'File {i}.txt has {len(text_content)} characters.')
        # 计算单词数
        word_count = len(text_content.split())
        
        # 将单词数存储在字典中
        word_counts[i] = word_count

# 打印每个文件的单词数
for file_index, count in word_counts.items():
    print(f'File {file_index}.txt has {count} words.')
    
print(f"Altogehter, there are {sum(word_counts.values())} words in the corpus.")