import matplotlib.pyplot as plt
from random_walk import RandmWalk

while True:
    rw = RandmWalk()
    rw.fill_walk()

    # 创建列表，用于颜色映射
    point_list = list(range(rw.num_points))

    # pyplot显式用法
    # The "Axes" interface is how Matplotlib is implemented, 
    # and many customizations and fine-tuning end up being done at this level.
    fig = plt.figure(figsize=(6,4))
    randm_fig = fig.subplots() #返回一个Axes实例

    # 绘制图像
    randm_fig.scatter(rw.x_values, rw.y_values, c=point_list, cmap=plt.cm.Blues, 
                edgecolors="none",s=15)
    # 突出起点和终点
    randm_fig.scatter(0, 0, c='green', edgecolors='none', s=100)
    randm_fig.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=100)
    

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break

    """
    此外可以修改点数：rw = RandmWalk(50000)
    """