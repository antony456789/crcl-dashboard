# 📌 modules/volatility.py
# 功能：顯示 CRCL 假數據的波動率 IV 曲線，將來可串接真實資料

import streamlit as st
import matplotlib.pyplot as plt

def display_iv_curve():
    """
    顯示一個模擬的 Strike vs IV 曲線，模擬展示用，日後可串接 yfinance、OptionStrat 等 API。
    """
    st.markdown("📌 本模組展示 CRCL 熱門 Strike 的隱含波動率（IV）曲線")
    
    # 假資料（可日後改為 yfinance 輸出）
    strikes = [200, 220, 240, 260, 280]
    iv_values = [130, 160, 180, 250, 310]  # 單位：%
    
    # 繪圖
    fig, ax = plt.subplots()
    ax.plot(strikes, iv_values, marker='o', linestyle='-', color='blue')
    ax.set_title("CRCL Implied Volatility Curve (Mock Data)")
    ax.set_xlabel("Strike Price")
    ax.set_ylabel("Implied Volatility (%)")
    ax.grid(True)

    st.pyplot(fig)
