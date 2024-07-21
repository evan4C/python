import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("time_series_covid19_confirmed_US.csv", index_col=0)
data = df.stack().unstack(0)


def nice_axes(axis):
    axis.set_facecolor('.8')
    axis.tick_params(labelsize=8, length=0)
    axis.grid(True, axis='x', color='white')
    axis.set_axisbelow(True)
    [spine.set_visible(False) for spine in axis.spines.values()]


s = data.loc['9/11/20']
fig, ax = plt.subplots(figsize=(4, 2.5), dpi=144)
colors = plt.cm.Dark2(range(len(s.index)))
y = []
for i in range(len(s.index)):
    t = s.index[i][:-12]
    y.append(t)

width = s.values
ax.barh(y=y, width=width, color=colors)

fig, ax_array = plt.subplots(nrows=1, ncols=3, figsize=(7, 2.5), dpi=144, tight_layout=True)
dates = ['9/11/20', '8/11/20', '7/11/20']
for ax, date in zip(ax_array, dates):
    s = data.loc[date].sort_values()
    print(s.index)
    ax.barh(y=s.index, width=s.values, color=colors)
    ax.set_title(date, fontsize='smaller')
    nice_axes(ax)

nice_axes(ax)
plt.show()
