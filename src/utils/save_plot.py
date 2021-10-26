import matplotlib.pyplot as plt
#plt.style.use("fivethirtyeight")# this is style of graphs
#import logging
import os
import pandas as pd





def saved_plot(df, plot_name, plot_dir):
    df.plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 1)


    unique_file = plot_name
    os.makedirs(plot_dir, exist_ok=True)
    plot_path = os.path.join(plot_dir, plot_name)
    plt.savefig(plot_path)
    plt.show

