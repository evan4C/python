import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def prepare_data(df, steps=5):
    df = df.reset_index()
    df.index = df.index * steps
    last_idx = df.index[-1] + 1
    df_expanded = df.reindex(range(last_idx))
    df_expanded['date'] = df_expanded['date'].fillna(method='ffill')
    df_expanded = df_expanded.set_index('date')
    df_rank_expanded = df_expanded.rank(axis=1, method='first')
    df_expanded = df_expanded.interpolate()
    df_rank_expanded = df_rank_expanded.interpolate()
    return df_expanded, df_rank_expanded


def nice_axes(axis):
    axis.set_facecolor('.8')
    axis.tick_params(labelsize=8, length=0)
    axis.grid(True, axis='x', color='white')
    axis.set_axisbelow(True)
    [spine.set_visible(False) for spine in axis.spines.values()]


def init():
    ax.clear()
    nice_axes(ax)
    ax.set_ylim(.2, 6.8)


def update(i):
    for bar in ax.containers:
        bar.remove()
    y = df_rank_expanded.iloc[i]
    width = df_expanded.iloc[i]
    ax.barh(y=y, width=width, color=colors, tick_label=labels)
    date_str = df_expanded.index[i].strftime('%B %-d, %Y')
    ax.set_title(f'COVID-19 Deaths by Country - {date_str}', fontsize='smaller')


data_expanded, data_rank_expanded = prepare_data(data)
fig = plt.Figure(figsize=(4, 2.5), dpi=144)
ax = fig.add_subplot()
anim = FuncAnimation(fig=fig, func=update, init_func=init, frames=len(data_expanded),
                     interval=100, repeat=False)

