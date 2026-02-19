'''
用于比对文件gfx条目，并生成替换后的文件
'''

import os
import re

def preprocess_gfx(content):
    """预处理：去注释、单行化、压缩空格"""
    # 删除 # 之后的注释
    content = re.sub(r'#.*', '', content)
    # 将换行符换成空格，随后压缩连续空格
    content = content.replace('\n', ' ').replace('\r', ' ')
    content = re.sub(r'\s+', ' ', content)
    return content.strip()

def get_all_entries_from_list(file_list):
    """
    遍历文件列表，提取所有 spriteType 块。
    返回字典: { "clean_name": "完整的块文本" }
    """
    all_entries = {}

    # 核心正则：匹配 spriteType = { ... }，忽略大小写
    # 使用非贪婪匹配 .*? 确保匹配到最近的结束括号
    block_pattern = re.compile(r'spriteType\s*=\s*\{.*?\}', re.IGNORECASE)
    # 匹配 name 字段，忽略大小写，兼容引号
    name_pattern = re.compile(r'name\s*=\s*"?([\w.:/-]+)"?', re.IGNORECASE)

    for file_path in file_list:
        if not os.path.exists(file_path):
            print(f"警告: 文件未找到 {file_path}")
            continue
        print(f"正在处理{file_path}")
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            clean_content = preprocess_gfx(f.read())

            # 1. 找到所有 spriteType 块
            blocks = block_pattern.findall(clean_content)

            for block in blocks:
                # 2. 在块内找 name
                name_match = name_pattern.search(block)
                if name_match:
                    # 统一转为小写作为 Key，实现逻辑上的“忽略大小写去重”
                    # 但保留 block 的原始文本用于输出
                    name_key = name_match.group(1).lower()
                    all_entries[name_key] = block

    return all_entries

def merge_gfx_lists(list1, list2, output_folder):
    print("开始处理列表 1...")
    dict1 = get_all_entries_from_list(list1)

    print("开始处理列表 2...")
    dict2 = get_all_entries_from_list(list2)

    # 找出共同的条目
    common_names = set(dict1.keys()) & set(dict2.keys())

    if not common_names:
        print("未发现匹配的相同条目。")
        return

    # 创建输出目录并写入文件
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, "VUC_merged.gfx")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("spriteTypes = {\n")
        for name in common_names:
            # 提取第二个列表（List 2）中的对应数据
            f.write(f"\t{dict2[name]}\n")
        f.write("}")

    print(f"--- 成功 ---")
    print(f"共发现 {len(common_names)} 个重复项。")
    print(f"已将来自【列表 2】的数据提取至: {output_file}")


def get_gfx_file_list(folder_path):
    """
    遍历指定文件夹及其子文件夹，返回所有 .gfx 文件的绝对路径列表
    """
    gfx_files = []

    # 检查路径是否存在
    if not os.path.exists(folder_path):
        print(f"错误: 文件夹路径不存在 -> {folder_path}")
        return []

    # os.walk 会递归遍历所有子目录
    for root, _, files in os.walk(folder_path):
        for file in files:
            # 检查后缀是否为 .gfx (忽略大小写)
            if file.lower().endswith('.gfx'):
                full_path = os.path.join(root, file)
                # 使用 abspath 转换为绝对路径，避免相对路径带来的混淆
                gfx_files.append(os.path.abspath(full_path))

    print(f"已在 {folder_path} 中找到 {len(gfx_files)} 个 .gfx 文件。")
    return gfx_files


if __name__ == "__main__":
    out_dir = r"interface\src"
    # 设定你的两个 Mod 或 文件夹 路径
    dir_utt = r"interface\src\dir_utt"
    dir_b = r"interface\src\dir2"
    list_utt = get_gfx_file_list(dir_utt)
    # list_a = list_utt
    dir_r56 = r"interface\src\dir_r56"
    list_r56 = get_gfx_file_list(dir_r56)
    list_a = list_utt + list_r56

    list_b = get_gfx_file_list(dir_b)


    # 然后调用之前的合并函数
    merge_gfx_lists(list_a, list_b, out_dir)