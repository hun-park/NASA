import os, tqdm, mat4py, json

def convert(sourcePath, destPath):
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

# merge lists of time-series data into one list

def merge(dataLists):
    returnDataList = []

    for dataList in dataLists:
        if (type(dataList) != list) : returnDataList += [dataList]
        else : returnDataList += dataList
    
    return returnDataList

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

def saveTxt(dataLists, fileName="temp"):
    with open(f'{fileName}.txt', 'w') as f : f.writelines(str(dataLists))