import tkinter as tk
from tkinter import messagebox
import os

class ResourcePackGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("XIAOQING的资源包生成器")
        self.root.geometry("300x150")

        # 创建变量
        self.n = tk.StringVar()

        # 创建输入框和按钮
        self.label = tk.Label(root, text="资源包序号:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root, textvariable=self.n)
        self.entry.pack(pady=5)

        self.generate_button = tk.Button(root, text="生成", command=self.generate_resource_pack)
        self.generate_button.pack(pady=10)

    def generate_resource_pack(self):
        try:
            # 获取输入的资源包序号
            pack_number = int(self.n.get())

            # 创建Resource Pack文件夹
            pack_folder_path = os.path.join(os.getcwd(), "Resource Pack")
            os.makedirs(pack_folder_path, exist_ok=True)

            # 在Resource Pack文件夹内创建assets文件夹
            assets_folder_path = os.path.join(pack_folder_path, "assets")
            os.makedirs(assets_folder_path, exist_ok=True)

            # 在Resource Pack文件夹内创建pack.mcmeta文件
            mcmeta_content = '{"pack": {"pack_format": ' + str(pack_number) + ', "description":"\\u00A76Your resource pack"}}'
            mcmeta_file_path = os.path.join(pack_folder_path, "pack.mcmeta")
            with open(mcmeta_file_path, 'w') as mcmeta_file:
                mcmeta_file.write(mcmeta_content)

            messagebox.showinfo("成功", "资源包生成成功！")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的资源包序号！")

if __name__ == "__main__":
    root = tk.Tk()
    app = ResourcePackGenerator(root)
    root.mainloop()
