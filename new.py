import os

folder = "hadaitainomonode"
for filename in os.listdir(folder):
    if filename.endswith(".md"):
        path = os.path.join(folder, filename)
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # 找到最后一行分隔线的位置
        if lines and lines[-1].strip() == "---":
            # 找到倒数第一个非空行的位置
            idx = len(lines) - 2
            while idx >= 0 and lines[idx].strip() == "":
                idx -= 1
            # 保留内容+用<br>替换空行+分隔线
            new_lines = lines[:idx+1] + ["<br>\n"] * (len(lines)-idx-2) + ["---\n"]
            with open(path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)