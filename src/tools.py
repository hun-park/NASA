import os, tqdm, mat4py, json, pandas, plotly.graph_objects

# convert mat-5 files into json
def converter(sourcePath, destPath):
    os.chdir(sourcePath)
    sourceNames = os.listdir(sourcePath)

    if (os.path.exists(destPath)):
        os.chdir(destPath)
        destNames = os.listdir(destPath)
        for destName in destNames: os.remove(destName)
        os.chdir(sourcePath)
    else : os.mkdir(destPath)

    for sourceName in tqdm.tqdm(sourceNames):
        if (os.path.isfile(sourceName)):
            _convert(destPath, sourceName)

def _convert(filePath, fileName): 
    with open(f"{filePath}{os.path.splitext(fileName)[0]}.json", "w") as jsonFile:
        json.dump(mat4py.loadmat(f"{fileName}"), jsonFile)

# transform python dictionay data structure into pandas dataframe
def transformer(dataLists):
    return pandas.DataFrame.from_dict(dataLists)

# merge lists of time-series data into one list
def merger(dataLists, isCliped=False, clipStart=0, clipEnd=-2):
    returnDataList = []

    if (isCliped) :
        for dataList in dataLists[clipStart:clipEnd+1]:
            if (type(dataList) != list) : returnDataList += [dataList]
            else : returnDataList += dataList
        
        return returnDataList
    else :
        for dataList in dataLists:
            if (type(dataList) != list) : returnDataList += [dataList]
            else : returnDataList += dataList
        
        return returnDataList

# check data is monotonic
def isMonotonic(dataLists, monotonicParam=1):
    for index in range(len(dataLists)):
        if index < len(dataLists) - 1:
            if monotonicParam*(dataLists[index] - dataLists[index + 1]) > 0 : 
                if (monotonicParam ==1) : return isMonotonic(dataLists, monotonicParam=-1)
                else : 
                    print("not monotonic")
                    break
        else : 
            if (monotonicParam ==1) : print("monotonic increase")
            else : print("monotonic decrease")

# save list as text file
def saveTxt(dataLists, fileName="temp"):
    with open(f'{fileName}.txt', 'w') as f : f.writelines(str(dataLists))

# load json files as dictionary
def loader(destPath, isFile=False, toDataFrame=False):
    dataDicts = dict()

    if (isFile):
        with open(destPath) as f:
            jsonData = json.load(f)
            
        dataDicts[os.path.split(destPath)[1]] = jsonData
    else:
        fileNames = os.listdir(destPath)
        os.chdir(destPath)

        for fileName in tqdm.tqdm(fileNames):
            if (os.path.isfile(fileName)):
                with open(os.path.join(destPath, fileName)) as f:
                    jsonData = json.load(f)
            
            dataDicts[fileName] = jsonData
    if (toDataFrame) : return pandas.DataFrame.from_dict(dataDicts)
    else : return dataDicts

# plot graph
def plotter(data, x_axis, y_axises, isSave=True, format='png', testName='temp'):
    fig = plotly.graph_objects.Figure()

    for y_axis in y_axises:
        fig.add_trace(plotly.graph_objects.Scatter(x=data[x_axis], y=data[y_axis], name=f'{y_axis}'))
    fig.write_html(f'{testName}_{x_axis}_{str(y_axises)}.html')

    fig.show()
    if (isSave) : return fig.write_image(f'{testName}_{x_axis}_{y_axis}.{format}', format=format)
    else : return fig
