import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import requests
import time
from threading import Thread


def send_heartbeat():
    while True:
        try:
            # 根据实际部署地址和端口替换 URL，appid 请换成你的应用 ID
            requests.post("http://127.0.0.1:5000/api/apps/your_appid/heartbeat")
        except Exception as e:
            print("Heartbeat error:", e)
        time.sleep(60)  # 每60秒发送一次心跳

# 启动后台线程（daemon 模式）
Thread(target=send_heartbeat, daemon=True).start()

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
