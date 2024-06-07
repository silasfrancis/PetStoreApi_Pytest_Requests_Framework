import json

def readingJsonResponseFile(jsonfile):
    with open(jsonfile, 'r') as file:
        data = json.load(file)
        return data

def savingJsonResponseFile(jsonfile, jsondata):
    save_file = open(jsonfile , "w")
    json.dump(jsondata, save_file, indent = 4)
    save_file.close()
