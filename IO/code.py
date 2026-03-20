# '''
# # UTTNH
# folder_path = Path(r"E:\SteamLibrary\steamapps\workshop\content\394360\3413890094\common\technologies")
# in_file_list = [f for f in folder_path.iterdir() if f.is_file()]
# # rt56
# in_file_list = [
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\air_techs.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\artillery.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\infantry_extra_tech.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\naval.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\armor.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\bba_air_techs.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\industry.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\NaW_unique_technologies.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\electronic_mechanical_engineering.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\infantry.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\r56_techs.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\r56_special_projects_techs.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\support.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\r56e_etax.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\r56_country_techs.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\NSB_armor.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\r56_vechicles.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\special_forces_doctrine.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\MTG_naval_Support.txt",
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\MTG_naval.txt",
# ]
# VNR
# in_file_list = [
#     r"E:\SteamLibrary\steamapps\workshop\content\394360\1778255798\common\technologies\MTG_naval.txt"
# ]
# VURC
# in_file_list = [
#     r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\air_techs.txt",
#     r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\armor.txt",
#     r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\artillery.txt",
#     r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\bba_air_techs.txt",
#     r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\COMPATCH_r56_ban.txt",
#     r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\electronic_mechanical_engineering.txt",
#     r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\industry.txt",
#     r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\infantry.txt",
#     r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\NSB_armor.txt",
#     # r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\r56_vechicles.txt",
#     r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\special_forces_doctrine.txt",
#     r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\support.txt",
#     r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\VUC_replace_tech.txt"
# ]
# '''

from pathlib import Path
import re

# --- 配置区 ---
# 主列表（你正在开发的 Compatch Mod）
main_files_paths = [
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\air_techs.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\armor.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\artillery.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\bba_air_techs.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\COMPATCH_r56_ban.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\electronic_mechanical_engineering.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\industry.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\infantry.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\NSB_armor.txt",
    # r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\r56_vechicles.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\special_forces_doctrine.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\support.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\common\technologies\VUC_replace_tech.txt",

    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR+UTTH\common\technologies\MTG_naval.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR+UTTH\common\technologies\MTG_naval_Support.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR+UTTH\common\technologies\naval.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR+UTTH\common\technologies\VUC_replace_tech.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR+UTTH\common\technologies\VUCE_ex_tech.txt",
    r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR+UTTH\common\technologies\VUCE_naval.txt"
    # 注意：VUC_replace_tech 这种不重名的文件通常不需要对比覆盖，除非你想合并它
]

# 外部列表（原版或 Workshop Mod 的路径）
external_files_paths = [
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\air_techs.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\artillery.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\infantry_extra_tech.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\naval.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\armor.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\bba_air_techs.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\industry.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\NaW_unique_technologies.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\electronic_mechanical_engineering.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\infantry.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\r56_techs.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\r56_special_projects_techs.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\support.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\r56e_etax.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\r56_country_techs.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\NSB_armor.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\r56_vechicles.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\special_forces_doctrine.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\MTG_naval_Support.txt",
    r"E:\SteamLibrary\steamapps\workshop\content\394360\820260968\common\technologies\MTG_naval.txt",

]

out_file_path = r"E:\Documents\Paradox Interactive\Hearts of Iron IV\mod\VNR + UTTNH + RT56\IO\patch_missing_techs.txt"

# --- 核心提取函数（保持原始逻辑） ---
def preprocess_hoi4_text(in_file_path) -> list[str]:
    try:
        with open(in_file_path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        cleaned_lines = []
        for line in lines:
            line = line.split('#', 1)[0].strip()
            if line: cleaned_lines.append(line)
        new_str = ' '.join(cleaned_lines)
        if new_str.startswith('technologies = {'):
            new_str = new_str[len('technologies = {'):-1]
            return parse_tech_names(new_str, in_file_path)
    except Exception:
        pass
    return []

def parse_tech_names(flat_text: str, in_file_path: str) -> list[str]:
    def extract_braced_block(s: str, start: int):
        depth = 0
        for i in range(start, len(s)):
            if s[i] == '{': depth += 1
            elif s[i] == '}':
                depth -= 1
                if depth == 0: return s[start+1:i].strip(), i + 1
        return "", len(s)

    tech_list = []
    pattern = re.compile(r'(\w+)\s*=\s*{')
    pos = 0
    while pos < len(flat_text):
        match = pattern.search(flat_text, pos)
        if not match: break
        block_start = match.end() - 1
        _, block_end = extract_braced_block(flat_text, block_start)
        pos = block_end
        tech_list.append(match.group(1))
    print(f"-----------------------------\n{in_file_path}:\n{tech_list}")
    return tech_list

# --- 改进的全局对比逻辑 ---

# 1. 建立主列表的“全局科技池”
main_global_pool = set()
main_file_stems = set() # 记录主列表里有哪些文件被覆盖了

for f in main_files_paths:
    path = Path(f)
    if path.exists():
        ids = preprocess_hoi4_text(str(path))
        main_global_pool.update(ids)
        main_file_stems.add(path.name)

# 2. 检查外部文件
diff_output = []

for f in external_files_paths:
    path = Path(f)
    # 只有当该文件名在主列表中出现（意味着你试图覆盖它）时，才检查它是否缺科技
    if path.name in main_file_stems:
        ext_techs = preprocess_hoi4_text(str(path))
        # 核心判断：外部文件里的 ID，是否在主列表的【任意一个】文件里出现过？
        missing_ids = [tid for tid in ext_techs if tid not in main_global_pool]

        if missing_ids:
            diff_output.append(f"# --- Missing in your Mod (from external {path.name}) ---")
            for tid in missing_ids:
                diff_output.append(f"{tid} = {{ research_cost = 1 }}")
            diff_output.append("")

# 3. 输出
with open(out_file_path, "w", encoding="utf-8") as f:
    f.write("\n".join(diff_output))

print(f"对比完成！全局池共有 {len(main_global_pool)} 个科技。")