from __future__ import division

class DataAnalyzer(object):

    def __init__(self, datapoints, concentration, chromophores, mw):
        super(DataAnalyzer, self).__init__()
        self._datapoints = datapoints
        self._concentration = concentration
        self._chromophores = chromophores
        self._mw = mw
        # Out variables
        self._normalized_molar_ellipticity = {}

    def process(self):
        for index, value in self._datapoints.items():
            self._normalized_molar_ellipticity[index] = (value * self._mw) / (10 * 0.1 * self._concentration * self._chromophores)

    def get_normalized_molar_ellipticity(self):
        return self._normalized_molar_ellipticity

