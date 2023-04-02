import maya.cmds as cmds


numVertices = cmds.polyEvaluate("pCube1", vertex=True)

#print(numVertices)
Xcoordinate=0
Ycoordinate=0
Zcoordinate=0

for i in range(numVertices):
    vertice="pCube1.vtx[" + str(i) + "]"
    position = cmds.pointPosition(str(vertice), world=True)
    print(vertice)
    
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

cmds.move(-Xcoordinate, -Ycoordinate, -Zcoordinate, "pCube1", relative=True)
print("Object moved in x y z : ", Xcoordinate, Ycoordinate, Zcoordinate)

Xcoordinate=0
Ycoordinate=0
Zcoordinate=0

for i in range(numVertices):
    vertice="pCube1.vtx[" + str(i) + "]"
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

for i in range(numVertices):
    vertice="pCube1.vtx[" + str(i) + "]"
    position = cmds.pointPosition(str(vertice), world=True)
    cmds.polyColorPerVertex(str(vertice), r=(position[0]/Xcoordinate), g=(position[1]/Ycoordinate), b=(position[2]/Zcoordinate))
    
