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
#           per 1 set *list*
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
import converter
import plotly.express as px
import json

parser = argparse.ArgumentParser(description="Folder Path")
pwd = os.getcwd()
parser.add_argument("-s", "--source", type=str, help="Path of source files", default=f"{pwd}/../data/")
parser.add_argument("-d", "--dest", type=str, help="Path to destination", default=f"{pwd}/../json/")
parser.add_argument("-c", "--convert", type=bool, help="Need to convert", default=False)
parsers = parser.parse_args()

sourcePath = parsers.source
destPath = parsers.dest

if (parsers.convert) : converter.convert(sourcePath, destPath)

with open('../json/RW26.json') as f:
    json_obj = json.load(f)

# fig = px.line(x=json_obj['data']['step']['time'], y=json_obj['data']['step']['voltage'])

# fig.show(renderer="png")

print(type(json_obj['data']['step']['date'][16665]))
print(json_obj['data']['step']['relativeTime'][3])
