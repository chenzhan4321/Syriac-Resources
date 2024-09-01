import os
from bs4 import BeautifulSoup

# 当前目录
current_directory = os.getcwd()

# 循环处理所有HTML文件
for i in range(1, 578):  # 577个文件，从1到577
    input_filename = os.path.join(current_directory, f'{i}.html')
    output_filename = os.path.join(current_directory, f'{i}.txt')
    
    # 读取HTML文件
    if os.path.exists(input_filename):
        with open(input_filename, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(html_content, 'html.parser')

        # 查找所有lang="syr"的元素，表示Syriac文本
        syriac_elements = soup.find_all(lang="syr")

        # 提取这些元素中的文本内容，保留空格
        syriac_texts = []
        for element in syriac_elements:
            text = ' '.join(element.stripped_strings)
            syriac_texts.append(text)

        # 将所有提取的Syriac文本合并成一个字符串
        cleaned_syriac_text = ' '.join(syriac_texts)

        # 将提取的文本写入一个文件
        with open(output_filename, 'w', encoding='utf-8') as text_file:
            text_file.write(cleaned_syriac_text)

print("提取完成。")