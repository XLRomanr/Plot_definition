import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import requests
import time
from threading import Thread

def update_access_time():
    """ 访问 Streamlit 页面时调用后端 API 记录最后访问时间 """
    appid = "Plot_definition"  # 你的 Streamlit 应用 ID
    flask_server_url = "http://11.2.171.248:5000"  # 你的 Flask 服务器地址
    url = f"{flask_server_url}/api/apps/{appid}/update_access_time"

    try:
        response = requests.post(url)
        if response.status_code == 200:
            st.success("访问时间已更新")
        else:
            st.warning("无法更新访问时间")
    except Exception as e:
        st.error(f"更新访问时间失败: {e}")

# **只在用户首次进入页面（当前会话）时调用**
if "access_logged" not in st.session_state:
    update_access_time()
    st.session_state.access_logged = True  # 标记当前会话已记录访问时间
    
# 设置标题
st.title("三次函数可视化工具")

# 输入系数
a = st.number_input("请输入三次项系数 (a):", value=1.0)
b = st.number_input("请输入二次项系数 (b):", value=0.0)
c = st.number_input("请输入一次项系数 (c):", value=0.0)
d = st.number_input("请输入常数项 (d):", value=0.0)

# 生成 x 和 y 数据
x = np.linspace(-10, 10, 500)
y = a * x**3 + b * x**2 + c * x + d

# 绘制函数图像
fig, ax = plt.subplots()
ax.plot(x, y, label=f"y = {a}x³ + {b}x² + {c}x + {d}")
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')  # x轴
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')  # y轴
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)

# 在Streamlit界面显示图像
st.pyplot(fig)
