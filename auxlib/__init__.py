from .common import *

from .data_gen import *
from .folder_admin import folders, folders_figs, name_of_folder
from .loader_and_saver import *

print("Importing library...")

#__all__ = ['DenseNeuralNetworkGen', 'loader_and_saver']

def latticeGraph(squareLattice: list, size=40):
    """
    Generates a graph of square lattices using the given list of square lattices.

    Parameters:
        squareLattice (list): A list of square lattices to be plotted.
        size (int, optional): The size of the square lattices. Defaults to 40.

    Returns:
        None
    """
    cmap1 = ListedColormap(['white', 'gray', 'black'])
    
    numPlots = len(squareLattice)
    rows = int(np.ceil(numPlots / 3))
    cols = min(3, numPlots)  # Ensure cols is at most 3

    fig = plt.figure(figsize=(3*cols, 3*rows))
    gs = gridspec.GridSpec(rows, cols + 1, width_ratios=[1]*cols + [0.05])

    ax = [fig.add_subplot(gs[i, j]) for i in range(rows) for j in range(cols)]
    
    for i, axi in enumerate(ax):
        if i < numPlots:
            im1 = axi.imshow(squareLattice[i], cmap=cmap1,
                            interpolation='nearest', vmin=-1, vmax=1)
            axi.set_xticks(np.arange(-0.5, size, 5))
            axi.set_yticks(np.arange(-0.5, size, 5))
            axi.set_xticklabels([])
            axi.set_yticklabels([])
        else:
            fig.delaxes(axi)  # Remove empty subplots

    # Add colorbar to the right of the entire figure
    cbar_ax = fig.add_subplot(gs[:, -1])
    fig.colorbar(im1, cax=cbar_ax, ticks=[-1, 0, 1])

    # Display the plot
    plt.tight_layout()
    plt.show()
    return


# CALLBACK
class myCallback(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):

        if(logs.get('val_accuracy') > 0.999):
            print("\nAccuracy is high enough, so cancelling training!")
            self.model.stop_training = True


print("Library successfully imported")