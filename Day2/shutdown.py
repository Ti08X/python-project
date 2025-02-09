import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import os

def set_shutdown():
    try:
        # 获取并验证时间
        h, m = int(hour.get()), int(minute.get())
        if not (0 <= h <=23 and 0 <= m <=59):
            raise ValueError
        
        # 计算剩余时间
        now = datetime.now()
        target = datetime(now.year, now.month, now.day, h, m)
        if target < now: target += timedelta(days=1)
        delay = max(60, int((target - now).total_seconds()))
        
        # 设置关机
        os.system(f"shutdown /s /t {delay}")
        info = f"将在 {target.strftime('%H:%M')} 关机\n剩余时间：{delay//3600}小时{delay%3600//60}分钟"
        messagebox.showinfo("设置成功", info)
    except:
        messagebox.showerror("错误", "请输入有效时间（0-23时，0-59分）")

def cancel_shutdown():
    if os.system("shutdown /a") == 0:
        messagebox.showinfo("已取消", "定时关机计划已取消")
    else:
        messagebox.showinfo("信息", "没有正在进行的关机计划")

# 创建界面
root = tk.Tk()
root.title("定时关机")
root.geometry("250x150")

# 时间输入框
tk.Label(root, text="关机时间设置").pack(pady=5)
time_frame = tk.Frame(root)
time_frame.pack()

hour = tk.Entry(time_frame, width=3)
hour.pack(side=tk.LEFT, padx=2)
tk.Label(time_frame, text="时").pack(side=tk.LEFT)

minute = tk.Entry(time_frame, width=3)
minute.pack(side=tk.LEFT, padx=2)
tk.Label(time_frame, text="分").pack(side=tk.LEFT)

# 功能按钮
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="设定", command=set_shutdown, width=6).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="取消", command=cancel_shutdown, width=6).pack(side=tk.LEFT, padx=5)

root.mainloop()