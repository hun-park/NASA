import argparse, os, tools

parser = argparse.ArgumentParser(description="Folder Path")
parser.add_argument("-s", "--source", type=str, help="Path of source files", default="/mnt/hp/NASA/data/")
parser.add_argument("-d", "--dest", type=str, help="Path to destination", default="/mnt/hp/NASA/json/RW26.json")
parser.add_argument("-c", "--convert", type=bool, help="Need to convert", default=False)
args, unknown = parser.parse_known_args()

if (args.convert) : tools.converter(args.source, args.dest)
data = tools.transformer(tools.loader(args.dest, isFile=True)['RW26.json']['data']['step'])
dischargeData = tools.transformer(tools.loader(args.dest, isFile=True)['RW26.json']['data']['step'],
                                  ['type', 'D'])

tools.timePlotter(data, 'time', ['voltage', 'current', 'temperature'], 
                  testName=os.path.split(args.dest)[1],
                  isCliped=True, clipStart=0, clipEnd=5)

tools.relativeTimePlotter(dischargeData, 'relativeTime', 'voltage', 
                          testName=os.path.split(args.dest)[1],
                          isCliped=True, clipStart=100, clipEnd=110)