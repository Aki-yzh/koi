import os

folder = "hadaitainomonode"
for filename in os.listdir(folder):
    if filename.endswith(".md"):
        path = os.path.join(folder, filename)
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # 查找分隔线位置
        if lines and lines[-1].strip() == "---":
            content_lines = lines[:-1]
            sep_line = lines[-1]
        else:
            content_lines = lines
            sep_line = "---\n"
        # 判断是否需要补行
        total = len(content_lines)
        if total < 24:
            content_lines += ["<br>\n"] * (24 - total)
        # 补一行空行
        if len(content_lines) < 25:
            content_lines.append("\n")
        # 重新写入
        new_lines = content_lines + [sep_line]
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)