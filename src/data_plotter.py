import matplotlib.pyplot as plt
import os


class DataPlotter(object):

    def __init__(self):
        super(DataPlotter, self).__init__()
        # Maps each section name to its xrange
        self._index = {}
        # Dict of dicts, each dicts is a curve to be plotted with the reference x values
        # {'section_name': {'filename': {points},
        #                   'filename': {points}}
        # }
        self._data = {}

    def adddataset(self, name, x_range, data, filename):
        self._index[name] = x_range
        if not self._data.get(name):
            self._data[name] = {}
        self._data[name][filename] = data

    def plot(self):
        '''
        Plots all the curves of a section on a single graph
        '''
        for name in self._index.keys():
            x_range = self._index[name]
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.set_title(name)
            ax.set_ylabel('Wavelength,CircularDichroism')
            for filenaname, points in self._data[name].items():
                curve_name = os.path.split(filenaname)[-1]
                ax.plot(x_range, [points[k] for k in x_range], label=curve_name)
        plt.legend()
        plt.show()
