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
