from __future__ import division
import numexpr as ne
import re


class CfgParser(object):

    def __init__(self):
        super(CfgParser, self).__init__()
        self._section_re_str = '^\[(.*);(.*)\]'
        self._section_re = re.compile(self._section_re_str)
        self._line_re_str = '^(.*);(.*);(.*);(.*)'
        self._line_re = re.compile(self._line_re_str)
        # Dict of list of dicts, each outer dict is a scenario of values that will be plotted together, e.g.:
        # {"test1": [{"filename": "x", "concentration": y, "chromophores": w, "mw": z},
        #           {"filename": "x", "concentration": y, "chromophores": w, "mw": z}]
        #  "test2": [...] }
        self._sections = {}
        # Dictionary mapping the test name with the x range for the plots
        # E.g., {"test1": [180, 181, ... 280],
        #        "test2": [...] }
        self._xranges = {}

    def parse(self, filename):
        with open(filename) as f:
            current_key = None
            for line in f:
                if len(line) == 0 or line == '\n' or line.startswith('#'):
                    continue
                r = self._section_re.match(line)
                if r:
                    # Start of a new section
                    current_key = r.group(1).strip()
                    self._sections[current_key] = []
                    lrange = r.group(2).strip()
                    startrange, endrange = map(lambda x: int(x), lrange.split('-'))
                    lrange = [x for x in range(startrange, endrange + 1)]
                    self._xranges[current_key] = lrange
                    continue
                r = self._line_re.match(line)
                if not r:
                    # It's either a section or a configuration line!
                    raise Exception("Unexpected line in configuration file: {}".format(line))
                csvname, concentration, chromophores, mol_weight = [r.group(k).strip() for k in range(1,5)]
                d = {"filename": csvname, "concentration": ne.evaluate(concentration), "chromophores": ne.evaluate(chromophores), "mw": ne.evaluate(mol_weight)}
                self._sections[current_key].append(d)

    def getconfig(self):
        return self._sections

    def get_x_range(self, section_key):
        return self._xranges[section_key]