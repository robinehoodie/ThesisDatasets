import os
  
path = "C:\\Users\\robin\\OneDrive\\Desktop\\For data set gather"
  
os.chdir(path)
text= ""
y=0
for file in os.listdir():
    x=0
    if file.endswith(".txt"):
        text +='"'
        while file[x]!=".":
            text = text + file[x]
            x+=1
        text += '", '
        y+=1
        if y==4:
            text += "\n"
            y=0
            
print(text)
        