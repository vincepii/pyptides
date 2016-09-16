import matplotlib.pyplot as plt


class DataPlotter(object):

    def __init__(self):
        super(DataPlotter, self).__init__()
        self._index = {}
        # List of dicts, each dicts is a curve to be plotted with the reference x values
        self._data = {}

    def adddataset(self, name, x_range, data):
        self._index[name] = x_range
        if not self._data.get(name):
            self._data[name] = []
        self._data[name].append(data)

    def plot(self):
        '''
        Plots all the curves of a section on a single graph
        '''
        for name in self._index.keys():
            x_range = self._index[name]
            for points in self._data[name]:
                plt.plot(x_range, [points[k] for k in x_range])
                fig = plt.figure()
                fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')
        # TODO: write title in plot and save it
        # Title will be name
        # Legend with curves (filenames?)
        plt.show()
