from re import T
import json

person = [
        "Abadies", "Aberilla", "Abrillo", "Alcober", 
        "Amodia", "Amores", "Baay", "Balo",
        "Baquial", "Baygan", "Bebita", "Bebita_1",
        "Berame", "Bergado", "Bongcac", "Bornillo",
        "Briones", "Buena", "Camay", "Carcasona",
        "Cardinas", "Castillo", "Costibolo", "Cotejar",
        "Cubal", "Cuevas", "Degollacion", "DelaCuadra",
        "del_Castillo", "Doydora", "Dy", "Ebol",
        "Elivera", "Encio", "Enriquez", "Escobia",
        "Escoto", "Esquivel", "Estrada", "Evangelista",
        "Faelnar", "Gallentes", "Lentic", "Loretero",
        "Lozada", "Mayol", "Nacor", "Navasca",
        "Nuena", "Ochea", "Ochea_1", "Pastoril",
        "Pastoriza", "Ragot", "Rallos", "Ramo",
        "Ramos", "Ramos_1", "Ramos_2", "Roa",
        "Sagusay", "Salomon", "Santos", "Seno",
        "Talip", "Tao", "Tapar", "Tobeza",
        "Villamor", "Villondo"
        ]

data = open("TextDataset/data.json", "a")
w = open("TextDataset/trainCebuano.json","a")
v = open("TextDataset/trainMix.json", "a")
testCebu = open("TextDataset/testCebuano.json", "a")
testMix =open("TextDataset/testMix.json", "a")

choice  = ["CEB_Iso_NamesMale","CEB_Iso_Airlines", 
           "CEB_Iso_Cities", "CEB_Iso_Companies", 
           "CEB_Iso_Hotels", "CEB_Iso_Landmarks",
           "CEB_Iso_NamesFem", "CEB_Iso_Surnames_Countries",
           "CEB_Utt_EngShib1", "CEB_Utt_EngShib2",
           "CEB_Iso_Landmarks"
           ]

Is = True

curr= ""
for name in person:
    f = open("TextData/"+name+".txt","r")
    line = f.readline()
    first= 0
    try:
        while Is:
            datawrite= []
            adder=[]
            x=0
            y=0
            u= ""
            check =0
            o=29
            key2 = ""
            text= ""
            key = ""

            while True:
                if line[o]=='.' or line[o] == '"':
                    break
                u= u+ line[o]
                o+=1
        

            for z in choice:
                if u==z:
                    check = 1

            if first == 0:
                x+=3
                first = 1
                while x!= 30:
                    key = key + line[x]
                    key2 = key2 + line[x]
                    x +=1
            else:
                while x!= 27:
                    key = key + line[x]
                    key2 = key2 + line[x]
                    x +=1
        
            while y != 3:
                if(line[x] == '"'):
                    y += 1
                x += 1

            if line[x] == '"' and line[x+1] != ' ':
                x+=1
            
            while line[x]!='"':
            
                if line[x] == "'":
                    x+=1
                if line[x] == '(' or line[x] == '-' or line[x]=="." or line[x].isspace():

                    if line[x+1] == '-':
                        while line[x] == '-':
                                x +=1
                    elif line[x]=='(':
                        while line[x-1] != ')':
                            x +=1
                    elif line[x] ==".":
                        x+=1
                        
                if line[x]!='"':
                    text = text + line[x]
                    x +=1
                if line[x] == '"' and line[x+1] == ' ' and line[x+2].isalpha():
                    x+=1
                if line[x] == '"' and line[x+1].isalpha():
                    x+=1
            
        
            if check == 0:
                if curr != u:
                    adder.append({
                        "key": "Datasets/testCebuano/" + key,
                        "text": text
                    })
                    testCebu.write(json.dumps(adder[0])+ '\n')
                    datawrite.append({
                        "key": "testCebuano",
                        "name" : name,
                        "location": key2
                    }, )
                    data.write(json.dumps(datawrite[0])+ '\n')
                    curr = u
                else:
                    adder.append({
                        "key": "Datasets/trainCebuano/" +key,
                        "text": text
                    })
                    w.write(json.dumps(adder[0])+ '\n')
                    datawrite.append({
                        "key": "trainCebuano",
                        "name" : name,
                        "location": key2
                    })
                    data.write(json.dumps(datawrite[0])+ '\n')
            else:
                if curr != u:
                    adder.append({
                        "key": "Datasets/testMix/" + key,
                        "text": text
                    })
                    testMix.write(json.dumps(adder[0])+ '\n')
                    datawrite.append({
                        "key": "testMix",
                        "name" : name,
                        "location": key2
                    })
                    data.write(json.dumps(datawrite[0]) + '\n')
                    curr = u
                else:
                    adder.append({
                        "key": "Datasets/trainMix/" + key,
                        "text": text
                    })
                    v.write(json.dumps(adder[0])+ '\n')
                    datawrite.append({
                        "key": "trainMix",
                        "name" : name,
                        "location": key2
                    })
                    data.write(json.dumps(datawrite[0])+ '\n')
            line = f.readline()
    except:
        print("sad")