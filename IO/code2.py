with open(r'common\technologies\COMPATCH_r56_ban.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

# 统计非注释行的出现次数（忽略前后空格）
non_comment_counts = {}
for line in lines:
    stripped = line.strip()
    if stripped and not stripped.startswith('#'):
        non_comment_counts[stripped] = non_comment_counts.get(stripped, 0) + 1

# 保留注释、空行，以及仅出现一次的非注释行
result = []
for line in lines:
    stripped_line = line.strip()
    if stripped_line.startswith('#'):
        result.append(line)
    elif stripped_line == '':
        result.append(line)
    else:
        if non_comment_counts.get(stripped_line, 0) == 1:
            result.append(line)

# 输出处理后的内容
with open(r"IO\out.txt", "w", encoding="utf-8") as f:
    f.write('\n'.join(result))