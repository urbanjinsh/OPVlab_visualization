import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取以 tab 分隔的 txt 文件
file_path = 'group4_IV measurement5-009_SAMPLE position=S12P2.txt'  # 替换为你的文件路径
data = pd.read_csv(file_path, sep='\t')

data_dark = data[data.iloc[:, 12] == 1]
data_light = data[data.iloc[:, 12] == 2]
# 打印读取的数据
# print(data_group1)
voltage_light = data_light.iloc[1:, 13]
current_light = data_light.iloc[1:, 14]
voltage_light = voltage_light.astype(float)
current_light = current_light.astype(float)

voltage_dark = data_dark.iloc[1:, 13]
current_dark = data_dark.iloc[1:, 14]
voltage_dark = voltage_dark.astype(float)
current_dark = current_dark.astype(float)


# 打印选取的列
# print(current)

# # 绘制图形
plt.figure(figsize=(10, 6))
plt.plot(voltage_light, current_light, color='b', label='Under light')
plt.plot(voltage_dark, current_dark, color='r', label='Under dark')

plt.xlabel('Voltage [V]')  # 可根据具体列名修改
plt.ylabel('Current [mA]')  # 可根据具体列名修改
plt.title('IV Curve')  # 可根据具体文件名修改


plt.legend()
plt.grid(True)
plt.show()