import hashlib
import rich.progress
import sys
import tkinter as tk
from tkinter import filedialog


# 计算sha256 和 md5 hash
def calc_hash(file_path, chunk_size=2**20, hash_type="sha256"):
    # 创建sha256 hash对象
    hash_object = hashlib.new(hash_type)

    # 以二进制模式打开文件
    with rich.progress.open(file_path, "rb") as file:
        # 创建rich进度条
        for chunk in iter(lambda: file.read(chunk_size), b""):
            # 更新hash对象
            hash_object.update(chunk)
        # 获取十六进制编码的哈希值
        return hash_object.hexdigest()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    # 程序结束后循环运行
    while True:
        input_type = input(
            "0.退出\n1.sha256\n2.md5\n默认选择1.sha256\n请输入hash类型或退出:"
        )
        if input_type == "0":
            sys.exit(0)
        hash_type = "md5" if input_type == "2" else "sha256"
        file_path = filedialog.askopenfilename()
        if not file_path:
            print("未选择文件")
            continue
        hash_value = calc_hash(file_path=file_path, hash_type=hash_type)
        print(f"HASH值:{hash_value}")
