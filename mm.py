import streamlit as st

def main():
    # 1. 設定網頁標題
    st.title("BMI 健康計算機")
    st.write("請輸入您的身高與體重，我們將為您計算 BMI 指數。")

    # 為了美觀，我們使用兩個欄位 (Columns) 讓輸入框並排
    col1, col2 = st.columns(2)

    with col1:
        # 輸入介面：身高 (cm)
        # min_value 設定為 1.0 避免除以零的錯誤，step=1.0 設定每次增減 1
        height_cm = st.number_input("身高 (cm)", min_value=1.0, value=170.0, step=1.0)

    with col2:
        # 輸入介面：體重 (kg)
        weight_kg = st.number_input("體重 (kg)", min_value=1.0, value=65.0, step=0.5)

    # 加入分隔線
    st.divider()

    # 2. 按鈕邏輯
    if st.button("開始計算", type="primary"):
        # 計算邏輯
        height_m = height_cm / 100  # 將公分轉換為公尺
        bmi = weight_kg / (height_m ** 2)
        
        # 顯示 BMI 數值 (保留兩位小數)
        st.subheader(f"您的 BMI 為：{bmi:.2f}")

        # 3. 判斷與輸出 (含加分題顏色邏輯)
        # 根據衛福部國健署標準：
        # 過輕: < 18.5
        # 正常: 18.5 <= BMI < 24
        # 異常/肥胖: >= 24 (包含過重與肥胖)

        if 18.5 <= bmi < 24:
            result_text = "正常範圍"
            # 使用 Streamlit 的顏色語法 :green[文字]
            color_message = f":green[**結果判定：{result_text}**] (恭喜！請保持)"
            st.markdown(color_message)
            st.balloons() # 加碼一個特效：如果是正常，顯示氣球慶祝
        else:
            if bmi < 18.5:
                result_text = "體重過輕"
            else:
                result_text = "肥胖 / 過重"
            
            # 使用 Streamlit 的顏色語法 :red[文字]
            color_message = f":red[**結果判定：{result_text}**] (請注意健康喔)"
            st.markdown(color_message)

if __name__ == "__main__":
    main()