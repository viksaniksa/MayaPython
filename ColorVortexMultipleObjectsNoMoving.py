import maya.cmds as cmds


mySelection = cmds.ls(selection=True)

print(mySelection)

numObjects = len(mySelection)

print(numObjects)

xCoords=[]
yCoords=[]
zCoords=[]

for object in mySelection:
    numVertices = cmds.polyEvaluate(object, vertex=True)
    for i in range(numVertices):
        vertice=object + ".vtx[" + str(i) + "]"
        #print(object)
        #print(vertice)
        position = cmds.pointPosition(str(vertice), world=True)
        xCoords.append(position[0])
        yCoords.append(position[1])
        zCoords.append(position[2])
            
print(max(xCoords), max(yCoords), max(zCoords))
print(min(xCoords), min(yCoords), min(zCoords))

for object in mySelection:
    numVertices = cmds.polyEvaluate(object, vertex=True)
    
    for i in range(numVertices):
        vertice=object + ".vtx[" + str(i) + "]"
        position = cmds.pointPosition(str(vertice), world=True)
        red=(position[0]-min(xCoords))/(max(xCoords)-min(xCoords))
        green=(position[1]-min(yCoords))/(max(yCoords)-min(yCoords))
        blue=(position[2]-min(zCoords))/(max(zCoords)-min(zCoords))
        cmds.polyColorPerVertex(str(vertice), r=red , g=green , b=blue)