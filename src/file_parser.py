import re

class FileParser(object):

    def __init__(self):
        super(FileParser, self).__init__()
        self._dataline_re_str = '^([0-9]+),([-]?[0-9]+[.]?[0-9]+)'
        self._dataline_re = re.compile(self._dataline_re_str)
        self._datapoints = {}
        self._index = []

    def parsefile(self, filename):
        with open(filename) as f:
            for line in f:
                if line.startswith("Wavelength,") and next(f).startswith("CircularDichroism"):
                    # This is the data that we want
                    while True:
                        line = next(f)
                        r = self._dataline_re.match(line)
                        if r:
                            self._datapoints[int(r.group(1))] = float(r.group(2))
                            self._index.append(int(r.group(1)))
                        else:
                            break

    def get_points(self):
        return self._datapoints

    def get_index(self):
        return self._index
