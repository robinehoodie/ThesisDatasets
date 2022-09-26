import unicodedata
f = open("data.txt","r")
w = open("train.txt","a")

start = 23
end = 23
pos=1
i=0

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

while i < pos:
    line = f.readline()
    i+=1

Is = 0
while Is == 0:
    key = '{"key": ' + '"C:\\' + "training_data\\" + "training.json\\"
    x=0
    y=0
    j=20
    z = ""
    while j!= 23:
        z = z + line[j]
        j+=1
    if(int(z) <= end):
        while x!= 27:
            key = key + line[x]
            x +=1
        key = key + '"'
        while y != 3:
            if(line[x] == '"'):
                y += 1
            x += 1
        key =key + ', "text": "'
        while line[x] != '"':
            if line[x] == '(' or line[x] == '-' or line[x]=="." or line[x].isspace():
                if line[x+1] == '-':
                    while line[x] == '-':
                         x +=1
                elif line[x]=='(':
                    while line[x-1] != ')':
                        x +=1
                elif line[x] ==".":
                    x+=1
                elif line[x].isspace() and line[x+1].isspace():
                    x+1
                    
            if(line[x]!='"'):
                # output = unicodedata.normalize('NFKD', line[x])
                output = remove_accents(line[x])
                # output.decode("utf-8")
                # .encode('ascii', 'ignore').decode("utf-8")
                # # print(output)
                # output = line[x]
                # print(output)
                # print(unidecode.unidecode(output))
                print(output)
                key = key + line[x]
                x +=1
            
        key= key + '"}'
        w.write("\n")
        w.write(key)
        line = f.readline()
    else:
        Is=1

