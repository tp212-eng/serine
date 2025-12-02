import streamlit as st
import time
from datetime import datetime

st.title("我的雲端時鐘 ⏰")

# 1. 創建一個空的容器 (Placeholder)
# 這就像是在黑板上留一塊空白，等一下要一直擦掉重寫
clock_spot = st.empty()

# 2. 開始無窮迴圈更新時間
# 注意：在網頁上跑無窮迴圈通常不建議，但做時鐘這是最簡單的方法
while True:
    # 獲取現在時間
    now_time = datetime.now().strftime("%H:%M:%S")
    
    # 更新容器的內容
    # 這裡我們用 Markdown 語法讓字變大
    clock_spot.markdown(
        f"<h1 style='text-align: center; color: cyan;'>{now_time}</h1>", 
        unsafe_allow_html=True
    )
    
    # 休息一秒鐘再繼續
    time.sleep(1)