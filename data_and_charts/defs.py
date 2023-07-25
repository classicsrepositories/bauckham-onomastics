from matplotlib.pyplot import plot,figure,subplots,legend,xlabel,ylabel,xlim,ylim,text,title,xticks,yticks
from matplotlib.pyplot import gca,gcf,fill_between

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from numpy.random import rand,randn
from numpy import array,zeros,ones

from scipy import stats

import os
from tqdm.notebook import tqdm

from matplotlib import rcParams,cm
from cycler import cycler

colors = ['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd',
         '#8c564b','#e377c2','#7f7f7f','#bcbd22','#17becf',
         (0.8941176470588236, 0.10196078431372549, 0.10980392156862745),
         (0.21568627450980393, 0.49411764705882355, 0.7215686274509804),
         (0.30196078431372547, 0.6862745098039216, 0.2901960784313726),
         (0.596078431372549, 0.3058823529411765, 0.6392156862745098),
         (1.0, 0.4980392156862745, 0.0),
         (1.0, 1.0, 0.2),
         (0.6509803921568628, 0.33725490196078434, 0.1568627450980392),
         (0.9686274509803922, 0.5058823529411764, 0.7490196078431373),
         (0.6, 0.6, 0.6)]

rcParams.update({
          'axes.axisbelow':True,
          'axes.grid': True,
          'axes.labelsize': 20.0,
          'axes.prop_cycle': cycler(color=colors), 
          'axes.titlesize': 24.0,
          'figure.figsize': [10.0, 8.0],
          'font.family': ['sans-serif'],
          'font.size': 20.0,
          'grid.color': '0.75',
          'grid.linestyle': '-',
          'legend.fontsize': 20.0,
          'legend.frameon': False,
          'legend.numpoints': 1,
          'legend.scatterpoints': 1,
          'lines.linewidth': 3.0,
          'lines.markersize': 5.0,
          'lines.solid_capstyle':'round',
          'text.color': '.15',
          'xtick.color': '.15',
          'xtick.direction': 'out',
          'xtick.labelsize': 20.0,
          'ytick.color': '.15',
          'ytick.direction': 'out',
          'ytick.labelsize': 20.0,})


