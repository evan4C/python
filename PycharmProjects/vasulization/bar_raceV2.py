# reference: https://medium.com/dunder-data/create-a-bar-chart-race-animation-in-python-with-matplotlib-477ed1590096
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("time_series_covid19_confirmed_US.csv", index_col=0)
# exchange the position of row and column
data = df.stack().unstack(0)

# shorten the state name
data.columns = [cname[:-13] for cname in data.columns]


def nice_axes(axis):
    axis.set_facecolor('.8')
    axis.tick_params(labelsize=8, length=0)
    axis.grid(True, axis='x', color='white')
    axis.set_axisbelow(True)
    [spine.set_visible(False) for spine in axis.spines.values()]


tail_data = data.tail()
# It’s easier to insert an exact number of new rows when using the default index
tail_data = tail_data.reset_index()
# print(tail_data)

# insert 5 new rows between the first and second rows and between the second and third rows.
tail_data.index = tail_data.index * 5

# Expand DataFrame with reindex
# pandas inserts new rows of all missing values for every index not in the current DataFrame.
last_idx = tail_data.index[-1] + 1
tail_data_expanded = tail_data.reindex(range(last_idx))
# print(tail_data_expanded)

# fill new rows in using the last known value with the fillna method and set it as the index again.
# method='ffill': propagate non-null values forward
tail_data_expanded['index'] = tail_data_expanded['index'].fillna(method='ffill')
tail_data_expanded = tail_data_expanded.set_index('index')
# print(tail_data_expanded)

# Rank each row
# Set axis to 1 to change the direction of the operation so that values in each row are ranked against each other.
rank_data = tail_data_expanded.rank(axis=1, method='first')
# print(rank_data)

# Linear interpolate missing values
# The interpolate method can fill in the missing values in a variety of ways. By default, it uses linear interpolation and works column-wise.
tail_data_expanded = tail_data_expanded.interpolate()
rank_data = rank_data.interpolate()

# Plot each step of the transition
# The interpolated ranks will serve as the new position of the bars along the y-axis.
fig, ax_array = plt.subplots(nrows=1, ncols=6, figsize=(12, 2),
                             dpi=144, tight_layout=True)

labels = tail_data.columns
for i, ax in enumerate(ax_array.flatten()):
    y = rank_data.iloc[i].index
    print(y)
    width = tail_data_expanded.iloc[i]
    print(width)
    ax.barh(y=y, width=width)
    nice_axes(ax)

plt.show()