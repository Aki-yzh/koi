import os

folder = "hadaitainomonode"
for filename in os.listdir(folder):
    if filename.endswith(".md"):
        path = os.path.join(folder, filename)
        with open(path, "a", encoding="utf-8") as f:
            f.write("\n---\n")