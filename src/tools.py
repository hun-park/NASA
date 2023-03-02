import os, tqdm, mat4py, json, pandas, plotly.graph_objects, plotly.subplots

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

# transform python dictionay data structure into pandas dataframe
def transformer(dataLists, onlyInclude=[None, None]):
    if (onlyInclude == [None, None]) :
        return pandas.DataFrame.from_dict(dataLists)
    else :
        data = pandas.DataFrame.from_dict(dataLists)
        return data.loc[data[onlyInclude[0]] == onlyInclude[1]]

# merge lists of time-series data into one list
def merger(dataLists, isCliped=False, clip=[0,-2]):
    returnDataList = []

    if (isCliped) :
        for dataList in dataLists[clip[0]:clip[1]+1]:
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

# plot graph along time
def timePlotter(data, x_axis, y_axises, isCliped=False, clip=[0,-2], isSave=True, format='png', testName='temp'):
    dataList = dict()
    for key in list(data.keys()):
        dataList[key] = merger(data[key], isCliped, clip)
    
    if (len(y_axises) == 1) :
        fig = plotly.graph_objects.Figure()
        fig.add_trace(plotly.graph_objects.Scatter(x=dataList[x_axis], y=dataList[y_axises[0]], name=f'{y_axises}'))
    else :
        fig = plotly.subplots.make_subplots(rows=len(y_axises), cols=1, shared_xaxes=True, subplot_titles=y_axises)
        for index in range(len(y_axises)):
            fig.add_trace(plotly.graph_objects.Scatter(x=dataList[x_axis], y=dataList[y_axises[index]], name=f'{y_axises[index]}'), row=index+1, col=1)
    
    fig.write_html(f'{testName}_{x_axis}_{str(y_axises)}.html')
    fig.write_image(f'{testName}_{x_axis}_{str(y_axises)}.{format}', format=format)

    if (isSave) : return fig
    else : return fig

# plot graph along relativeTime
def relativeTimePlotter(data, x_axis, y_axises, isCliped=False, clip=[0,-2], isSave=True, format='png', testName='temp'):
    parkingLot = data.to_dict()
    keyRing = list(data.to_dict()['time'].keys())

    if (len(y_axises) == 1) :
        fig = plotly.graph_objects.Figure()

        if (isCliped):
            for key in keyRing[clip[0]:clip[1]+1]:
                fig.add_trace(plotly.graph_objects.Scatter(x=parkingLot[x_axis][key], y=parkingLot[y_axises][key], name=f'{y_axises}_{key}'))
        else :
            for key in keyRing:
                fig.add_trace(plotly.graph_objects.Scatter(x=parkingLot[x_axis][key], y=parkingLot[y_axises][key], name=f'{y_axises}_{key}'))
    else:
        fig = plotly.subplots.make_subplots(rows=len(y_axises), cols=1, shared_xaxes=True, subplot_titles=y_axises)

        for index in range(len(y_axises)):
            if (isCliped):
                for key in keyRing[clip[0]:clip[1]+1]:
                    fig.add_trace(plotly.graph_objects.Scatter(x=parkingLot[x_axis][key], y=parkingLot[y_axises[index]][key], name=f'{y_axises[index]}_{keyRing.index(key)}'), row=index+1, col=1)
            else :
                for key in keyRing:
                    fig.add_trace(plotly.graph_objects.Scatter(x=parkingLot[x_axis][key], y=parkingLot[y_axises[index]][key], name=f'{y_axises[index]}_{keyRing.index(key)}'), row=index+1, col=1)


    fig.write_html(f'{testName}_{x_axis}_{str(y_axises)}.html')
    fig.write_image(f'{testName}_{x_axis}_{str(y_axises)}.{format}', format=format)

    if (isSave) : return fig
    else : return fig