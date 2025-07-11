import os

folder = "hadaitainomonode"
for filename in os.listdir(folder):
    if filename.endswith(".md"):
        path = os.path.join(folder, filename)
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # 删除所有只包含 <br> 的行
        lines = [line for line in lines if line.strip() != "<br>"]
        # 检查分隔线前是否有空行，没有则加一行空行
        if lines and lines[-1].strip() == "---":
            if len(lines) > 1 and lines[-2].strip() != "":
                lines.insert(-1, "\n")
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(lines)