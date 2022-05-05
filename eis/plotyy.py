import numpy as np
import matplotlib.pyplot as plt

# this is also called a 'parity' plot
def plotyy(y, y_pred, color=None, title=None):
    # Customize colors to match with capacity vs cycle plot earlier
    if color is not None:
        n_series = np.unique(color).size
    else:
        n_series = 1
    cmap = plt.get_cmap('tab10', n_series)
    # Get axes and plot
    fig, ax = plt.subplots(1,1)
    sc = ax.scatter(y.values, y_pred, c=color, cmap=cmap)
    ax.set_aspect('equal')
    plt.xlabel('Actual discharge capacity (mAh)')
    plt.ylabel('Predicted discharge capacity (mAh)')
    plt.axis('square')
    # Diagonal line for guiding the eye
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    lims = np.concatenate((xlim, ylim))
    lims = np.array([min(lims), max(lims)])
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    ax.set_autoscale_on(False)
    plt.plot([-100, 100], [-100,100], '--k')
    if n_series > 1:
        # colorbar
        cbar = plt.colorbar(sc)
        tick_locs = (np.arange(n_series) + 1.5)*(n_series-1)/n_series
        cbar.set_ticks(tick_locs)
        cbar.set_ticklabels(np.arange(n_series)+1)
    # title
    if title is not None:
        plt.title(title)
    plt.tight_layout()