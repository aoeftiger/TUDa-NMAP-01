#!/usr/bin/env python
import warnings
warnings.filterwarnings('ignore')

import numpy as np
np.random.seed(0)

import matplotlib
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm

import seaborn as sns
sns.set_context('talk', font_scale=1.2, rc={'lines.linewidth': 3})
sns.set_style('ticks',
              {'grid.linestyle': 'none', 'axes.edgecolor': '0',
               'axes.linewidth': 1.2, 'legend.frameon': True,
               'xtick.direction': 'out', 'ytick.direction': 'out',
               'xtick.top': True, 'ytick.right': True,
              })

def set_axes(xlim=(-np.pi * 1.1, np.pi * 1.1), ylim=(-3, 3)):
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(r'$\theta$')
    plt.ylabel(r'$p$')
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r"$-\pi$", r"$-\pi/2$", "0", r"$\pi/2$", r"$\pi$"])