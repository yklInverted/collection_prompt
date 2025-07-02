#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import random
import time

class RandomTextWindow:
    def __init__(self):
        # 定义文本列表
        self.text_list1 = ['第二栏', '第三栏', '第四栏']
        self.text_list2 = ['门关闭', '门开一小半', '门开一半','门开一大半']
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("随机文本显示器")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # 设置窗口居中
        self.center_window()
        
        # 创建样式
        style = ttk.Style()
        style.configure('Large.TLabel', font=('Arial', 80, 'bold'))
        
        # 创建标签显示文本
        self.text_label = ttk.Label(
            self.root, 
            text="", 
            style='Large.TLabel',
            anchor='center',
            justify='center'
        )
        self.text_label.pack(expand=True, fill='both', padx=20, pady=20)
        
        # 创建控制按钮框架
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)
        
        # 添加手动刷新按钮
        refresh_button = ttk.Button(
            button_frame, 
            text="手动刷新", 
            command=self.update_text
        )
        refresh_button.pack(side='left', padx=5)
        
        # 添加退出按钮
        exit_button = ttk.Button(
            button_frame, 
            text="退出", 
            command=self.root.quit
        )
        exit_button.pack(side='left', padx=5)
        
        # 添加状态标签
        self.status_label = ttk.Label(
            self.root, 
            text="每2秒自动刷新", 
            font=('Arial', 10),
            foreground='gray'
        )
        self.status_label.pack(pady=(0, 10))
        
        # 初始显示
        self.update_text()
        
        # 开始定时刷新
        self.schedule_update()
    
    def center_window(self):
        """将窗口居中显示"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def update_text(self):
        """更新显示的文本"""
        random_text = random.choice(self.text_list1) + ' ' + random.choice(self.text_list2)
        self.text_label.config(text=random_text)
        
        # 更新状态显示当前时间
        current_time = time.strftime("%H:%M:%S")
        self.status_label.config(text=f"最后更新: {current_time} | 每2秒自动刷新")
    
    def schedule_update(self):
        """安排下一次更新"""
        self.update_text()
        # 2秒后再次调用
        self.root.after(10000, self.schedule_update)
    
    def run(self):
        """运行应用程序"""
        try:
            print("随机文本显示器已启动...")
            # print("文本列表:", self.text_list)
            print("按Ctrl+C或点击'退出'按钮关闭程序")
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\n程序被用户中断")
        finally:
            print("程序已关闭")

def main():
    """主函数"""
    # 确保在conda环境中运行的提示
    print("请确保您正在'lerobot' conda环境中运行此脚本")
    print("如果不在正确的环境中，请运行: conda activate lerobot")
    print("-" * 50)
    
    # 创建并运行应用程序
    app = RandomTextWindow()
    app.run()

if __name__ == "__main__":
    main()
