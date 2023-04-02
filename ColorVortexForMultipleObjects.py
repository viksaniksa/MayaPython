import maya.cmds as cmds


mySelection = cmds.ls(selection=True)

print(mySelection)

numObjects = len(mySelection)

print(numObjects)

Xcoordinate=0
Ycoordinate=0
Zcoordinate=0

for object in mySelection:
    numVertices = cmds.polyEvaluate(object, vertex=True)
    for i in range(numVertices):
        vertice=object + ".vtx[" + str(i) + "]"
        #print(object)
        #print(vertice)
            
        
        position = cmds.pointPosition(str(vertice), world=True)
        
    
        if position[0]<Xcoordinate:
            Xcoordinate=position[0]
            print("X changed to ",  Xcoordinate)
        
        if position[1]<Ycoordinate:
            Ycoordinate=position[1]
            print("Y changed to ",  Ycoordinate)
        
        if position[2]<Zcoordinate:
            Zcoordinate=position[2]
            print("Z changed to ", Zcoordinate)
        
print(Xcoordinate, Ycoordinate, Zcoordinate)

for object in mySelection:
    cmds.move(-Xcoordinate, -Ycoordinate, -Zcoordinate, object, relative=True)

print("Objects moved in x y z : ", Xcoordinate, Ycoordinate, Zcoordinate)

Xcoordinate=0
Ycoordinate=0
Zcoordinate=0

for object in mySelection:
    numVertices = cmds.polyEvaluate(object, vertex=True)
    for i in range(numVertices):
        vertice=object + ".vtx[" + str(i) + "]"
        #print(object)
        #print(vertice)
        position = cmds.pointPosition(str(vertice), world=True)
        
    
        if position[0]>Xcoordinate:
            Xcoordinate=position[0]
            print("X changed to ",  Xcoordinate)
        
        if position[1]>Ycoordinate:
            Ycoordinate=position[1]
            print("Y changed to ",  Ycoordinate)
        
        if position[2]>Zcoordinate:
            Zcoordinate=position[2]
            print("Z changed to ", Zcoordinate)

print(Xcoordinate, Ycoordinate, Zcoordinate)

for object in mySelection:
    numVertices = cmds.polyEvaluate(object, vertex=True)
    
    for i in range(numVertices):
        vertice=object + ".vtx[" + str(i) + "]"
        position = cmds.pointPosition(str(vertice), world=True)
        cmds.polyColorPerVertex(str(vertice), r=(position[0]/Xcoordinate), g=(position[1]/Ycoordinate), b=(position[2]/Zcoordinate))