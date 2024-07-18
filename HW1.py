import numpy as np
import matplotlib.pyplot as plt
w = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]) 
#正反行程平均校准点
single = np.array([9.35, 15, 17.5, 20.7, 23.825, 27.675, 32.425, 35.8, 38.425, 41.5, 42.225])
half = np.array([0.35, 3.425, 9.95, 17.675, 24.75, 30.025, 39.4, 44.475, 61.55, 73.4, 81.9])
overall = np.array([1.75, 11.625, 25.175, 36.6,	52.025,	63.925,	77.175,	90.35, 103.725, 116.925, 130.25])

w = w/1000
single = single/1000
half = half/1000
overall = overall/1000

single_result = np.polyfit(w,single,1) #线性拟合
half_result = np.polyfit(w,half,1)
overall_result = np.polyfit(w,overall,1)

p1 = np.poly1d(single_result)
single_fit = p1(w) #参考点
plt.figure(1)
plt.title("single arm bridge")
plt.xlabel("weight/kg")
plt.ylabel("voltage/V")
plt.plot(w,single,'*')
plt.plot(w,single_fit)
plt.savefig("single_arm_bridge.png")
print("单臂灵敏度:" + str(single_result))

p2 = np.poly1d(half_result)
half_fit = p2(w) #参考点
plt.figure(2)
plt.title("half bridge")
plt.xlabel("weight/kg")
plt.ylabel("voltage/V")
plt.plot(w,half,'*')
plt.plot(w,half_fit)
plt.savefig("half_bridge.png")
print("半桥灵敏度:" + str(half_result))

p3 = np.poly1d(overall_result)
overall_fit = p3(w) #参考点
plt.figure(3)
plt.title("full bridge")
plt.xlabel("weight/kg")
plt.ylabel("voltage/V")
plt.plot(w,overall,'*')
plt.plot(w,overall_fit)
plt.savefig("full_bridgee.png")
print("全桥灵敏度:" + str(overall_result))
plt.show()

y1_errormax = np.max(np.abs(single_fit - single)) #最大误差
y2_errormax = np.max(np.abs(half_fit - half))
y3_errormax = np.max(np.abs(overall_fit - overall))
print(y1_errormax,y2_errormax,y3_errormax)

y1_full = single_fit[-1] - single_fit[0] #满量程
y2_full = half_fit[-1] - half_fit[0]
y3_full = overall_fit[-1] - overall_fit[0]
print(y1_full,y2_full,y3_full)

y1 = y1_errormax/y2_full*100 #非线性误差
y2 = y2_errormax/y2_full*100
y3 = y3_errormax/y3_full*100
print(y1,y2,y3)