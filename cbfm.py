"""
© Lopastudio 2021
© Patrik Nagy 2021
13.3.2021
"""
import time
from pycraft_minetest import *
print("COMPLETE BUILDER FOR MINETEST")
print("CBFM")
time.sleep(1)
print("BY PATRIK NAGY")
time.sleep(1)
print("© Lopastudio 2021")
time.sleep(1)
print("© Patrik Nagy 2021")
time.sleep(1)
print("13.3.2021")
time.sleep(1)


agent = Turtle(stone)
agent.speed(10)

def help():
    print("HELP MENU")
    print("COMPLETE BUILDER FOR MINETEST")
    print("CBFM")
    print("BY Patrik Nagy")
    time.sleep(3)
    print("")
    print("Build")
    print("Main Root Command To Build Block")
    time.sleep(3)
    print("")
    print("Change Block")
    print("Enter Name Of Block (air, brick, wood, tnt, stone)")
    time.sleep(5)
    print("")
    print("Bager")
    print("Dig a pit of any size")
    time.sleep(5)
    print("")
    print("left/right")
    print("left = Rotate Builder To -90°")
    print("right = Rotate Builder To 90°")
    time.sleep(5)
    print("")
    print("demo = Build Demo Project")
    time.sleep(5)
    print("")
    print("panelak_builder = Start panelak_builder Program")
    time.sleep(5)
    print("")
    print("ENJOY BUILDING VERY COOL STUFF")
    time.sleep(5)
    
def demo():
    agent.speed(10)
    agent.forward(50)
    chat ("command: build")
    agent.left(90)
    chat ("command: left")
    agent.forward(50)
    chat ("command: build")
    agent.left(90)
    chat ("command: left")
    agent.forward(50)
    chat ("command: build")
    agent.left(90)
    chat ("command: left")
    agent.forward(50)
    chat ("command: build")
    agent.left(90)
    chat ("command: left")
    
def patro(agent, sirka, dlzka, vyska):
    for _ in range(vyska):
        agent.forward(dlzka)
        agent.left(90)
        agent.forward(sirka)
        agent.left(90)
        agent.forward(dlzka)
        agent.left(90)
        agent.forward(sirka)
        agent.left(90)
        agent.up(90)
        agent.penup()
        agent.forward(1)
        agent.down(90)
        agent.pendown()
def panelak(agent, sirka, dlzka, vyska_panelaku, vyska_patro):
    for _ in range(vyska_panelaku):
        patro(agent, sirka, dlzka, vyska_patro)
def panelak_builder():
    agent = Turtle(diamond)
    agent.speed(11)
    vyska_patra = int(input("zadajte vysku poschodia: "))
    vyska_panelaku = int(input("zadajte vysku panelaku: "))
    dlzka = int(input("zadajte dlzku panelaku: "))
    sirka = int(input("zadajte sirku panelaku: "))
    panelak(agent, sirka, dlzka, vyska_panelaku, vyska_patra)

def bager():
    chat("Don't move!!!")
    chat("Don't move!!!")
    chat("Don't move!!!")
    velkostx = int(input("enter X:"))
    velkosty = int(input("enter Y:"))
    velkostz = int(input("enter Z:"))
    for i in range(velkostx):
        for j in range(velkosty):
            for k in range(velkostz):
                block(air, i, j, k)


    


    
while True:
    x = input("CBFM/ ")
    if x == "help":
        help()  
    if x == "demo":
        demo()
    if x == "bager":
        bager()
    if x == "panelak_builder":
        panelak_builder()
    if x == "build":
        agent.forward(1)
    if x == "left":
        agent.left(90)
    if x == "right":
        agent.right(90)
    if x == "air":
        agent.penblock(air)
    if x == "brick":
        agent.penblock(brick)
    if x == "stone":
        agent.penblock(stone)
    if x == "wood":
        agent.penblock(wood)
    if x == "tnt":
        agent.penblock(tnt)
    if x == "exit":
        break
