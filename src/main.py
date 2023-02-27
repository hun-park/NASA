import argparse, os
import tools

parser = argparse.ArgumentParser(description="Folder Path")
pwd = os.getcwd()

parser.add_argument("-s", "--source", type=str, help="Path of source files", default=f"{pwd}/../data/")
parser.add_argument("-d", "--dest", type=str, help="Path to destination", default=f"{pwd}/../json/RW26.json")
parser.add_argument("-c", "--convert", type=bool, help="Need to convert", default=False)
parsers = parser.parse_args()

if (parsers.convert) : tools.converter(parsers.source, parsers.dest)
dataDict = tools.loader(parsers.dest, isFile=True)
dataList = {'time': tools.merger(dataDict['RW26.json']['data']['step']['time']),
            'voltage': tools.merger(dataDict['RW26.json']['data']['step']['voltage']),
            'current': tools.merger(dataDict['RW26.json']['data']['step']['current']),
            'temparature': tools.merger(dataDict['RW26.json']['data']['step']['temperature'])
            }

tools.plotter(dataList, 'time', 'voltage')