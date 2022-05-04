import numpy as np
import matplotlib.pyplot as plt

with open ("settings.txt", "r") as settings:
    freq = [float(i) for i in settings.read().split("\n")]
data = np.loadtxt ("7-1_data.txt", dtype = float)
data = data * (3.3/256)
period = 1/freq[0]
time = [period * i for i in np.arange(data.size)]

#for p in np.arange(data.size):
#   print (time[p], data[p])

fig, ax = plt.subplots (figsize = (16, 9))
ax.plot (time, data, linestyle = '-', color = 'red', linewidth = 1)
ax.plot (time[1::150], data[1::150], label = 'U(t)', linestyle = '-', marker = 'o', markersize = 7, color = 'red', markerfacecolor = 'red')

ax.set (xlabel = 't, с', ylabel = 'U, В', title = 'Зависимость U(t) при зарядке и разрядке конденсатора')
ax.legend(loc = 'upper right', fontsize = 20)

ax.minorticks_on()
ax.grid (which = 'major', color = 'black', linewidth = 1)
ax.grid (which = 'minor', color = 'black', linestyle = ':')

plt.ylim(0, max (data) * 1.05) 
plt.xlim(0, max (time) * 1.05)

plt.text (60, 2, "Время заряда: " + str(time[np.argmax(data)]) + " с\n"
 + "Время разряда: " + str(time[np.argmax(time)] - time[np.argmax(data)]) + " с", 
fontsize = 15, bbox = dict (boxstyle =  "square", ec = (1., 0.5, 0.5), 
fc = (1., 0.7, 0.7)))

fig.savefig ("graph.svg")
plt.show

