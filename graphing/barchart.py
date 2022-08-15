#!/usr/bin/env python3
"""Provides the monthly average temperature around the year in Sierra Vista"""

import matplotlib.pyplot as plt
import numpy as np

labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
average_high = [61, 64, 70, 77, 85, 93, 92, 89, 87, 79, 69, 62]
average_low = [34, 37, 42, 47, 55, 63, 66, 65, 60, 51, 41, 34]

#Label Locations
x = np.arange(len(labels))
#Width of the bar
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, average_high, width, label='High')
rects2 = ax.bar(x + width/2, average_low, width, label='Low')

#Add some text for labels, title and custom x-axis tick labels, etc
ax.set_ylabel('Temperature')
ax.set_title('Monthly average high and low temperature in Sierra Vista')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.savefig("/home/student/static/SV_averageTemp.png")
