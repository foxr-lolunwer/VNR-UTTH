'''
用于比对文件gfx条目，并生成替换后的文件
'''

import os
import re
from dataclasses import dataclass
from typing import Dict, List, Set

# ==================== 配置类 ====================
@dataclass
class GfxConfig:
    """GFX处理配置"""
    output_folder: str
    ignore_folders: List[str]  # 忽略的文件夹列表（仅匹配 name）
    list_a_folders: List[str]  # 待检查列表 A
    list_b_folders: List[str]  # 合并参考列表 B

@dataclass
class GfxEntry:
    """单个 spriteType 条目"""
    name: str
    texture_file: str
    block_text: str

# ==================== 工具函数 ====================
def preprocess_gfx(content):
    """预处理：去注释、单行化、压缩空格"""
    # 删除 # 之后的注释
    content = re.sub(r'#.*', '', content)
    # 将换行符换成空格，随后压缩连续空格
    content = content.replace('\n', ' ').replace('\r', ' ')
    content = re.sub(r'\s+', ' ', content)
    return content.strip()

def get_gfx_file_list(folder_path: str) -> List[str]:
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

def extract_entry_info(block: str) -> GfxEntry:
    """从 spriteType 块中提取 name 和 textureFile 信息"""
    name_pattern = re.compile(r'name\s*=\s*"?([\w.:/-]+)"?', re.IGNORECASE)
    texture_pattern = re.compile(r'textureFile\s*=\s*"?([^"\s}]+)"?', re.IGNORECASE)

    name_match = name_pattern.search(block)
    texture_match = texture_pattern.search(block)
    name = name_match.group(1).lower() if name_match else ""
    texture_file = texture_match.group(1).strip() if texture_match else ""

    return GfxEntry(name=name, texture_file=texture_file, block_text=block)


def get_all_entries_from_list(file_list: List[str]) -> Dict[str, GfxEntry]:
    """
    遍历文件列表，提取所有 spriteType 块。
    
    返回字典:
    - { "clean_name": GfxEntry }
    """
    all_entries: Dict[str, GfxEntry] = {}

    # 核心正则：匹配 spriteType = { ... }，忽略大小写
    # 使用非贪婪匹配 .*? 确保匹配到最近的结束括号
    block_pattern = re.compile(r'spriteType\s*=\s*\{.*?\}', re.IGNORECASE)

    for file_path in file_list:
        if not os.path.exists(file_path):
            print(f"警告: 文件未找到 {file_path}")
            continue
        
        print(f"[处理] {file_path}")
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            clean_content = preprocess_gfx(f.read())

            # 1. 找到所有 spriteType 块
            blocks = block_pattern.findall(clean_content)

            for block in blocks:
                entry = extract_entry_info(block)
                if not entry.name:
                    continue

                # 直接存储，不再在此阶段过滤 ignore
                if entry.name in all_entries:
                    print(f"警告: 在同一列表中发现重复条目 {entry.name}，已覆盖先前的记录。")
                all_entries[entry.name] = entry

    return all_entries

def get_ignored_entry_names(ignore_folders: List[str]) -> Set[str]:
    """
    从忽略文件夹中提取所有条目的名称（仅用于最终合并时跳过）
    
    返回集合: { "entry_name1", "entry_name2", ... }
    """
    ignore_names = set()
    
    if not ignore_folders:
        return ignore_names
    
    print("\n" + "="*50)
    print("扫描忽略文件夹中的条目...")
    print("="*50)
    
    for folder in ignore_folders:
        if not os.path.exists(folder):
            print(f"警告: 忽略文件夹不存在 -> {folder}")
            continue
        
        print(f"\n扫描文件夹: {folder}")
        files = get_gfx_file_list(folder)
        entries = get_all_entries_from_list(files)  # 此处无需再次过滤 ignore
        ignore_names.update(entries.keys())
        print(f"  找到 {len(entries)} 个条目")
    
    print(f"\n总共将忽略 {len(ignore_names)} 个条目名称")
    print("="*50 + "\n")
    
    return ignore_names

def merge_gfx_lists(list_a: List[str], list_b: List[str], output_folder: str, ignore_folders: List[str] = None):
    """
    合并两个列表中的 GFX 条目（新版规则）
    
    参数:
        list_a: 待检查列表 A 的文件路径列表
        list_b: 合并参考列表 B 的文件路径列表
        output_folder: 输出文件夹
        ignore_folders: 需要忽略的文件夹列表，该文件夹中的所有条目名称在合并时会被跳过
    """
    if ignore_folders is None:
        ignore_folders = []
    
    # 提前收集忽略列表中的 name 集合（仅用于最终跳过）
    ignore_entry_names = get_ignored_entry_names(ignore_folders)
    
    print("\n" + "="*50)
    print("开始处理列表 A（待检查）...")
    print("="*50)
    dict_a = get_all_entries_from_list(list_a)

    print("\n" + "="*50)
    print("开始处理列表 B（参考）...")
    print("="*50)
    dict_b = get_all_entries_from_list(list_b)

    # 找出共同的条目（A ∩ B）
    common_names = set(dict_a.keys()) & set(dict_b.keys())

    merged_entries = []           # 替换条目（B 的 block_text）
    duplicate_texture_files = set()  # 完全相同纹理记录（B 的 textureFile）

    for name in sorted(common_names):
        # ⚠️ 核心修改：若条目名称在忽略列表中，直接跳过（不输出也不记录）
        if name in ignore_entry_names:
            continue

        entry_a = dict_a[name]
        entry_b = dict_b[name]

        if entry_a.texture_file == entry_b.texture_file:
            # 完全相同 → 记录 B 的纹理文件
            duplicate_texture_files.add(entry_b.texture_file)
        else:
            # 纹理不同 → 使用 B 的条目替换
            merged_entries.append(entry_b.block_text)

    # 创建输出目录
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, "VUC_merged.gfx")
    duplicate_file = os.path.join(output_folder, "VUC_merged_same_texture_files.txt")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("spriteTypes = {\n")
        for block_text in merged_entries:
            f.write(f"\t{block_text}\n")
        f.write("}")

    if len(duplicate_texture_files):
        with open(duplicate_file, 'w', encoding='utf-8') as f:
            for texture_file in sorted(duplicate_texture_files):
                f.write(f"{texture_file}\n")

    print("\n" + "="*50)
    print("--- 成功 ---")
    print("="*50)
    print(f"列表 A 条目总数: {len(dict_a)}")
    print(f"列表 B 条目总数: {len(dict_b)}")
    print(f"共同条目数: {len(common_names)}")
    print(f"跳过（因在忽略列表中）: {len([n for n in common_names if n in ignore_entry_names])}")
    print(f"跳过（完全相同纹理）: {len(duplicate_texture_files)}")
    print(f"生成替换条目数: {len(merged_entries)}")
    print(f"已将替换条目写入: {output_file}")
    print(f"已将相同纹理记录写入: {duplicate_file}")
    print("="*50 + "\n")

def main(config: GfxConfig):
    """主函数：执行完整的GFX合并流程"""
    print(f"开始GFX合并流程...")
    print(f"忽略文件夹: {config.ignore_folders if config.ignore_folders else '无'}")
    
    # 收集列表 A 的所有文件
    list_a_files = []
    for folder in config.list_a_folders:
        list_a_files.extend(get_gfx_file_list(folder))
    
    # 收集列表 B 的所有文件
    list_b_files = []
    for folder in config.list_b_folders:
        list_b_files.extend(get_gfx_file_list(folder))
    
    # 执行合并
    merge_gfx_lists(list_a_files, list_b_files, config.output_folder, config.ignore_folders)

# ==================== 主程序 ====================
if __name__ == "__main__":
    # 创建配置
    config = GfxConfig(
        output_folder=r"interface\src",
        ignore_folders=[
            r"interface\src\dir_ignore"  # 忽略文件夹
        ],
        list_a_folders=[
            r"interface\src\dir_utt",
            # r"interface\src\dir_r56"
        ],
        list_b_folders=[
            r"interface\src\dir2",
        ]
    )
    
    main(config)