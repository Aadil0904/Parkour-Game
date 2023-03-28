#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 20:08:41 2021

@author: aadilshaikh
"""

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random as rd
app = Ursina()
window.fullscreen = True
class Voxel(Entity):           #platform cubes
    def __init__(self, position = (0, 0, 0)): 
        super().__init__(
            position = position,
            model = 'cube', 
            origin_y = 0.18,
            scale_x = 4,
            scale_z = 4,
            scale_y = 4,
            texture = 'icetexture.jpg',
            color = color.white, 
            highlight = color.lime,
            collider = 'box'
        )
    def input(self, key):
        if key == 'escape':
            quit()

class Voxel2(Entity):          #obstacles
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            position = position,
            model = 'cube', 
            origin_y = 0.2,
            scale_x = 4,
            scale_z = 4,
            scale_y = 7,
            texture = 'white_cube',
            color = color.white66, 
            highlight = color.lime,
            collider = 'box'
        )

class Voxel3(Entity):           #secret route
    def __init__(self, position = (0, 0, 0)): 
        super().__init__(
            position = position,
            model = 'cube', 
            origin_y = 0.18,
            scale_x = 4,
            scale_z = 4,
            scale_y = 4,
            texture = 'white_cube',
            color = color.rgba(0,0,0,0), 
            highlight = color.lime,
            collider = 'box'
        )

ent1 = Entity(position = (0,0,0),   #start black platform
            model = 'cube', 
            scale_x = 4.2,
            scale_z = 4.2,
            scale_y = 4,
            texture = 'icetexture.jpg',
            color = color.black, 
            highlight = color.lime,
            collider = 'box'
        )
ent2 = Entity(position = (114,-16,114),  #end black platform
            model = 'cube', 
            scale_x = 4.2,
            scale_z = 4.2,
            scale_y = 4,
            texture = 'icetexture.jpg',
            color = color.rgba(0,0,0,0), 
            highlight = color.lime,
            collider = 'box'
        )


for z in range(0,120,6):
    for x in range(0,120,6):
        if x==0 and z==0:
            continue
        voxel = Voxel(position = (x, 0, z))
sec_rot = []
for x in range(96,126,4):
    voxel = Voxel3(position=(x,0,-4))
    sec_rot.append(voxel)
for z in range(-4,120,4):
    '''if z==104:
        continue'''
    voxel = Voxel3(position=(x,0,z))
    sec_rot.append(voxel)

cp=0
chp = []
while cp<4:
    z = rd.randrange(0,115,36)
    x = rd.randrange(0,115,36)
    hit_info = raycast((x,0,z), (0,1,0))
    if hit_info.entity.color!=color.orange and (x!=0 and z!=0) and (x!=114 and z!=114):
        hit_info.entity.color = color.orange
        cp+=1
        chp.append(hit_info.entity)

hit_info = raycast((114,0,112),(0,180,0), ignore=(ent1,))
hit_info.entity.color = color.blue
edp = hit_info.entity

voxel2 = []
v2p = []
for i in range(0, 20):
    j = rd.randrange(-1,2,2)
    v2p.append(j)
for z in range(0,120,6):
    x = rd.randint(4,120)
    voxel2.append(Voxel2(position = (x, 6, z)))



player = FirstPersonController()
player.collider = 'box'
hit_info = raycast(player.position, (0,180,0), ignore=(player,ent1))
q = 1
j = 0
cp= 0
sp= 0
new_time=0
old_time=new_time 
info = Text(text = "Time: "+str(int(new_time))+"s", scale = 1, x = -0.79, y = 0.465, color = color.red)
check_info = Text(text = "Check Points Reached: "+str(cp)+"/4", scale = 1, x = -0.79, y = 0.49,color=color.red)
secret_passage = Text(text = "Secret-Passage found: "+str(sp)+"/1", scale = 1, x = -0.79, y = 0.44, color = color.red)
Game_Over = Text(text = "GAME OVER", scale = 5, color = color.black66, x=0, y=0,font='VeraMono.ttf')
Game_Over.x = 0-(Game_Over.width/2)
Game_Over.y = 0+(Game_Over.height/2)
Game_Over.visible = False
Finish = Text(text = "LEVEL 3 COMPLETED!", scale = 5, color = color.white66, x=0, y=0,font='VeraMono.ttf')
Finish.x = 0-(Finish.width/2)
Finish.y = 0+(Finish.height/2)
Finish.visible = False
c = 0
flag1 = flag2 = 0
def update():
    global hit_info
    global new_time,old_time
    global player
    global q, j, c, flag1, flag2, cp,sec_rot,sp
    global info, check_info, secret_passage
    global Game_Over
    lt = time.dt
    new_time += lt
    new_time = float("{:.2f}".format(new_time))
    ent = hit_info.entity
    hit_info = raycast(player.position, (0,1,0), ignore=(player,ent1), distance =0.2) #to get the entity below the player
    for i in range(0,20): #pushing the player on colliding with the obstacles
        if voxel2[i].x > 118:
            v2p[i] = -1
        elif voxel2[i].x < -4:
            v2p[i] = 1
        if player.intersects(voxel2[i]).hit:
            if v2p[i] == -1:
                if voxel2[i].x - player.x<=3:
                    player.x -= 0.25
            elif v2p[i] == 1:
                if player.x - voxel2[i].x<=3:
                    player.x += 0.25
            elif player.z - voxel2[i].z <= 2.2:
                player.z = voxel2[i].z+2.2
            elif voxel2[i].z - player.z <= 2.2:
                player.z = voxel2[i].z-2.2
        voxel2[i].x=voxel2[i].x + 0.2*v2p[i]


    if hit_info.hit: #color changing and destruction of the platforms
        if hit_info.entity in sec_rot:
            hit_info.entity.color = color.black
            sp=1
            secret_passage.text = "Secret-Passage found "+str(sp)+"/1"
        if voxel2 != hit_info.entity and hit_info.entity.color!=color.rgba(0,0,0,0) and hit_info.entity.color!=color.black and hit_info.entity not in chp: #drift
            player.x+=0.025
        r = rd.randint(0,1)
        if ent != hit_info.entity:
            if hit_info.entity.color == color.orange:
                hit_info.entity.color = color.brown
                cp+=1
                check_info.text = "Check Points Reached: "+str(cp)+"/4"
            elif(hit_info.entity==edp and hit_info.entity !=ent2 and cp==4):
                edp.color = color.black
                destroy(edp, delay = 2)
            else:
                if r == 1 and hit_info.entity.color==color.white:
                    hit_info.entity.color = color.green
                elif r==0 and hit_info.entity.color==color.white:
                    hit_info.entity.color = color.red
                    destroy(hit_info.entity, delay = 2)

    if (new_time)!=(old_time) and c==0:
        info.text = "Time: "+str(new_time)+"s"
    old_time = new_time
    if player.y<-70 and flag2==0:
        Game_Over.visible = True
        j+=time.dt
        flag1 = 1
        if j>3:
            quit()
    if hit_info.hit:
        if hit_info.entity==ent2 and flag1==0:
            ent2.color = color.black
            Finish.visible = True
            c=1
            flag2 = 1
            j+=time.dt
            if j>3:
                import mysql.connector as connector
                with open ("player.txt","r") as myfile:
                    Data = myfile.readline()
                    mylistdata = Data.split('~')
                    val = tuple(mylistdata)
                    Final_time = str(new_time-3.23)
            
                mycon=connector.connect(host='localhost', user='root', passwd='istanbul2005', database='podar12_21')
                if mycon.is_connected==False:
                    print("Error connecting to database:")
                else:
                    myQry="UPDATE PlayerData set HighScore3 = "+Final_time+" where User_ID = %s and Password = %s and ("+Final_time+"<HighScore3)"
                    myCursor=mycon.cursor()
                    myCursor.execute(myQry,val)
                    mycon.commit()      
                mycon.close()                
                quit()
    if flag2==1 and player.y<-70:
        j+=time.dt
        if j>3:
            quit()
    
app.run()