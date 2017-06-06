import matplotlib.pyplot as plt
import numpy as np

x = [7,8,9,10,11,12]
fig = plt.figure()
ax1 = fig.add_subplot(111)
# ax1.plot(x, [234,249,184,252,200,166], '-', linewidth=2, label = "Hot")
# ax1.plot(x, [81,117,159,94,68,66], '-', linewidth=2, label = "Cold")
# ax1.plot(x, [36,42,64,92,249,200], '-', linewidth=2, label = "Rain")
# ax1.plot(x, [9,17,14,33,26,18], '-', linewidth=2, label = "Snow")
# ax1.plot(x, [27,37,42,53,35,26], '-', linewidth=2, label = "Wind")
# ax1.plot(x, [0.60,0.54,0.40,0.48,0.34,0.35], '-', linewidth=2, label = "Hot")
# ax1.plot(x, [0.21,0.25,0.34,0.18,0.12,0.14], '-', linewidth=2, label = "Cold")
# ax1.plot(x, [0.09,0.09,0.14,0.18,0.43,0.42], '-', linewidth=2, label = "Rain")
# ax1.plot(x, [0.02,0.04,0.03,0.06,0.04,0.04], '-', linewidth=2, label = "Snow")
# ax1.plot(x, [0.07,0.08,0.09,0.10,0.06,0.05], '-', linewidth=2, label = "Wind")
ax1.plot(x, [77,76,70,83,66,62], '-', linewidth=2, label = "max")
ax1.plot(x, [61,60,57,62,61,47], '-', linewidth=2, label = "min")
ax1.plot(x, [0,0,0,0,73,10], '-', linewidth=2, label = "Rain * 10")
ax1.plot(x, [0,0,0,0,0,0.01], '-', linewidth=2, label = "Snow * 10")
ax1.plot(x, [6,4,5,7,4,2], '-', linewidth=2, label = "Wind (MPH)")
ax1.legend(loc='upper center')
plt.title("Austin, TX")
plt.xlabel("Date in March")
plt.ylabel("Temp")

plt.show()

