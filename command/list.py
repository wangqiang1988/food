import os

def list_md_files():
    md_files = []
    current_dir = os.getcwd()  # 获取当前工作目录

    for file in os.listdir(current_dir):  # 遍历当前目录下的所有文件和文件夹
        if file.endswith(".md"):  # 如果文件名以 ".md" 结尾，则添加到列表中
            file_name = os.path.splitext(file)[0]  # 去除文件扩展名
            md_files.append(file_name)

    return md_files

if __name__ == "__main__":
    md_files = list_md_files()
    print("Markdown 文件列表:")
    print(md_files)
