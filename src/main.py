# Structure *type*
#
# data *dict*
#   step *dict* (ex RW26)
#       comment *list* (#s 16,666)
#           comment *str*
#       type *list* (#s 16,666)
#           type *str*
#       time *list* (#s 16,666)
#           per 1 set *list*
#       relativeTime *list* (#s 16,666) //starts with 0
#           per 1 set *list*            //not monotonic
#       voltage *list* (#s 16,666)
#           per 1 set *list*
#       current *list* (#s 16,666)
#           per 1 set *list*
#       temperature *list* (#s 16,666)
#           per 1 set *list*
#       date *list* (#s 16,666)
#           date *str*
#   procedure *str*
#   description *str*

import argparse, os
import tools

parser = argparse.ArgumentParser(description="Folder Path")
pwd = os.getcwd()

parser.add_argument("-s", "--source", type=str, help="Path of source files", default=f"{pwd}/../data/")
parser.add_argument("-d", "--dest", type=str, help="Path to destination", default=f"{pwd}/../json/RW26.json")
parser.add_argument("-c", "--convert", type=bool, help="Need to convert", default=False)
parsers = parser.parse_args()

sourcePath = parsers.source
destPath = parsers.dest
isConvert = parsers.convert

if (isConvert) : tools.converter(sourcePath, destPath)
dataDict = tools.loader(destPath, isFile=True)
dataList = {'time': tools.merger(dataDict['RW26.json']['data']['step']['time']),
            'voltage': tools.merger(dataDict['RW26.json']['data']['step']['voltage']),
            'current': tools.merger(dataDict['RW26.json']['data']['step']['current']),
            'temparature': tools.merger(dataDict['RW26.json']['data']['step']['temperature'])
            }

tools.plotter(dataList, 'time', 'voltage', isSave=True, format='eps')

# import chart_studio
# username = 'hun.park'
# api_key = 'NT3hSxNOA6fe3fztPoLk'
# chart_studio.tools.set_credentials_file(username=username,api_key=api_key)
# chart_studio.plotly.plot())