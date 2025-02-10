import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import requests
import time
from threading import Thread

def update_access_time():
    appid = "Plot_definition"  # 你应该替换成该 Streamlit 应用的 ID
    flask_server_url = "http://11.2.171.248:5000"  # 改成你的 Flask 服务器 IP
    url = f"{flask_server_url}/api/apps/{appid}/update_access_time"
    
    try:
        response = requests.post(url)
        if response.status_code == 200:
            st.success("访问时间已更新")
        else:
            st.warning("无法更新访问时间")
    except Exception as e:
        print(f"Failed to update access time: {e}")

# 后台线程定时调用更新访问时间
def run_periodic_update():
    while True:
        update_access_time()
        time.sleep(600)  # 每 10 分钟更新一次访问时间

# 启动后台线程（守护线程）
Thread(target=run_periodic_update, daemon=True).start()


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
