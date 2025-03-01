import matplotlib.pyplot as pt

def focusgraph():
    file = open("Focus.txt","r")
    content = file.read()
    file.close()

    content = content.split(",")
    x1 = []
    for i in range(0,len(content)):
        content[i] = float(content[i])
        x1.append(i)

    y1 = content

    pt.plot(x1,y1,color = "red",marker = "o")
    pt.title("FOCUS TIME GRAPGH",fontsize = 14)
    pt.xlabel("Time",fontsize = 14)
    pt.ylabel("Focus Time",fontsize = 16)
    pt.grid
    pt.show()

