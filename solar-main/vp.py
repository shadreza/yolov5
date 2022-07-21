from vpython import *
from time import *

mRadius = .5
wallThickness = .1
roomWidth = 12
roomDepth = 20
roomHeight = 2
floor = box(pos=vector(0, -roomHeight / 2, 0), size=vector(roomWidth, wallThickness, roomDepth), color=color.white)
ceiling = box(pos=vector(0, roomHeight / 2, 0), size=vector(roomWidth, wallThickness, roomDepth), color=color.white)
backWall = box(pos=vector(0, 0, -roomDepth / 2), size=vector(roomWidth, roomHeight, wallThickness), color=color.white)
leftWall = box(pos=vector(-roomWidth / 2, 0, 0), size=vector(wallThickness, roomHeight, roomDepth), color=color.white)
rightWall = box(pos=vector(roomWidth / 2, 0, 0), size=vector(wallThickness, roomHeight, roomDepth), color=color.white)
marble = sphere(radius=mRadius, color=color.red)
deltaX = .1
deltaY = .1
deltaZ = .1

xPos = 0
yPos = 0
zPos = 0

while True:
    rate(25)

    xPos = xPos + deltaX
    yPos = yPos + deltaY
    zPos = zPos + deltaZ

    Xrme = xPos + mRadius
    Xlme = xPos - mRadius
    Ytme = yPos + mRadius
    Ybme = yPos - mRadius
    Zbme = zPos - mRadius
    Zfme = zPos + mRadius

    Rwe = roomWidth / 2 - wallThickness / 2
    Lwe = -roomWidth / 2 + wallThickness / 2
    Cwe = roomHeight / 2 - wallThickness / 2
    FLOORwe = -roomHeight / 2 + wallThickness / 2
    Bwe = -roomDepth / 2 + wallThickness / 2
    Fwe = roomDepth / 2 - wallThickness / 2

    if (Xrme >= Rwe or Xlme <= Lwe):
        deltaX = deltaX * (-1)

    if (Ytme >= Cwe or Ybme <= FLOORwe):
        deltaY = deltaY * (-1)

    if (Zfme >= Fwe or Zbme <= Bwe):
        deltaZ = deltaZ * (-1)

    marble.pos = vector(xPos, yPos, zPos)