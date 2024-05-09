from tkinter import *
import time as t
import math as m
from PIL import Image

root=Tk()

boom_image=PhotoImage(file="boom.gif")
heart_image=PhotoImage(file="heart.png")
cannon_l=PhotoImage(file="cannon.png")
cannon_r=PhotoImage(file="cannon.png")
bulletf=PhotoImage(file="bullet.png")
game_over=PhotoImage(file="GAMEOVER.png")
menu_image=PhotoImage(file="menu-1.png")
sky = PhotoImage(file="sky.png")
background = PhotoImage(file="NewBG.png")
skeleton1_image=PhotoImage(file="skeleton.gif")
skeleton2_image=PhotoImage(file="skeleton.gif")
skeleton3_image=PhotoImage(file="skeleton.gif")
skeleton4_image=PhotoImage(file="skeleton.gif")
skull1_image=PhotoImage(file="skull.gif")
skull2_image=PhotoImage(file="skull.gif")
golem1_image = PhotoImage(file="Golem.gif")
gob1_image=PhotoImage(file="goblin1.gif")
gob2_image=PhotoImage(file="goblin2.gif")
width1 = sky.width()
height1 = sky.height()
wave1_image=PhotoImage(file="wave1.png")
wave2_image=PhotoImage(file="wave2.png")
exit_image=PhotoImage(file="exit.png")
 
frame = Canvas(root,width=width1,height=height1)
frame.pack(expand=1)

layer0=frame.create_image(width1/2,height1/2,image=sky)

"""On cree les mobs pour le controle des niveaux plus tard"""

goblin1=frame.create_image(0,height1-55,image=gob1_image) 

goblin2=frame.create_image(0,height1-55,image=gob1_image) 

goblin3=frame.create_image(0,height1-55,image=gob1_image)

goblin4=frame.create_image(0,height1-55,image=gob1_image)

goblin5=frame.create_image(0,height1-55,image=gob1_image)

goblin6=frame.create_image(0,height1-55,image=gob1_image)

golem1=frame.create_image(-35,height1-95,image=golem1_image)

golem2=frame.create_image(-35,height1-95,image=golem1_image)

golem3=frame.create_image(-35,height1-95,image=golem1_image)

skeleton1=frame.create_image(1060,height1-65,image=skeleton1_image)
skeleton2=frame.create_image(1060,height1-65,image=skeleton2_image)
skeleton3=frame.create_image(1060,height1-65,image=skeleton3_image)
skeleton4=frame.create_image(1060,height1-65,image=skeleton4_image)
skeleton5=frame.create_image(1060,height1-65,image=skeleton1_image)
skeleton6=frame.create_image(1060,height1-65,image=skeleton2_image)
skeleton7=frame.create_image(1060,height1-65,image=skeleton3_image)
skeleton8=frame.create_image(1060,height1-65,image=skeleton4_image)

skull1=frame.create_image(1060,height1-105,image=skull1_image)
skull2=frame.create_image(1060,height1-135,image=skull2_image)
skull3=frame.create_image(1060,height1-175,image=skull1_image)
skull4=frame.create_image(1060,height1-195,image=skull2_image)

layer1=frame.create_image(width1/2,height1/2,image=background)

menu=frame.create_image(518,225,image=menu_image)



bullet_l1=frame.create_image(490, 70, image=bulletf)
bullet_l2=frame.create_image(490, 70, image=bulletf)
bullet_l3=frame.create_image(490, 70, image=bulletf)
bullet_l4=frame.create_image(490, 70, image=bulletf)

bullet_r1=frame.create_image(545, 70, image=bulletf)
bullet_r2=frame.create_image(545, 70, image=bulletf)
bullet_r3=frame.create_image(545, 70, image=bulletf)
bullet_r4=frame.create_image(545, 70, image=bulletf)

cannon_right=frame.create_image(545,70, image=cannon_r)

cannon_left=frame.create_image(490,70, image=cannon_l)

wave1=frame.create_image(456,-29,image=wave1_image)
exito=frame.create_image(380,-29,image=exit_image)
wave2=frame.create_image(304,-29,image=wave2_image)

heart1=frame.create_image(485,45,image=heart_image)
heart2=frame.create_image(505,45,image=heart_image)
heart3=frame.create_image(525,45,image=heart_image)
heart4=frame.create_image(545,45,image=heart_image)

def cannon_shoot_coords(event):
    global can_shoot
    if can_shoot==1:
        vitesse=1500
        x=event.x
        y=event.y
        if x<490:    
            distance=x-490
            hauteur=y-70
            diagonale=m.sqrt((distance**2)+(hauteur**2))
            temps=diagonale/vitesse
            n_frames=(temps/0.016666)
            global vitessel_x
            global vitessel_y
            vitessel_x=distance/n_frames
            vitessel_y=hauteur/n_frames
        if x>545:
            distance=x-545
            hauteur=y-70
            diagonale=m.sqrt((distance**2)+(hauteur**2))
            temps=diagonale/vitesse
            n_frames=(temps/0.016666)
            global vitesser_x
            global vitesser_y
            vitesser_x=distance/n_frames
            vitesser_y=hauteur/n_frames
        can_shoot=0
        
def leave(event):
    root.destroy()

def test1(event):
    global wave_1

    wave_1=1
    
def test2(event):
    global wave_2

    wave_2=1

def menuclick(event):
    
    global paused
    
    if paused==1:
        paused=0
        for i in range(0,32):
            g=9.8*((i/20)**2)
            frame.move(wave1,0,-g)
            frame.update()
            t.sleep(0.016666)
        for i in range(0,32):
            g=9.8*((i/20)**2)
            frame.move(exito,0,-g)
            frame.update()
            t.sleep(0.016666)
        for i in range(0,32):
            g=9.8*((i/20)**2)
            frame.move(wave2,0,-g)
            frame.update()
            t.sleep(0.016666)
        
        
        
    else:
        paused=1
        for i in range(0,32):
            g=9.8*((i/20)**2)
            frame.move(wave1,0,g)
            frame.update()
            t.sleep(0.016666)
        for i in range(0,32):
            g=9.8*((i/20)**2)
            frame.move(exito,0,g)
            frame.update()
            t.sleep(0.016666)
        for i in range(0,32):
            g=9.8*((i/20)**2)
            frame.move(wave2,0,g)
            frame.update()
            t.sleep(0.016666)





def reset_bullet(objeto):
    global cycle_r,cycle_l,cycle_r_old,cycle_l_old,active_r1,active_r2,active_r3,active_r4,active_l1,active_l2,active_l3,active_l4
    global bullet_l1,bullet_l2,bullet_l3,bullet_l4,bullet_r1,bullet_r2,bullet_r3,bullet_r4
    x,y=frame.coords(objeto)
    if x>545:
        if objeto==bullet_r1:
            active_r1=0
        if objeto==bullet_r2:
            active_r2=0
        if objeto==bullet_r3:
            active_r3=0
        if objeto==bullet_r4:
            active_r4=0
        cycle_r_old=cycle_r
        cycle_r=0
        reset_x=545-x
        reset_y=70-y
        frame.move(objeto,reset_x,reset_y)
        
    if x<490:
        if objeto==bullet_l1:
            active_l1=0
        if objeto==bullet_l2:
            active_l2=0
        if objeto==bullet_l3:
            active_l3=0
        if objeto==bullet_l4:
            active_l4=0
        cycle_l_old=cycle_l
        cycle_l=0
        reset_x=490-x
        reset_y=70-y
        frame.move(objeto,reset_x,reset_y)
        
def bullet(vitesser_x,vitesser_y,vitessel_x,vitessel_y):

    global cycle_r,cycle_l,cycle_r_old,cycle_l_old,active_r1,active_r2,active_r3,active_r4,active_l1,active_l2,active_l3,active_l4
    global vitesse_r1_x,vitesse_r1_y,vitesse_r2_x,vitesse_r2_y,vitesse_r3_x,vitesse_r3_y,vitesse_r4_x,vitesse_r4_y,vitesse_l1_x,vitesse_l1_y,vitesse_l2_x,vitesse_l2_y,vitesse_l3_x,vitesse_l3_y,vitesse_l4_x,vitesse_l4_y
    global bullet_l1,bullet_l2,bullet_l3,bullet_l4,bullet_r1,bullet_r2,bullet_r3,bullet_r4

    
    xL1,yL1=frame.coords(bullet_l1)
    xL2,yL2=frame.coords(bullet_l2)
    xL3,yL3=frame.coords(bullet_l3)
    xL4,yL4=frame.coords(bullet_l4)
    xR1,yR1=frame.coords(bullet_r1)
    xR2,yR2=frame.coords(bullet_r2)
    xR3,yR3=frame.coords(bullet_r3)
    xR4,yR4=frame.coords(bullet_r4)

    if xL1<0 or yL1>230 or yL1<0:

        active_l1=0
        cycle_l_old=cycle_l
        cycle_l=0
        reset_x=490-xL1
        reset_y=70-yL1
        frame.move(bullet_l1,reset_x,reset_y)
        hit(xL1,yL1)


    if xL2<0 or yL2>230 or yL2<0:

        active_l2=0
        cycle_l_old=cycle_l
        cycle_l=0
        reset_x=490-xL2
        reset_y=70-yL2
        frame.move(bullet_l2,reset_x,reset_y)
        hit(xL2,yL2)


    if xL3<0 or yL3>230 or yL3<0:

        active_l3=0
        cycle_l_old=cycle_l
        cycle_l=0
        reset_x=490-xL3
        reset_y=70-yL3
        frame.move(bullet_l3,reset_x,reset_y)
        hit(xL3,yL3)


    if xL4<0 or yL4>230 or yL4<0:

        active_l4=0
        cycle_l_old=cycle_l
        cycle_l=0
        reset_x=490-xL4
        reset_y=70-yL4
        frame.move(bullet_l4,reset_x,reset_y)
        hit(xL4,yL4)


    if xR1>1036 or yR1>230 or yR1<0:

        active_r1=0
        cycle_r_old=cycle_r
        cycle_r=0
        reset_x=545-xR1
        reset_y=70-yR1
        frame.move(bullet_r1,reset_x,reset_y)
        hit(xR1,yR1)


    if xR2>1036 or yR2>230 or yR2<0:

        active_r2=0
        cycle_r_old=cycle_r
        cycle_r=0
        reset_x=545-xR2
        reset_y=70-yR2
        frame.move(bullet_r2,reset_x,reset_y)
        hit(xR2,yR2)


    if xR3>1036 or yR3>230 or yR3<0:

        active_r3=0
        cycle_r_old=cycle_r
        cycle_r=0
        reset_x=545-xR3
        reset_y=70-yR3
        frame.move(bullet_r3,reset_x,reset_y)
        hit(xR3,yR3)

    if xR4>1036 or yR4>230 or yR4<0:

        active_r4=0
        cycle_r_old=cycle_r
        cycle_r=0
        reset_x=545-xR4
        reset_y=70-yR4
        frame.move(bullet_r4,reset_x,reset_y)
        hit(xR4,yR4)

    
    if cycle_r==1:

        active_r1=1
        vitesse_r1_x=vitesser_x
        vitesse_r1_y=vitesser_y
        
    if cycle_r==2:

        active_r2=1
        vitesse_r2_x=vitesser_x
        vitesse_r2_y=vitesser_y
        
    if cycle_r==3:

        active_r3=1
        vitesse_r3_x=vitesser_x
        vitesse_r3_y=vitesser_y

    if cycle_r==4:

        active_r4=1
        vitesse_r4_x=vitesser_x
        vitesse_r4_y=vitesser_y

    if cycle_l==1:

        active_l1=1
        vitesse_l1_x=vitessel_x
        vitesse_l1_y=vitessel_y

    if cycle_l==2:

        active_l2=1
        vitesse_l2_x=vitessel_x
        vitesse_l2_y=vitessel_y

    if cycle_l==3:

        active_l3=1
        vitesse_l3_x=vitessel_x
        vitesse_l3_y=vitessel_y

    if cycle_l==4:
        
        active_l4=1
        vitesse_l4_x=vitessel_x
        vitesse_l4_y=vitessel_y

    if active_r1==1:

        frame.move(bullet_r1,vitesse_r1_x,vitesse_r1_y)
        hitboxes(bullet_r1)
        
    if active_r2==1:

        frame.move(bullet_r2,vitesse_r2_x,vitesse_r2_y)
        hitboxes(bullet_r2)
        
    if active_r3==1:

        frame.move(bullet_r3,vitesse_r3_x,vitesse_r3_y)
        hitboxes(bullet_r3)
        
    if active_r4==1:

        frame.move(bullet_r4,vitesse_r4_x,vitesse_r4_y)
        hitboxes(bullet_r4)
    if active_l1==1:

        frame.move(bullet_l1,vitesse_l1_x,vitesse_l1_y)
        hitboxes(bullet_l1)
        
    if active_l2==1:

        frame.move(bullet_l2,vitesse_l2_x,vitesse_l2_y)
        hitboxes(bullet_l2)
        
    if active_l3==1:

        frame.move(bullet_l3,vitesse_l3_x,vitesse_l3_y)
        hitboxes(bullet_l3)
        
    if active_l4==1:
        
        frame.move(bullet_l4,vitesse_l4_x,vitesse_l4_y)
        hitboxes(bullet_l4)
        
def cannon_rotation():
    x=root.winfo_pointerx()-root.winfo_rootx()
    y=root.winfo_pointery()-root.winfo_rooty()    
    if x<490:
        rel_x1=x-490
        rel_y1=y-70
        angle=m.atan2(rel_x1,rel_y1)
        angle=angle*60
        cl=Image.open('cannon.png')
        out_l=cl.rotate(angle)
        out_l.save('cannon_r_l.png')
        cannon_l.configure(file='cannon_r_l.png')
        
    elif x>545:
        rel_x2=x-545
        rel_y2=y-70
        angle=m.atan2(rel_x2,rel_y2)
        angle=angle*60
        cr=Image.open('cannon.png')
        out_r=cr.rotate(angle)
        out_r.save('cannon_r_r.png')
        cannon_r.configure(file='cannon_r_r.png')

def cycle(event):
    global can_shoot
    if can_shoot==1:
        x=event.x
        global cycle_r,cycle_l,cycle_l_old,cycle_r_old
    
        if x<490:
            cycle_l=cycle_l_old
            cycle_l=cycle_l+1
            cycle_l_old=cycle_l
        
            if cycle_l>4:

                cycle_l=1

            print(cycle_l)

        if x>545:
            cycle_r=cycle_r_old
            cycle_r=cycle_r+1
            cycle_r_old=cycle_r

            if cycle_r>4:
            
                cycle_r=1

    
        

def hitboxes(obiectum):
    #CS=[]#liste avec les coordonnÃ©es de l'object 
    #CS.append(frame.coords(obiectum))
    x1,y1=frame.coords(obiectum)
    #print(CS)
    OC=[]#liste avec les Ã©lÃ©ments qui sont en contact avec l'objet
    OC.append(frame.find_overlapping(x1,y1,x1+4,y1+4))
    #print(OC)
    if any(2 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblin1)
        hit(x1,y1)
    if any(3 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblin2)
        hit(x1,y1)
    if any(4 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblin3)
        hit(x1,y1)
    if any(5 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblin4)
        hit(x1,y1)
    if any(6 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblin5)
        hit(x1,y1)
    if any(7 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblin6)
        hit(x1,y1)
    if any(8 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        golem(golem1)
        hit(x1,y1)
    if any(9 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        golem(golem2)
        hit(x1,y1)
    if any(10 in code for code in OC):
        print('we gonna do stuff')
        reset_bullet(obiectum)
        golem(golem3)
        hit(x1,y1)
    if any(11 in code for code in OC):
        reset_bullet(obiectum)
        skeleton(skeleton1)
        hit(x1,y1)
    if any(12 in code for code in OC):
        reset_bullet(obiectum)
        skeleton(skeleton2)
        hit(x1,y1)
    if any(13 in code for code in OC):
        reset_bullet(obiectum)
        skeleton(skeleton3)
        hit(x1,y1)
    if any(14 in code for code in OC):
        reset_bullet(obiectum)
        skeleton(skeleton4)
        hit(x1,y1)
    if any(15 in code for code in OC):
        reset_bullet(obiectum)
        skeleton(skeleton5)
        hit(x1,y1)
    if any(16 in code for code in OC):
        reset_bullet(obiectum)
        skeleton(skeleton6)
        hit(x1,y1)
    if any(17 in code for code in OC):
        reset_bullet(obiectum)
        skeleton(skeleton7)
        hit(x1,y1)
    if any(18 in code for code in OC):
        reset_bullet(obiectum)
        skeleton(skeleton8)
        hit(x1,y1)
    if any(19 in code for code in OC):
        reset_bullet(obiectum)
        skull(skull1)
        hit(x1,y1)
    if any(20 in code for code in OC):
        reset_bullet(obiectum)
        skull(skull2)
        hit(x1,y1)
    if any(21 in code for code in OC):
        reset_bullet(obiectum)
        skull(skull3)
        hit(x1,y1)
    if any(22 in code for code in OC):
        reset_bullet(obiectum)
        skull(skull4)
        hit(x1,y1)
        
def hit(x1,y1):
    global active_boom,boom
    boom=frame.create_image(x1+2,y1+2,image=boom_image)
    booms.append(boom)
    active_boom=1
       
def reset_mob(mob):
    """Arrete le mouvement du mob et le remet en attente pour une nouvelle spawn"""
    global active_gob1,active_gob2,active_gob3,active_gob4,active_gob5,active_gob6,active_gol1,active_gol2,active_gol3
    global active_skel1,active_skel2,active_skel3,active_skel4,active_skel5,active_skel6,active_skel7,active_skel8,active_skull1,active_skull2,active_skull3,active_skull4
    global gob1_health,gob2_health,gob3_health,gob4_health,gob5_health,gob6_health,gol1_health,gol2_health,gol3_health
    global skel1_health,skel2_health,skel3_health,skel4_health,skel5_health,skel6_health,skel7_health,skel8_health,skull1_health,skull2_health,skull3_health,skull4_health
    x,y=frame.coords(mob)
    if mob==goblin1:
        active_gob1=0
        gob1_health=1
        print("i need to stop")
    if mob==goblin2:
        active_gob2=0
        gob2_health=1
    if mob==goblin3:
        active_gob3=0
        gob3_health=1
    if mob==goblin4:
        active_gob4=0
        gob4_health=1
    if mob==goblin5:
        active_gob5=0
        gob5_health=1
    if mob==goblin6:
        active_gob6=0
        gob6_health=1
    if mob==golem1:
        active_gol1=0
        gol1_health=10
    if mob==golem2:
        active_gol2=0
        gol2_health=10
    if mob==golem3:
        active_gol3=0
        gol3_health=10
    if mob==skeleton1:
        active_skel1=0
        skel1_health=2
    if mob==skeleton2:
        active_skel2=0
        skel2_health=2
    if mob==skeleton3:
        active_skel3=0
        skel3_health=2
    if mob==skeleton4:
        active_skel4=0
        skel4_health=2
    if mob==skeleton5:
        active_skel5=0
        skel5_health=2
    if mob==skeleton6:
        active_skel6=0
        skel6_health=2
    if mob==skeleton7:
        active_skel7=0
        skel7_health=2
    if mob==skeleton8:
        active_skel8=0
        skel8_health=2
    if mob==skull1:
        active_skull1=0
        skull1_health=1
    if mob==skull2:
        active_skull2=0
        skull2_health=1
    if mob==skull3:
        active_skull3=0
        skull3_health=1
    if mob==skull4:
        active_skull4=0
        skull4_health=1
    
    if x<490:
        reset_x=-x-30
        frame.move(mob,reset_x,0)
    if x>545:
         reset_x=(1036-x)+30
         frame.move(mob,reset_x,0)

        
def tower():
    "regarde si il ya a eut contact avec la tour, si contact on remet le mob au point de départ et on perd des points de vie en accord"
    global tower_health
    OC=[]
    OC.append(frame.find_overlapping(490,70,545,250))
    if any(2 in code for code in OC):
        reset_mob(goblin1)
        tower_health=tower_health-1
        health()
    if any(3 in code for code in OC):
        reset_mob(goblin2)
        tower_health=tower_health-1
        health()
    if any(4 in code for code in OC):
        reset_mob(goblin3)
        tower_health=tower_health-1
        health()
    if any(5 in code for code in OC):
        reset_mob(goblin4)
        tower_health=tower_health-1
        health()
    if any(6 in code for code in OC):
        reset_mob(goblin5)
        tower_health=tower_health-1
        health()
    if any(7 in code for code in OC):
        reset_mob(goblin6)
        tower_health=tower_health-1
        health()
    if any(8 in code for code in OC):
        reset_mob(golem1)
        tower_health=tower_health-3
        health()
    if any(9 in code for code in OC):
        reset_mob(golem2)
        tower_health=tower_health-3
        health()
    if any(10 in code for code in OC):
        reset_mob(golem3)
        tower_health=tower_health-3
        health()
    if any(11 in code for code in OC):
        reset_mob(skeleton1)
        tower_health=tower_health-1
        health()
    if any(12 in code for code in OC):
        reset_mob(skeleton2)
        tower_health=tower_health-1
        health()
    if any(13 in code for code in OC):
        reset_mob(skeleton3)
        tower_health=tower_health-1
        health()
    if any(14 in code for code in OC):
        reset_mob(skeleton4)
        tower_health=tower_health-1
        health()
    if any(15 in code for code in OC):
        reset_mob(skeleton5)
        tower_health=tower_health-1
        health()
    if any(16 in code for code in OC):
        reset_mob(skeleton6)
        tower_health=tower_health-1
        health()
    if any(17 in code for code in OC):
        reset_mob(skeleton7)
        tower_health=tower_health-1
        health()
    if any(18 in code for code in OC):
        reset_mob(skeleton8)
        tower_health=tower_health-1
        health()
    if any(19 in code for code in OC):
        reset_mob(skull1)
        tower_health=tower_health-2
        health()
    if any(20 in code for code in OC):
        reset_mob(skull2)
        tower_health=tower_health-2
        health()
    if any(21 in code for code in OC):
        reset_mob(skull3)
        tower_health=tower_health-2
        health()
    if any(22 in code for code in OC):
        reset_mob(skull4)
        tower_health=tower_health-2
        health()
    
        
def health():
    global tower_health
    
    if tower_health==3:
        frame.move(heart4,0,500)

    if tower_health==2:
        frame.move(heart3,0,500)
        frame.move(heart4,0,500)

    if tower_health==1:
        frame.move(heart2,0,500)
        frame.move(heart3,0,500)
        frame.move(heart4,0,500)
        
    if tower_health <= 0:
        lost=frame.create_image(width1/2,height1/2,image=game_over)
        
def goblin(goblino):
    "s'occupe des PV de monstres de types goblin et les stop avec la fonction reset_mob"
    global gob1_health,gob2_health,gob3_health,gob4_health,gob5_health,gob6_health
    if goblino==goblin1:
        gob1_health=gob1_health-1
        if gob1_health==0:
            reset_mob(goblino)
    if goblino==goblin2:
        gob2_health=gob2_health-1
        if gob2_health==0:
            reset_mob(goblino)
    if goblino==goblin3:
        gob3_health=gob3_health-1
        if gob3_health==0:
            reset_mob(goblino)
    if goblino==goblin4:
        gob4_health=gob4_health-1
        if gob4_health==0:
            reset_mob(goblino)
    if goblino==goblin5:
        gob5_health=gob5_health-1
        if gob1_health==0:
            reset_mob(goblino)
    if goblino==goblin6:
        gob6_health=gob6_health-1
        if gob6_health==0:
            reset_mob(goblino)
            
def golem(golemo):
    "s'occupe des PV de monstres de types golems et les stop avec la fonction reset_mob"
    global gol1_health,gol2_health,gol3_health
    if golemo==golem1:
        gol1_health=gol1_health-1
        if gol1_health==0:
            reset_mob(golemo)
    if golemo==golem2:
        gol2_health=gol2_health-1
        if gol2_health==0:
            reset_mob(golemo)
    if golemo==golem3:
        gol3_health=gol3_health-1
        if gol3_health==0:
            reset_mob(golemo)

def skeleton(skeletono):
    global skel1_health,skel2_health,skel3_health,skel4_health,skel5_health,skel6_health,skel7_health,skel8_health
    if skeletono==skeleton1:
        skel1_health=skel1_health-1
        if skel1_health==0:
            reset_mob(skeletono)
    if skeletono==skeleton2:
        skel2_health=skel2_health-1
        if skel2_health==0:
            reset_mob(skeletono)
    if skeletono==skeleton3:
        skel3_health=skel3_health-1
        if skel3_health==0:
            reset_mob(skeletono)
    if skeletono==skeleton4:
        skel4_health=skel4_health-1
        if skel4_health==0:
            reset_mob(skeletono)
    if skeletono==skeleton5:
        skel5_health=skel5_health-1
        if skel5_health==0:
            reset_mob(skeletono)
    if skeletono==skeleton6:
        skel6_health=skel6_health-1
        if skel6_health==0:
            reset_mob(skeletono)
    if skeletono==skeleton7:
        skel7_health=skel7_health-1
        if skel7_health==0:
            reset_mob(skeletono)
    if skeletono==skeleton8:
        skel8_health=skel8_health-1
        if skel8_health==0:
            reset_mob(skeletono)

def skull(skullo):
    global skull1_health,skull2_health,skull3_health,skull4_health
    if skullo==skull1:
        skull1_health=skull1_health-1
        if skull1_health==0:
            reset_mob(skullo)
    if skullo==skull2:
        skull2_health=skull2_health-1
        if skull2_health==0:
            reset_mob(skullo)
    if skullo==skull3:
        skull3_health=skull3_health-1
        if skull3_health==0:
            reset_mob(skullo)
    if skullo==skull4:
        skull4_health=skull4_health-1
        if skull4_health==0:
            reset_mob(skullo)
    

def animation():
    global active_gob1,active_gob2,active_gob3,active_gob4,active_gob5,active_gob6,active_gol1,active_gol2,active_gol3
    global active_skel1,active_skel2,active_skel3,active_skel4,active_skel5,active_skel6,active_skel7,active_skel8,active_skull1,active_skull2,active_skull3,active_skull4
    global counter_skeleton1,counter_skeleton2,counter_skeleton3,counter_skeleton4,counter_skeleton5,counter_skeleton6,counter_skeleton7,counter_skeleton8,frame_skeleton1,frame_skeleton2,frame_skeleton3,frame_skeleton4,frame_skeleton5,frame_skeleton6,frame_skeleton7,frame_skeleton8,counter_skull1,counter_skull2,counter_skull3,counter_skull4,frame_skull1,frame_skull2,frame_skull3,frame_skull4
    global counter_golem1,frame_golem1,counter_golem2,frame_golem2,counter_golem3,frame_golem3,frame_goblin1,frame_golbin2,frame_golbin3,frame_golbin4,frame_golbin5,frame_golbin6
    global active_boom,frame_boom
    
    if active_gob1==1:
        frame_counter(goblin1)
        i=str(frame_goblin1)
        gob1_image.configure(format="gif -index "+i)
        frame.move(goblin1,3,0)
    if active_gob2==1:
        frame_counter(goblin2)
        i=str(frame_goblin2)
        gob1_image.configure(format="gif -index "+i)
        frame.move(goblin2,3,0)
    if active_gob3==1:
        frame_counter(goblin3)
        i=str(frame_goblin3)
        gob1_image.configure(format="gif -index "+i)
        frame.move(goblin3,3,0)
    if active_gob4==1:
        frame_counter(goblin4)
        i=str(frame_goblin4)
        gob1_image.configure(format="gif -index "+i)
        frame.move(goblin4,3,0)
    if active_gob5==1:
        frame_counter(goblin5)
        i=str(frame_goblin5)
        gob1_image.configure(format="gif -index "+i)
        frame.move(goblin5,3,0)
    if active_gob6==1:
        frame_counter(goblin6)
        i=str(frame_goblin6)
        gob1_image.configure(format="gif -index "+i)
        frame.move(goblin6,3,0)
    if active_gol1==1:
        frame_counter(golem1)
        i=str(frame_golem1)
        golem1_image.configure(format="gif -index "+i)
        if i=="0" or i=="4":
            frame.move(golem1,0.2,0)
        else:
            frame.move(golem1,0.5,0)
    if active_gol2==1:
        frame_counter(golem2)
        i=str(frame_golem2)
        golem1_image.configure(format="gif -index "+i)
        if i=="0" or i=="4":
            frame.move(golem2,0.2,0)
        else:
            frame.move(golem2,0.5,0)
    if active_gol3==1:
        frame_counter(golem3)
        i=str(frame_golem3)
        golem1_image.configure(format="gif -index "+i)
        if i=="0" or i=="4":
            frame.move(golem3,0.2,0)
        else:
            frame.move(golem3,0.5,0)
    if active_skel1==1:
        frame_counter(skeleton1)
        i=str(frame_skeleton1)
        skeleton1_image.configure(format="gif -index "+i)
        frame.move(skeleton1,-0.8,0)
    if active_skel2==1:
        frame_counter(skeleton2)
        i=str(frame_skeleton2)
        skeleton2_image.configure(format="gif -index "+i)
        frame.move(skeleton2,-0.8,0)
    if active_skel3==1:
        frame_counter(skeleton3)
        i=str(frame_skeleton3)
        skeleton3_image.configure(format="gif -index "+i)
        frame.move(skeleton3,-0.8,0)
    if active_skel4==1:
        frame_counter(skeleton4)
        i=str(frame_skeleton4)
        skeleton4_image.configure(format="gif -index "+i)
        frame.move(skeleton4,-0.8,0)
    if active_skel5==1:
        frame_counter(skeleton5)
        i=str(frame_skeleton5)
        skeleton1_image.configure(format="gif -index "+i)
        frame.move(skeleton5,-0.8,0)
    if active_skel6==1:
        frame_counter(skeleton6)
        i=str(frame_skeleton6)
        skeleton2_image.configure(format="gif -index "+i)
        frame.move(skeleton6,-0.8,0)
    if active_skel7==1:
        frame_counter(skeleton7)
        i=str(frame_skeleton7)
        skeleton3_image.configure(format="gif -index "+i)
        frame.move(skeleton7,-0.8,0)
    if active_skel8==1:
        frame_counter(skeleton8)
        i=str(frame_skeleton8)
        skeleton4_image.configure(format="gif -index "+i)
        frame.move(skeleton8,-0.8,0)
    
    if active_skull1==1:
        frame_counter(skull1)
        i=str(frame_skull1)
        skull1_image.configure(format="gif -index "+i)
        frame.move(skull1,-4,0)
    if active_skull2==1:
        frame_counter(skull2)
        i=str(frame_skull2)
        skull2_image.configure(format="gif -index "+i)
        frame.move(skull2,-5,0)
    if active_skull3==1:
        frame_counter(skull3)
        i=str(frame_skull3)
        skull1_image.configure(format="gif -index "+i)
        frame.move(skull3,-4,0)
    if active_skull4==1:
        frame_counter(skull4)
        i=str(frame_skull4)
        skull2_image.configure(format="gif -index "+i)
        frame.move(skull4,-5,0)
    if active_boom==1:
        frame_counter(boom1)
        if frame_boom==4:
            for boom in booms:
                frame.delete(boom)
            active_boom=0
            frame_boom=0
        else:
            i=str(frame_boom)
            boom_image.configure(format="gif -index "+i)
        
        
def frame_counter(mob):
    global counter_golem1,frame_golem1,counter_golem2,frame_golem2,counter_golem3,frame_golem3,frame_goblin1,frame_goblin2,frame_goblin3,frame_goblin4,frame_goblin5,frame_goblin6
    global counter_skeleton1,counter_skeleton2,counter_skeleton3,counter_skeleton4,counter_skeleton5,counter_skeleton6,counter_skeleton7,counter_skeleton8,frame_skeleton1,frame_skeleton2,frame_skeleton3,frame_skeleton4,frame_skeleton5,frame_skeleton6,frame_skeleton7,frame_skeleton8,counter_skull1,counter_skull2,counter_skull3,counter_skull4,frame_skull1,frame_skull2,frame_skull3,frame_skull4
    global active_boom,frame_boom

    if mob==goblin1:
        frame_goblin1=frame_goblin1+1
        if frame_goblin1==13:
            frame_goblin1=0
    if mob==goblin2:
        frame_goblin2=frame_goblin2+1
        if frame_goblin2==13:
            frame_goblin2=0
    if mob==goblin3:
        frame_goblin3=frame_goblin3+1
        if frame_goblin3==13:
            frame_goblin3=0
    if mob==goblin4:
        frame_goblin4=frame_goblin4+1
        if frame_goblin4==13:
            frame_goblin4=0
    if mob==goblin5:
        frame_goblin5=frame_goblin5+1
        if frame_goblin5==13:
            frame_goblin5=0
    if mob==goblin6:
        frame_goblin6=frame_goblin6+1
        if frame_goblin6==13:
            frame_goblin6=0
    
    if mob==golem1:
        counter_golem1+=1
        if counter_golem1==8:
            frame_golem1=frame_golem1+1
            counter_golem1=0
        if frame_golem1==9:
            frame_golem1=0

    if mob==golem2:
        counter_golem2+=1
        if counter_golem2==8:
            frame_golem2=frame_golem2+1
            counter_golem2=0
        if frame_golem2==9:
            frame_golem2=0

    if mob==golem3:
        counter_golem3+=1
        if counter_golem3==8:
            frame_golem3=frame_golem3+1
            counter_golem3=0
        if frame_golem3==9:
            frame_golem3=0

    if mob==skeleton1:
        counter_skeleton1+=1
        if counter_skeleton1==3:
            frame_skeleton1+=1
            counter_skeleton1=0
        if frame_skeleton1==7:
            frame_skeleton1=0
    if mob==skeleton2:
        counter_skeleton2+=1
        if counter_skeleton2==3:
            frame_skeleton2+=1
            counter_skeleton2=0
        if frame_skeleton2==7:
            frame_skeleton2=0
    if mob==skeleton3:
        counter_skeleton3+=1
        if counter_skeleton3==3:
            frame_skeleton3+=1
            counter_skeleton3=0
        if frame_skeleton3==7:
            frame_skeleton3=0
    if mob==skeleton4:
        counter_skeleton4+=1
        if counter_skeleton4==3:
            frame_skeleton4+=1
            counter_skeleton4=0
        if frame_skeleton4==7:
            frame_skeleton4=0
    if mob==skeleton5:
        counter_skeleton5+=1
        if counter_skeleton5==3:
            frame_skeleton5+=1
            counter_skeleton5=0
        if frame_skeleton5==7:
            frame_skeleton5=0
    if mob==skeleton6:
        counter_skeleton6+=1
        if counter_skeleton6==3:
            frame_skeleton6+=1
            counter_skeleton6=0
        if frame_skeleton6==7:
            frame_skeleton6=0
    if mob==skeleton7:
        counter_skeleton7+=1
        if counter_skeleton7==3:
            frame_skeleton7+=1
            counter_skeleton7=0
        if frame_skeleton7==7:
            frame_skeleton7=0
    if mob==skeleton8:
        counter_skeleton8+=1
        if counter_skeleton8==3:
            frame_skeleton8+=1
            counter_skeleton8=0
        if frame_skeleton8==7:
            frame_skeleton8=0
    
    if mob==skull1:
        counter_skull1+=1
        if counter_skull1==2:
            frame_skull1+=1
            counter_skull1=0
        if frame_skull1==9:
            frame_skull1=0
    if mob==skull2:
        counter_skull2+=1
        if counter_skull2==2:
            frame_skull2+=1
            counter_skull2=0
        if frame_skull2==9:
            frame_skull2=0
    if mob==skull3:
        counter_skull3+=1
        if counter_skull3==2:
            frame_skull3+=1
            counter_skull3=0
        if frame_skull3==9:
            frame_skull3=0
    if mob==skull4:
        counter_skull4+=1
        if counter_skull4==2:
            frame_skull4+=1
            counter_skull4=0
        if frame_skull4==9:
            frame_skull4=0

    if mob==boom1:
        frame_boom+=1
    

def level_1():
    global active_gob1,active_gob2,active_gob3,active_gob4,active_gob5,active_gob6,active_gol1,active_gol2,active_gol3
    global active_skel1,active_skel2,active_skel3,active_skel4,active_skel5,active_skel6,active_skel7,active_skel8,active_skull1,active_skull2,active_skull3,active_skull4
    global wave_1,wave_2,wave_3,wave_4,wave_5,timer

    if wave_1==1:
        
        timer=timer+1
        
        if timer==15:
            active_gob1=1
        if timer==45:
            active_gob2=1
        if timer==75:
            active_gol1=1

    if wave_2==1:

        timer=timer+1
        
        if timer==15:
            active_skel1=1
            
        if timer==115:
            active_skel2=1
            active_skull1=1
            
        if timer==165:
            active_skel3=1
            
        if timer==195:
            active_skel4=1
            
        if timer==225:
            active_skel5=1
            active_skull2=1
            
        if timer==265:
            active_skel6=1
            
        if timer==305:
            active_skel7=1
            active_skull3=1
            
        if timer==335:
            active_skel8=1
            
        if timer==505:
            active_skull4=1
        if timer==545:
            active_skull1=1
        if timer==585:
            active_skull3=1
        if timer==605:
            active_skull2=1
        if timer==665:
            active_skull4=1
            active_skel1=1
        if timer==705:
            active_skull1=1
            active_skel2=1
        if timer==745:
            active_skel3=1
        if timer==775:
            active_skel4=1
        if timer==805:
            active_skel5=1
        if timer==835:
            active_skel6=1
            active_skull2=1
        if timer==885:
            active_skull3=1
        if timer==905:
            active_skull4=1
        if timer==1105:
            active_skull1=1
            
frame_number=0
cycle_r_old=0
cycle_l_old=0
active_r1,active_r2,active_r3,active_r4,active_l1,active_l2,active_l3,active_l4=0,0,0,0,0,0,0,0
cycle_r=0
cycle_l=0 
playing=1

counter_golem1,frame_golem1,counter_golem2,frame_golem2,counter_golem3,frame_golem3,frame_goblin1,frame_goblin2,frame_goblin3,frame_goblin4,frame_goblin5,frame_goblin6=0,0,0,0,0,0,0,0,0,0,0,0
counter_skeleton1,counter_skeleton2,counter_skeleton3,counter_skeleton4,counter_skeleton5,counter_skeleton6,counter_skeleton7,counter_skeleton8,frame_skeleton1,frame_skeleton2,frame_skeleton3,frame_skeleton4,frame_skeleton5,frame_skeleton6,frame_skeleton7,frame_skeleton8,counter_skull1,counter_skull2,counter_skull3,counter_skull4,frame_skull1,frame_skull2,frame_skull3,frame_skull4=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
timer,wave_1,wave_2,wave_3,wave_4,wave_5=0,0,0,0,0,0
paused=0
vitesser_x=0
vitesser_y=0
vitessel_x=0
vitessel_y=0
tower_health=4
"Mob health and active stats"
gob1_health,gob2_health,gob3_health,gob4_health,gob5_health,gob6_health,=1,1,1,1,1,1
skel1_health,skel2_health,skel3_health,skel4_health,skel5_health,skel6_health,skel7_health,skel8_health=2,2,2,2,2,2,2,2
skull1_health,skull2_health,skull3_health,skull4_health=1,1,1,1
active_gob1,active_gob2,active_gob3,active_gob4,active_gob5,active_gob6,active_gol1,active_gol2,active_gol3=0,0,0,0,0,0,0,0,0
active_skel1,active_skel2,active_skel3,active_skel4,active_skel5,active_skel6,active_skel7,active_skel8,active_skull1,active_skull2,active_skull3,active_skull4=0,0,0,0,0,0,0,0,0,0,0,0
gol1_health,gol2_health,gol3_health,=10,10,10
active_boom=0
can_shoot=1
counter=0
frame_boom=0
boom1=0
booms=[]

try:
    root.resizable(width=False,height=False)
    while playing==1:
        if paused==0:

            level_1()
            animation()
            bullet(vitesser_x,vitesser_y,vitessel_x,vitessel_y)
            tower()    
            cannon_rotation()
            root.bind("<Button 1>",cannon_shoot_coords)
            frame.bind("<Button 1>",cycle)
            
            if can_shoot==0:
                counter+=1
                if counter==22:
                    can_shoot=1
                    counter=0
            

        
        frame.tag_bind(menu,"<Button 1>",menuclick)
        frame.tag_bind(exito,"<Button 1>",leave)
        frame.tag_bind(wave1,"<Button 1>",test1)
        frame.tag_bind(wave2,"<Button 1>",test2)
        root.bind("<Escape>",menuclick)
        frame.update()
        t.sleep(0.016666)

    
    root.mainloop()

        
except KeyboardInterrupt:
    root.destroy()
