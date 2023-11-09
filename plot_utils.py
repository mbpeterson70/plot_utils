import matplotlib.pyplot as plt
import numpy as np

def square_equal_aspect(ax):
    """
    Sets a plot's aspect ratio equal and makes the plot square while still being centered at the
    original plot's center.

    Args:
        ax (matplotlib axis): matplotlib axis
    """
    # set equal aspect ratio
    ax.set_aspect('equal')

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    xrange = xlim[1] - xlim[0]
    yrange = ylim[1] - ylim[0]

    if xrange > yrange:
        ycenter = ylim[0] + .5*yrange
        ax.set_ylim([ycenter - .5*xrange, ycenter + .5*xrange])
    else:
        xcenter = xlim[0] + .5*xrange
        ax.set_xlim([xcenter - .5*yrange, xcenter + .5*yrange])
    return
    
def legend(ax, kwargs_list, labels_list):
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    out_of_bounds = [xlim[1]+(xlim[1]-xlim[0]), ylim[1]+(ylim[1]-ylim[0])]
    for kwargs, label in zip(kwargs_list, labels_list):
        ax.plot(*out_of_bounds, **kwargs, label=label)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.legend()
    
def setup_kwargs(
    marker=None,
    markersize=None,
    color=None,
    linestyle=None,
    mew=None,
):
    kwargs = {}
    if marker is not None:
        kwargs['marker'] = marker
    if markersize is not None:
        kwargs['markersize'] = markersize
    if color is not None:
        kwargs['color'] = color
    if linestyle is not None:
        kwargs['linestyle'] = linestyle
    if mew is not None:
        kwargs['mew'] = mew
    return kwargs

def remove_ticks(ax, x=True, y=True):
    if x:
        # xticks = ax.get_xticks()
        # ax.set_xticks(xticks, minor=False)
        ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    if y:
        # yticks = ax.get_yticks()
        # ax.set_yticks(yticks, minor=False)
        ax.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

    
def plot_T2d(T, axis_len=None, color=None, **kwargs):
    ax = plt.gca()
    if axis_len is None:
        axis_len = max(ax.get_xlim()[1] - ax.get_xlim()[0], ax.get_ylim()[1] - ax.get_ylim()[0]) / 20
    
    frame_orig = T[:2,-1]
    frame_xaxis = frame_orig + axis_len * T[:2,0] / np.linalg.norm(T[:2,0])
    frame_yaxis = frame_orig + axis_len * T[:2,1] / np.linalg.norm(T[:2,0])

    plt.plot([frame_orig[0], frame_xaxis[0]], [frame_orig[1], frame_xaxis[1]],
             color=color if color is not None else 'red', **kwargs)
    plt.plot([frame_orig[0], frame_yaxis[0]], [frame_orig[1], frame_yaxis[1]], 
             color=color if color is not None else 'green', **kwargs)

def plot_pose2d(T, axis_len=None, color=None, **kwargs):
    plot_T2d(T, axis_len, color, **kwargs)