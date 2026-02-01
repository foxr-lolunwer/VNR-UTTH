import os

def sync_vnr_files_in_subfolders():
    # 获取脚本当前所在的目录
    base_dir = os.getcwd()
    
    # 定义需要处理的子文件夹名称
    target_subfolders = ['simp_chinese', 'english']

    for folder_name in target_subfolders:
        folder_path = os.path.join(base_dir, folder_name)
        
        # 检查文件夹是否存在
        if not os.path.isdir(folder_path):
            print(f"--- 跳过：找不到目录 {folder_name} ---")
            continue

        print(f"\n--- 正在处理目录: {folder_name} ---")
        
        # 获取该文件夹下所有文件
        try:
            all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        except Exception as e:
            print(f"读取目录 {folder_name} 出错: {e}")
            continue

        # 区分前缀文件 (区分大小写)
        vnr_prefixed = [f for f in all_files if f.startswith('VNR_')]
        # 非前缀文件
        others = [f for f in all_files if not f.startswith('VNR_')]

        for file in others:
            # 获取文件的完整路径
            current_file_path = os.path.join(folder_path, file)
            
            # 过滤逻辑：只处理 .yml 且不以 FL_ 开头的文件
            if file.startswith('FL_') or not file.endswith('.yml'):
                print(f"[跳过] 非目标文件：{file}")
                continue

            target_name = "VNR_" + file
            target_file_path = os.path.join(folder_path, target_name)

            if target_name in vnr_prefixed:
                # 情况 1：存在匹配的 VNR_ 文件 -> 执行替换
                print(f"[替换] 发现匹配：{file} -> {target_name}")
                try:
                    os.remove(target_file_path)   # 删除旧的 VNR_ 文件
                    os.rename(current_file_path, target_file_path) # 将当前文件更名为 VNR_
                except Exception as e:
                    print(f"      替换失败: {e}")
            else:
                # 情况 2：没有匹配的 VNR_ 前缀文件 -> 直接删除
                print(f"[删除] 无匹配 VNR_ 前缀：{file}")
                try:
                    os.remove(current_file_path)
                except Exception as e:
                    print(f"      删除失败: {e}")

    print("\n所有指定目录处理完成。")

if __name__ == "__main__":
    sync_vnr_files_in_subfolders()