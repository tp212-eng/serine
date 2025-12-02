import tkinter as tk
from time import strftime

def update_time():
    # 獲取當前時間，格式為 時:分:秒 (24小時制)
    # 如果想要 12 小時制並顯示 AM/PM，請將格式改為 '%I:%M:%S %p'
    string_time = strftime('%H:%M:%S')
    
    # 更新標籤的文字內容
    clock_label.config(text=string_time)
    
    # 設定每 1000 毫秒 (即 1 秒) 重新執行一次 update_time 函式
    clock_label.after(1000, update_time)

# 建立主視窗
root = tk.Tk()
root.title("數位時鐘")
root.resizable(False, False) # 禁止調整視窗大小 (可選)

# 設定視窗背景顏色 (為了讓邊緣也是黑色的)
root.configure(bg='black')

# 設定標籤 (Label) 的樣式
# font: 字體設定 ('字型', 大小, '粗體')
# bg: 背景顏色 (black)
# fg: 文字顏色 (blue / #ff0000 為亮綠色)
clock_label = tk.Label(root, 
                       font=('calibri', 250, 'bold'),
                       background='black',
                       foreground="#FF7B00")

# 將標籤放置在視窗中央
clock_label.pack(anchor='center', padx=20, pady=20)

# 啟動時鐘更新功能
update_time()

# 進入視窗主迴圈
root.mainloop()