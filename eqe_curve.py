import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取以 tab 分隔的 txt 文件
file_11p2 = 'source\EQE\OSOL-45678_11p2_ 1_yyoon_300-900nm_0,0000V_2024-06-11 14-20-17.sr.fmf'  # 替换为你的文件路径
data_11p2 = pd.read_csv(file_11p2, sep='\t')

file_12p1 = 'source\EQE\OSOL-45678_12p1_ 2_yyoon_300-900nm_0,0000V_2024-06-11 14-23-28.sr.fmf'  # 替换为你的文件路径
data_12p1 = pd.read_csv(file_12p1, sep='\t')

file_12p3 = 'source\EQE\OSOL-45678_12p3_ 3_yyoon_300-900nm_0,0000V_2024-06-11 14-26-39.sr.fmf'  # 替换为你的文件路径
data_12p3 = pd.read_csv(file_12p3, sep='\t')

wavelength_11p2 = data_11p2.iloc[:, 0]
eqe_11p2 = data_11p2.iloc[:, 6]

wavelength_12p1 = data_12p1.iloc[:, 0]
eqe_12p1 = data_12p1.iloc[:, 6]

wavelength_12p3 = data_12p3.iloc[:, 0]
eqe_12p3 = data_12p3.iloc[:, 6]


# # 绘制图形
plt.figure(figsize=(10, 6))
# plt.plot(wavelength_11p2, eqe_11p2, color='b', label='11p2')
# # #         #  , marker='o', linestyle='-', color='b')
plt.plot(wavelength_12p1, eqe_12p1, color='r', label='12p1')
plt.plot(wavelength_12p3, eqe_12p3, color='g', label='12p3')


plt.xlabel('Wavelength [nm]')  # 可根据具体列名修改
plt.ylabel('EQE [%]')  # 可根据具体列名修改
plt.title('EQE Curve')  # 可根据具体文件名修改

plt.legend()
plt.grid(True)
plt.show()