import argparse
from file_parser import FileParser
from data_analyzer import DataAnalyzer
from data_plotter import DataPlotter
from cfg_parser import CfgParser

def main():
    parser = argparse.ArgumentParser(description='Plot data from unknown tool')
    parser.add_argument('filename', type=str, help='name of the configuration file')
    args = parser.parse_args()

    cfg = CfgParser()
    cfg.parse(args.filename)
    config = cfg.getconfig()

    for section, analysis_list in config.items():
        dp = DataPlotter()
        for analysis in analysis_list:
            fp = FileParser()
            fp.parsefile(analysis['filename'])
            da = DataAnalyzer(fp.get_points(), analysis['concentration'], analysis['chromophores'], analysis['mw'])
            da.process()
            dp.adddataset(section, cfg.get_x_range(section), da.get_normalized_molar_ellipticity())
        dp.plot()

if __name__ == "__main__":
    main()
