import matplotlib.pyplot as plt
import numpy as np

# 创建极坐标图
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

# 生成角度和半径数据
theta = np.linspace(0, 2*np.pi, 100)
r = np.random.rand(100)

# 绘制极坐标图
ax.plot(theta, r)

# 添加标题
ax.set_title('Polar Plot')

# 显示图形
plt.show()
