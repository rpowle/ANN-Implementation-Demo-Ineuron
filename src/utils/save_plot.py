import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import ListedColormap
import joblib # for saving method
plt.style.use("fivethirtyeight")# this is style of graphs
import os
import logging


def save_plot(df, file_name, model):
  def _create_base_plot(df):
      df.plot(kind="scatter", x="x1", y="x2", c="y", s=100, cmap="winter")
      figure = plt.gcf() # get current figure
      figure.set_size_inches(10, 8)