import os
import json
data = open("TextDataset/data.json", "r")
line= data.readline()
while line != "":
    read = json.loads(line)
    source = "AudioData/"+"Nacor" + "/"
    destination = "Datasets/"
    
    if read["key"] == "trainCebuano":
        destination += "trainCebuano/"

    elif read["key"] == "testCebuano":
        destination += "testCebuano/"
    
    elif read["key"] == "testMix":
        destination += "testMix/"
       
    elif read["key"] == "trainMix":
        destination += "trainMix/"
    
    source += read["location"]
    destination += read["location"]
    
    try:
        os.replace(source,destination)
    except FileNotFoundError:
        print("nope")
        
    line= data.readline()