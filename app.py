# 📌 app.py
# 功能：主入口頁面，呼叫子模組顯示功能項目（目前為 IV 波動率曲線展示）

import streamlit as st
from modules import volatility

# 設定頁面標題與佈局
st.set_page_config(page_title="CRCL Options Dashboard", layout="wide")

# 儀表板標題
st.title("📈 CRCL Options IV & Sentiment Dashboard")

# 顯示波動率模組
st.header("📊 Implied Volatility Monitor")
volatility.display_iv_curve()
