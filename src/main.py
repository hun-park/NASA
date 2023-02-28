import argparse, os, tools

parser = argparse.ArgumentParser(description="Folder Path")
parser.add_argument("-s", "--source", type=str, help="Path of source files", default="/mnt/hp/NASA/data/")
parser.add_argument("-d", "--dest", type=str, help="Path to destination", default="/mnt/hp/NASA/json/RW26.json")
parser.add_argument("-c", "--convert", type=bool, help="Need to convert", default=False)
parsers = parser.parse_args()

if (parsers.convert) : tools.converter(parsers.source, parsers.dest)
data = tools.transformer(tools.loader(parsers.dest, isFile=True)['RW26.json']['data']['step'])
dataList = \
{
    'comment'    : tools.merger(data['comment'],     isCliped=True, clipStart=0, clipEnd=500),
    'type'       : tools.merger(data['type'],        isCliped=True, clipStart=0, clipEnd=500),
    'time'       : tools.merger(data['time'],        isCliped=True, clipStart=0, clipEnd=500),
    'voltage'    : tools.merger(data['voltage'],     isCliped=True, clipStart=0, clipEnd=500),
    'current'    : tools.merger(data['current'],     isCliped=True, clipStart=0, clipEnd=500),
    'temparature': tools.merger(data['temperature'], isCliped=True, clipStart=0, clipEnd=500)
}

print(data.head(5))
tools.plotter(dataList, 'time', ('voltage', 'current'), testName=os.path.split(parsers.dest)[1])