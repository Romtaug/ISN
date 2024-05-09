# --------------------------------------------------------#
#               ISN Baccalauréat 2019 - Lycée Vernant     #
#                            Fantatosy                    #
# --------------------------------------------------------#

# Importation des librairies
from tkinter import *
import time as t
import math as m
import winsound
from PIL import Image

winsound.PlaySound("pont_levis.wav", winsound.SND_FILENAME)
root=Tk()
cannon_l=PhotoImage(file="cannon.png")
cannon_r=PhotoImage(file="cannon.png")
bulletf=PhotoImage(file="bullet.png")
game_over=PhotoImage(file="GAMEOVER.png")
menu_image=PhotoImage(file="menu-1.png")
sky = PhotoImage(file="sky.png")
background = PhotoImage(file="NewBG.png")
#Bonhommes
golem1_image = PhotoImage(file="Golem.gif")
golem2_image = PhotoImage(file="Golem.gif")
gob1_image = PhotoImage(file="goblin1.gif")
gob1d_image = PhotoImage(file="goblin1.gif")
gob2_image = PhotoImage(file="goblin2.gif")
gob2d_image = PhotoImage(file="goblin2.gif")
eye1_image = PhotoImage(file="NewPiskel.gif")
eye2_image = PhotoImage(file="NewPiskel.gif")
# Chevaliers Romain
chev1_image=PhotoImage(file="chevalierbig1.gif")
chev2_image=PhotoImage(file="chevalierbig2.gif")
spider1_image=PhotoImage(file="spider.gif")
spider2_image=PhotoImage(file="spider.gif")

skeleton1_image=PhotoImage(file="skeleton.gif")
skeleton2_image=PhotoImage(file="skeleton.gif")


width1 = sky.width()
height1 = sky.height()
wave1_image=PhotoImage(file="wave1.png")
exit_image=PhotoImage(file="exit.png")
 
frame = Canvas(root,width=width1,height=height1)
frame.pack(expand=1)

layer0=frame.create_image(width1/2,height1/2,image=sky)

"""On cree les mobs pour le controle des niveaux plus tard"""

goblin1=frame.create_image(0,height1-55,image=gob1_image) 
goblin2=frame.create_image(0,height1-55,image=gob1_image) 
goblin3=frame.create_image(0,height1-55,image=gob1_image)

goblin1d=frame.create_image(1000,height1-55,image=gob1d_image) 
goblin2d=frame.create_image(1000,height1-55,image=gob1d_image) 
goblin3d=frame.create_image(1000,height1-55,image=gob1d_image)
#
goblino1=frame.create_image(0,height1-55,image=gob2_image) 
goblino2=frame.create_image(0,height1-55,image=gob2_image) 
goblino3=frame.create_image(0,height1-55,image=gob2_image)

goblino1d=frame.create_image(1000,height1-55,image=gob2d_image) 
goblino2d=frame.create_image(1000,height1-55,image=gob2d_image) 
goblino3d=frame.create_image(1000,height1-55,image=gob2d_image)
#
golem1=frame.create_image(0,height1-95,image=golem1_image)
golem2=frame.create_image(0,height1-95,image=golem1_image)
golem3=frame.create_image(0,height1-95,image=golem1_image)

golem1d=frame.create_image(1000,height1-95,image=golem2_image)
golem2d=frame.create_image(1000,height1-95,image=golem2_image)
golem3d=frame.create_image(1000,height1-95,image=golem2_image)
#
eye1=frame.create_image(0,height1-55,image=eye1_image)
eye2=frame.create_image(0,height1-55,image=eye1_image)
eye3=frame.create_image(0,height1-55,image=eye1_image)

eye1d=frame.create_image(1000,height1-55,image=eye2_image)
eye2d=frame.create_image(1000,height1-55,image=eye2_image)
eye3d=frame.create_image(1000,height1-55,image=eye2_image)
#
chev1=frame.create_image(0,height1-55,image=chev1_image)
chev2=frame.create_image(0,height1-55,image=chev1_image)
chev3=frame.create_image(0,height1-55,image=chev1_image)

chev1d=frame.create_image(1000,height1-55,image=chev2_image)
chev2d=frame.create_image(1000,height1-55,image=chev2_image)
chev3d=frame.create_image(1000,height1-55,image=chev2_image)
#
chev1=frame.create_image(0,height1-55,image=chev1_image)
chev2=frame.create_image(0,height1-55,image=chev1_image)
chev3=frame.create_image(0,height1-55,image=chev1_image)

chev1d=frame.create_image(1000,height1-55,image=chev2_image)
chev2d=frame.create_image(1000,height1-55,image=chev2_image)
chev3d=frame.create_image(1000,height1-55,image=chev2_image)
#
spider1=frame.create_image(0,height1-55,image=spider1_image)
spider2=frame.create_image(0,height1-55,image=spider1_image)
spider3=frame.create_image(0,height1-55,image=spider1_image)

spider1d=frame.create_image(1000,height1-55,image=spider2_image)
spider2d=frame.create_image(1000,height1-55,image=spider2_image)
spider3d=frame.create_image(1000,height1-55,image=spider2_image)
#
skeleton1=frame.create_image(0,height1-55,image=skeleton1_image)
skeleton2=frame.create_image(0,height1-55,image=skeleton1_image)
skeleton3=frame.create_image(0,height1-55,image=skeleton1_image)

skeleton1d=frame.create_image(1000,height1-55,image=skeleton2_image)
skeleton2d=frame.create_image(1000,height1-55,image=skeleton2_image)
skeleton3d=frame.create_image(1000,height1-55,image=skeleton2_image)
#
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

hp=frame.create_rectangle(480,45,560,50,fill="red")

cannon_right=frame.create_image(545,70, image=cannon_r)

cannon_left=frame.create_image(490,70, image=cannon_l)

wave1=frame.create_image(456,-29,image=wave1_image)
exito=frame.create_image(380,-29,image=exit_image)

# Fonctions

def cannon_shoot_coords(event):
    vitesse=3000
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
        
def leave(event):
    root.destroy()

def test(event):
    global wave_1

    wave_1=1
    

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

        global active_l1,cycle_l,cycle_l_old
        active_l1=0
        cycle_l_old=cycle_l
        cycle_l=0
        reset_x=490-xL1
        reset_y=70-yL1
        frame.move(bullet_l1,reset_x,reset_y)


    if xL2<0 or yL2>230 or yL2<0:

        global active_l2
        active_l2=0
        cycle_l_old=cycle_l
        cycle_l=0
        reset_x=490-xL2
        reset_y=70-yL2
        frame.move(bullet_l2,reset_x,reset_y)


    if xL3<0 or yL3>230 or yL3<0:

        global active_l3
        active_l3=0
        cycle_l_old=cycle_l
        cycle_l=0
        reset_x=490-xL3
        reset_y=70-yL3
        frame.move(bullet_l3,reset_x,reset_y)


    if xL4<0 or yL4>230 or yL4<0:

        global active_l4
        active_l4=0
        cycle_l_old=cycle_l
        cycle_l=0
        reset_x=490-xL4
        reset_y=70-yL4
        frame.move(bullet_l4,reset_x,reset_y)


    if xR1>1036 or yR1>230 or yR1<0:

        global active_r1,cycle_r,cycle_r_old
        active_r1=0
        cycle_r_old=cycle_r
        cycle_r=0
        reset_x=545-xR1
        reset_y=70-yR1
        frame.move(bullet_r1,reset_x,reset_y)


    if xR2>1036 or yR2>230 or yR2<0:

        global active_r2
        active_r2=0
        cycle_r_old=cycle_r
        cycle_r=0
        reset_x=545-xR2
        reset_y=70-yR2
        frame.move(bullet_r2,reset_x,reset_y)


    if xR3>1036 or yR3>230 or yR3<0:

        global active_r3
        cycle_r_old=cycle_r
        cycle_r=0
        reset_x=545-xR3
        reset_y=70-yR3
        frame.move(bullet_r3,reset_x,reset_y)

    if xR4>1036 or yR4>230 or yR4<0:

        global active_r4
        active_r4=0
        cycle_r_old=cycle_r
        cycle_r=0
        reset_x=545-xR4
        reset_y=70-yR4
        frame.move(bullet_r4,reset_x,reset_y)

    
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

    
    else:
        cycle_r=cycle_r
        cycle_l=cycle_l


def hitboxes(obiectum):
    #CS=[]#liste avec les coordonnees de l'object 
    #CS.append(frame.coords(obiectum))
    x1,y1=frame.coords(obiectum)
    #print(CS)
    OC=[]#liste avec les elements qui sont en contact avec l'objet
    OC.append(frame.find_overlapping(x1,y1,x1+8,y1+8))
    #print(OC)
    if any(2 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblin1)
    if any(3 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblin2)
    if any(4 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblin3)
    if any(5 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblin1d)
    if any(6 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblin2d)
    if any(7 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblin3d)
        
    if any(8 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblino1)
    if any(9 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblino2)
    if any(10 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblino3)
    if any(11 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblino1d)
    if any(12 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblino2d)
    if any(13 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblino3d)

    if any(14 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(eye1)
    if any(15 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(eye2)
    if any(16 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(eye3)
    if any(17 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(eye1d)
    if any(18 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(eye2d)
    if any(19 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(eye3d)

    if any(20 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(chevalier1)
    if any(21 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(chevalier2)
    if any(22 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(chevalier3)
    if any(23 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(chevalier1d)
    if any(24 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(chevalier2d)
    if any(25 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(chevalier3d)

    if any(26 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(spider1)
    if any(27 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(spider2)
    if any(28 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(spider3)
    if any(29 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(spider1d)
    if any(30 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(spider2d)
    if any(31 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(spider3d)

    if any(32 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(skeleton1)
    if any(33 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(skeleton2)
    if any(34 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(skeleton3)
    if any(35 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(skeleton1d)
    if any(36 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(skeleton2d)
    if any(37 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        other(skeleton3d)
        
    if any(38 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        golem(golem1)
    if any(39 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        golem(golem2)
    if any(41 in code for code in OC):
        print('we gonna do stuff')
        reset_bullet(obiectum)
        golem(golem3)
    if any(42 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        golem(golem1d)
    if any(43 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        golem(golem2d)
    if any(44 in code for code in OC):
        print('we gonna do stuff')
        reset_bullet(obiectum)
        golem(golem3d)



#vie boule

def reset_mob(mob):
    """Arrete le mouvement du mob et le remet en attente pour une nouvelle spawn"""
    global active_gob1,active_gob2,active_gob3,active_gob1d,active_gob2d,active_gob3d,active_gol1,active_gol2,active_gol3,active_gol1d,active_gol2d,active_gol3d,active_go1,active_go2,active_go3,active_go1d,active_go2d,active_go3d,active_eye1,active_eye2,active_eye3,active_eye1d,active_eye2d,active_eye3d,active_chev1,active_chev2,active_chev3,active_chev1d,active_chev2d,active_chev3d,active_spi1,active_spi2,active_spi3,active_spi1d,active_spi2d,active_spi3d,active_ske1,active_ske2,active_ske3,active_ske1d,active_ske2d,active_ske3d
    global gob1_health,gob2_health,gob3_health,gob1d_health,gob2d_health,gob3d_health,gol1_health,gol2_health,gol3_health,gol1d_health,gol2d_health,gol3_health,go1_health,go2_health,go3_health,go1d_health,go2d_health,go3d_health,eye1_health,eye2_health,eye3_health,eye1d_health,eye2d_health,eye3d_health,chev1_health,chev2_health,chev3_health,chev1d_health,chev2d_health,chev3d_health,spi1_health,spi2_health,spi3_health,spi1d_health,active_spi2d_health,spi3d_health,ske1_health,ske2_health,ske3_health,ske1d_health,active_ske2d_health,ske3d_health

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
    if mob==goblin1d:
        active_gob1d=0
        gob1d_health=1
        print("i need to stop")
    if mob==goblin2d:
        active_gob2d=0
        gob2d_health=1
    if mob==goblin3d:
        active_gob3d=0
        gob3d_health=1
        
    if mob==goblino1:
        active_go1=0
        go1_health=1
        print("i need to stop")
    if mob==goblino2:
        active_go2=0
        go2_health=1
    if mob==goblino3:
        active_go3=0
        go3_health=1
    if mob==goblino1d:
        active_go1d=0
        go1d_health=1
        print("i need to stop")
    if mob==goblino2d:
        active_go2d=0
        go2d_health=1
    if mob==goblino3d:
        active_go3d=0
        go3d_health=1
        
    if mob==eye1:
        active_eye1=0
        eye1_health=1
        print("i need to stop")
    if mob==eye2:
        active_eye2=0
        eye2_health=1
    if mob==eye3:
        active_eye3=0
        eye3_health=1
    if mob==eye1d:
        active_eye1d=0
        eye1d_health=1
        print("i need to stop")
    if mob==eye2d:
        active_eye2d=0
        eye2d_health=1
    if mob==eye3d:
        active_eye3d=0
        eye3d_health=1

    if mob==chev1:
        active_chev1=0
        chev1_health=1
        print("i need to stop")
    if mob==chev2:
        active_chev2=0
        chev2_health=1
    if mob==chev3:
        active_chev3=0
        chev3_health=1
    if mob==chev1d:
        active_chev1d=0
        chev1d_health=1
        print("i need to stop")
    if mob==chev2d:
        active_chev2d=0
        chev2d_health=1
    if mob==chev3d:
        active_chev3d=0
        chev3d_health=1

    if mob==spider1:
        active_spi1=0
        spi1_health=1
        print("i need to stop")
    if mob==spider2:
        active_spi2=0
        spi2_health=1
    if mob==spider3:
        active_spi3=0
        spi3_health=1
    if mob==spider1d:
        active_spi1d=0
        spi1d_health=1
        print("i need to stop")
    if mob==spider2d:
        active_spi2d=0
        spi2d_health=1
    if mob==spider3d:
        active_spi3d=0
        spi3d_health=1

    if mob==skeleton1:
        active_ske1=0
        ske1_health=1
        print("i need to stop")
    if mob==skeleton2:
        active_ske2=0
        ske2_health=1
    if mob==skeleton3:
        active_ske3=0
        ske3_health=1
    if mob==skeleton1d:
        active_ske1d=0
        ske1d_health=1
        print("i need to stop")
    if mob==skeleton2d:
        active_ske2d=0
        ske2d_health=1
    if mob==skeleton3d:
        active_ske3d=0
        ske3d_health=1
        
    if mob==golem1:
        active_gol1=0
        gol1_health=10
    if mob==golem2:
        active_gol2=0
        gol2_health=10
    if mob==golem3:
        active_gol3=0
        gol3_health=10
    if mob==golem1d:
        active_gol1d=0
        gol1d_health=10
    if mob==golem2d:
        active_gol2d=0
        gol2d_health=10
    if mob==golem3d:
        active_gol3d=0
        gol3d_health=10
        
    if x<490:
        reset_x=-x-30
        frame.move(mob,reset_x,0)
    if x>545:
         reset_x=x+(1036-x)+30
         frame.move(mob,reset_x,0)

        
def tower():
    "regarde si il ya a eut contact avec la tour, si contact on remet le mob au point de départ et on perd des points de vie en accord"
    global tower_health
    OC=[]
    OC.append(frame.find_overlapping(490,70,545,250))
    if any(2 in code for code in OC):
        reset_mob(goblin1)
        tower_health=tower_health-1
    if any(3 in code for code in OC):
        reset_mob(goblin2)
        tower_health=tower_health-1
    if any(4 in code for code in OC):
        reset_mob(goblin3)
        tower_health=tower_health-1
    if any(5 in code for code in OC):
        reset_mob(goblin1d)
        tower_health=tower_health-1
    if any(6 in code for code in OC):
        reset_mob(goblin2d)
        tower_health=tower_health-1
    if any(7 in code for code in OC):
        reset_mob(goblin3d)
        tower_health=tower_health-1
        tower_health=tower_health-1
        
    if any(8 in code for code in OC):
        reset_mob(goblino1)
        tower_health=tower_health-1
    if any(9 in code for code in OC):
        reset_mob(goblino2)
        tower_health=tower_health-1
    if any(10 in code for code in OC):
        reset_mob(goblino3)
        tower_health=tower_health-1
    if any(11 in code for code in OC):
        reset_mob(goblino1d)
        tower_health=tower_health-1
    if any(12 in code for code in OC):
        reset_mob(goblino2d)
        tower_health=tower_health-1
    if any(13 in code for code in OC):
        reset_mob(goblino3d)
        tower_health=tower_health-1
        tower_health=tower_health-1
        
        
    if any(14 in code for code in OC):
        reset_mob(golem1)
        tower_health=tower_health-3
    if any(15 in code for code in OC):
        reset_mob(golem2)
        tower_health=tower_health-3
    if any(16 in code for code in OC):
        reset_mob(golem3)
        tower_health=tower_health-3
    if any(17 in code for code in OC):
        reset_mob(golem1d)
        tower_health=tower_health-3
    if any(18 in code for code in OC):
        reset_mob(golem2d)
        tower_health=tower_health-3
    if any(19 in code for code in OC):
        reset_mob(golem3d)
        tower_health=tower_health-3
        
    if any(20 in code for code in OC):
        reset_mob(eye1)
        tower_health=tower_health-1
    if any(21 in code for code in OC):
        reset_mob(eye2)
        tower_health=tower_health-1
    if any(22 in code for code in OC):
        reset_mob(eye3)
        tower_health=tower_health-1
    if any(23 in code for code in OC):
        reset_mob(eye1d)
        tower_health=tower_health-1
    if any(24 in code for code in OC):
        reset_mob(eye2d)
        tower_health=tower_health-1
    if any(25 in code for code in OC):
        reset_mob(eye3d)
        tower_health=tower_health-1
        tower_health=tower_health-1

    if any(26 in code for code in OC):
        reset_mob(chev1)
        tower_health=tower_health-1
    if any(27 in code for code in OC):
        reset_mob(chev2)
        tower_health=tower_health-1
    if any(28 in code for code in OC):
        reset_mob(chev3)
        tower_health=tower_health-1
    if any(29 in code for code in OC):
        reset_mob(chev1d)
        tower_health=tower_health-1
    if any(30 in code for code in OC):
        reset_mob(chev2d)
        tower_health=tower_health-1
    if any(31 in code for code in OC):
        reset_mob(chev3d)
        tower_health=tower_health-1
        tower_health=tower_health-1
        
    if any(32 in code for code in OC):
        reset_mob(spider1)
        tower_health=tower_health-1
    if any(33 in code for code in OC):
        reset_mob(spider2)
        tower_health=tower_health-1
    if any(34 in code for code in OC):
        reset_mob(spider3)
        tower_health=tower_health-1
    if any(35 in code for code in OC):
        reset_mob(spider1d)
        tower_health=tower_health-1
    if any(36 in code for code in OC):
        reset_mob(spider2d)
        tower_health=tower_health-1
    if any(37 in code for code in OC):
        reset_mob(spider3d)
        tower_health=tower_health-1
        tower_health=tower_health-1

    if any(38 in code for code in OC):
        reset_mob(skeleton1)
        tower_health=tower_health-1
    if any(39 in code for code in OC):
        reset_mob(skeleton2)
        tower_health=tower_health-1
    if any(40 in code for code in OC):
        reset_mob(skeleton3)
        tower_health=tower_health-1
    if any(41 in code for code in OC):
        reset_mob(skeleton1d)
        tower_health=tower_health-1
    if any(42 in code for code in OC):
        reset_mob(sskeleton2d)
        tower_health=tower_health-1
    if any(43 in code for code in OC):
        reset_mob(skeleton3d)
        tower_health=tower_health-1
        tower_health=tower_health-1
     
        
    if tower_health <= 0:
        lost=frame.create_image(width1/2,height1/2,image=game_over)
        
def goblin(goblino):
    "s'occupe des PV de monstres de types goblin et les stop avec la fonction reset_mob"
    global gob1_health,gob2_health,gob3_health,gob1d_health,gob2d_health,gob3d_health,go1_health,go2_health,go3_health,go1d_health,go2d_health,go3d_health,eye1_health,eye2_health,eye3_health,eye1d_health,eye2d_health,eye3d_health
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
    if goblino==goblin1d:
        gob1d_health=gob1d_health-1
        if gob1d_health==0:
            reset_mob(goblino)
    if goblino==goblin2d:
        gob2d_health=gob2d_health-1
        if gob1_health==0:
            reset_mob(goblino)
    if goblino==goblin3d:
        gob3d_health=gob3d_health-1
        if gob3d_health==0:
            reset_mob(goblino)

    if goblino==goblino1:
        go1_health=go1_health-1
        if go1_health==0:
            reset_mob(goblino)
    if goblino==goblino2:
        go2_health=go2_health-1
        if go2_health==0:
            reset_mob(goblino)
    if goblino==goblino3:
        go3_health=go3_health-1
        if gob3_health==0:
            reset_mob(goblino)
    if goblino==goblino1d:
        go1d_health=go1d_health-1
        if gob1d_health==0:
            reset_mob(goblino)
    if goblino==goblino2d:
        go2d_health=go2d_health-1
        if gob2d_health==0:
            reset_mob(goblino)
    if goblino==goblino3d:
        go3d_health=go3d_health-1
        if go3d_health==0:
            reset_mob(goblino)

    if goblino==eye1:
        eye1_health=eye1_health-1
        if go1_health==0:
            reset_mob(goblino)
    if goblino==eye2:
        eye2_health=eye2_health-1
        if eye2_health==0:
            reset_mob(goblino)
    if goblino==eye3:
        eye3_health=eye3_health-1
        if eye3_health==0:
            reset_mob(goblino)
    if goblino==eye1d:
        eye1d_health=eye1d_health-1
        if eye1d_health==0:
            reset_mob(goblino)
    if goblino==eye2d:
        eye2d_health=eye2d_health-1
        if eye1_health==0:
            reset_mob(goblino)
    if goblino==eye3d:
        eye3d_health=eye3d_health-1
        if eye3d_health==0:
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
    if golemo==golem1d:
        gol1_health=gol1_health-1
        if gold1_health==0:
            reset_mob(golemo)
    if golemo==golem2d:
        gol2d_health=gol2d_health-1
        if gol2d_health==0:
            reset_mob(golemo)
    if golemo==golem3d:
        gol3d_health=gol3d_health-1
        if gol3_health==0:
            reset_mob(golemo)

def other(othero):
    "s'occupe des PV de monstres de types golems et les stop avec la fonction reset_mob"
    global chev1_health,chev2_health,chev3_health,chev1d_health,chev2d_health,chev3d_health,spi1_health,spi2_health,spi3_health,spi1d_health,active_spi2d_health,spi3d_health,ske1_health,ske2_health,ske3_health,ske1d_health,active_ske2d_health,ske3d_health


    if othero==chevalier1:
        chev1_health=chev1_health-1
        if chev1_health==0:
            reset_mob(othero)
    if othero==chevalier2:
        chev2_health=chev2_health-1
        if chev2_health==0:
            reset_mob(othero)
    if othero==chevalier3:
        chev3_health=chev3_health-1
        if chev3_health==0:
            reset_mob(othero)
    if othero==golem1d:
        chev1_health=chev1_health-1
        if chev1d_health==0:
            reset_mob(othero)
    if othero==chevalier2d:
        chev2d_health=chev2d_health-1
        if chev2d_health==0:
            reset_mob(othero)
    if othero==chevalier3d:
        chev3d_health=chev3d_health-1
        if chev3_health==0:
            reset_mob(othero)

    if othero==spider1:
        spi1_health=spi1_health-1
        if spi1_health==0:
            reset_mob(othero)
    if othero==spider2:
        spi2_health=spi2_health-1
        if spi2_health==0:
            reset_mob(othero)
    if othero==spider3:
        spi3_health=spi3_health-1
        if spi3_health==0:
            reset_mob(othero)
    if othero==spider1d:
        spi1_health=spi1_health-1
        if spi1d_health==0:
            reset_mob(othero)
    if othero==spider2d:
        spi2d_health=spi2d_health-1
        if spi2d_health==0:
            reset_mob(othero)
    if othero==spider3d:
        spi3d_health=spi3d_health-1
        if spi3_health==0:
            reset_mob(othero)

    if othero==skeleton1:
        ske1_health=ske1_health-1
        if ske1_health==0:
            reset_mob(othero)
    if othero==skeleton2:
        ske2_health=ske2_health-1
        if ske2_health==0:
            reset_mob(othero)
    if othero==skeleton3:
        ske3_health=ske3_health-1
        if ske3_health==0:
            reset_mob(othero)
    if othero==skeleton1d:
        ske1_health=ske1_health-1
        if ske1d_health==0:
            reset_mob(othero)
    if othero==skeleton2d:
        ske2d_health=ske2d_health-1
        if ske2d_health==0:
            reset_mob(othero)
    if othero==skeleton3d:
        ske3d_health=ske3d_health-1
        if ske3_health==0:
            reset_mob(othero)
            

            
def animation():
    global active_gob1,active_gob2,active_gob3,active_gob1d,active_gob2d,active_gob3d,active_gol1,active_gol2,active_gol3,active_gol1d,active_gol2d,active_gol3d,active_go1,active_go2,active_go3,active_go1d,active_go2d,active_go3d,active_eye1,active_eye2,active_eye3,active_eye1d,active_eye2d,active_eye3d,active_chev1,active_chev2,active_chev3,active_chev1d,active_chev2d,active_chev3d,active_spi1,active_spi2,active_spi3,active_spi1d,active_spi2d,active_spi3d,active_ske1,active_ske2,active_ske3,active_ske1d,active_ske2d,active_ske3d
    global counter_gobin1,counter_gobin2,counter_gobin3,counter_gobin1d,counter_gobin2d,counter_gobin3d,counter_golem1,counter_golem2,counter_golem3,counter_golem1d,counter_golem2d,counter_golem3d,counter_goblino1,counter_goblino2,counter_goblino3,counter_goblino1d,counter_goblino2d,counter_goblino3d,counter_eye1,counter_eye2,counter_eye3,counter_eye1d,counter_eye2d,counter_eye3d,counter_chevalier1,counter_chevalier2,counter_chevalier3,counter_chevalier1d,counter_chevalier2d,counter_chevalier3d,counter_spider1,counter_spider2,counter_spider3,counter_spider1d,counter_spider2d,counter_spider3,counter_spider1,counter_spider2,counter_spider3,counter_spider1d,counter_spider2d,counter_spi3d,counter_skeleton1,counter_skeleton2,counter_skeleton3,counter_skeleton1d,counter_skeleton2d,counter_skeleton3d

    if active_gob1==1:
        frame_counter(goblin1)
        i=str(frame_goblino1)
        gob1_image.configure(format="gif -index "+i)
        frame.move(goblin1,3,0)
    if active_gob2==1:
        frame_counter(goblin2)
        i=str(frame_goblino2)
        gob1_image.configure(format="gif -index "+i)
        print("yeet")
        frame.move(goblin2,3,0)
    if active_gob3==1:
        frame_counter(goblin3)
        i=str(frame_goblino3)
        gob1_image.configure(format="gif -index "+i)
        frame.move(goblin3,3,0)
        
    if active_gob1d==1:
        frame_counter(goblin1d)
        i=str(frame_goblino1d)
        gob1d_image.configure(format="gif -index "+i)
        frame.move(goblin1d,-3,0)
    if active_gob2d==1:
        frame_counter(goblin2d)
        i=str(frame_goblino2d)
        gob1_image.configure(format="gif -index "+i)
        print("yeet")
        frame.move(goblin2d,-3,0)
    if active_gob3d==1:
        frame_counter(goblin3d)
        i=str(frame_goblino3d)
        gob1_image.configure(format="gif -index "+i)
        frame.move(goblin3d,-3,0)


    if active_go1==1:
        frame_counter(goblino1)
        i=str(frame_goblino1)
        gob1_image.configure(format="gif -index "+i)
        frame.move(goblino1,3,0)
    if active_go2==1:
        frame_counter(goblino2)
        i=str(frame_goblino2)
        gob1_image.configure(format="gif -index "+i)
        frame.move(goblino2,3,0)
    if active_go3==1:
        frame_counter(goblino3)
        i=str(frame_goblino3)
        gob1_image.configure(format="gif -index "+i)
        frame.move(goblino3,3,0)
    if active_go1d==1:
        frame_counter(goblino1d)
        i=str(frame_goblino1d)
        gob2_image.configure(format="gif -index "+i)
        frame.move(goblino2,-3,0)
    if active_go2d==1:
        frame_counter(goblino2d)
        i=str(frame_goblino2d)
        gob2_image.configure(format="gif -index "+i)
        frame.move(goblino2d,-3,0)
    if active_go3d==1:
        frame_counter(goblino3d)
        i=str(frame_goblino3d)
        gob2_image.configure(format="gif -index "+i)
        frame.move(goblino3,-3,0)
    
    
    if active_eye1==1:
        frame_counter(eye1)
        i=str(frame_eye1)
        eye1_image.configure(format="gif -index "+i)
        frame.move(eye1,3,0)
    if active_eye2==1:
        frame_counter(eye2)
        i=str(frame_eye2)
        eye1_image.configure(format="gif -index "+i)
        frame.move(eye2,3,0)
    if active_eye3==1:
        frame_counter(eye3)
        i=str(frame_eye3)
        eye1_image.configure(format="gif -index "+i)
        frame.move(eye3,3,0)
    if active_eye1d==1:
        frame_counter(eye1d)
        i=str(frame_eye1d)
        eye2_image.configure(format="gif -index "+i)
        frame.move(eye2,-3,0)
    if active_eye2d==1:
        frame_counter(eye2d)
        i=str(frame_eye2d)
        eye2_image.configure(format="gif -index "+i)
        frame.move(eye2d,-3,0)
    if active_eye3d==1:
        frame_counter(eye3d)
        i=str(frame_eye3d)
        eye2_image.configure(format="gif -index "+i)
        frame.move(eye3,-3,0)

    if active_spider1==1:
        frame_counter(spider1)
        i=str(frame_spider1)
        spider1_image.configure(format="gif -index "+i)
        frame.move(spider1,3,0)
    if active_spider2==1:
        frame_counter(spider2)
        i=str(frame_spider2)
        spider1_image.configure(format="gif -index "+i)
        frame.move(spider2,3,0)
    if active_spider3==1:
        frame_counter(spider3)
        i=str(frame_spider3)
        spider1_image.configure(format="gif -index "+i)
        frame.move(spider3,3,0)
    if active_spider1d==1:
        frame_counter(spider1d)
        i=str(frame_spider1d)
        spider2_image.configure(format="gif -index "+i)
        frame.move(spider2,-3,0)
    if active_spider2d==1:
        frame_counter(spider2d)
        i=str(frame_spider2d)
        spider2_image.configure(format="gif -index "+i)
        frame.move(spider2d,-3,0)
    if active_spider3d==1:
        frame_counter(spider3d)
        i=str(frame_spider3d)
        spider2_image.configure(format="gif -index "+i)
        frame.move(spider3,-3,0)

    if active_ske1==1:
        frame_counter(skeleton1)
        i=str(frame_skeleton1)
        skeleton1_image.configure(format="gif -index "+i)
        frame.move(skeleton1,3,0)
    if active_ske2==1:
        frame_counter(skeleton2)
        i=str(frame_skeleton2)
        skeleton1_image.configure(format="gif -index "+i)
        frame.move(skeleton2,3,0)
    if active_ske3==1:
        frame_counter(skeleton3)
        i=str(frame_skeleton3)
        skeleton1_image.configure(format="gif -index "+i)
        frame.move(skeleton3,3,0)
    if active_ske1d==1:
        frame_counter(skeleton1d)
        i=str(frame_skeleton1d)
        skeleton2_image.configure(format="gif -index "+i)
        frame.move(skeleton2,-3,0)
    if active_ske2d==1:
        frame_counter(skeleton2d)
        i=str(frame_skeleton2d)
        skeleton2_image.configure(format="gif -index "+i)
        frame.move(skeleton2d,-3,0)
    if active_ske3d==1:
        frame_counter(skeleton3d)
        i=str(frame_skeleton3d)
        skeleton2_image.configure(format="gif -index "+i)
        frame.move(skeleton3,-3,0)



        
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

    if active_gol1d==1:
        frame_counter(golem1d)
        i=str(frame_golem1d)
        golem1_image.configure(format="gif -index "+i)
        if i=="0" or i=="4":
            frame.move(golem1d,-0.2,0)
        else:
            frame.move(golem1d,-0.5,0)
    if active_gol2d==1:
        frame_counter(golem2d)
        i=str(frame_golem2d)
        golem1_image.configure(format="gif -index "+i)
        if i=="0" or i=="4":
            frame.move(golem2d,-0.2,0)
        else:
            frame.move(golem2d,-0.5,0)
    if active_gol3d==1:
        frame_counter(golem3d)
        i=str(frame_golem3d)
        golem1_image.configure(format="gif -index "+i)
        if i=="0" or i=="4":
            frame.move(golem3d,-0.2,0)
        else:
            frame.move(golem3d,-0.5,0)

    


    

def frame_counter(mob):
    global counter_gobin1,counter_gobin2,counter_gobin3,counter_gobin1d,counter_gobin2d,counter_gobin3d,counter_golem1,counter_golem2,counter_golem3,counter_golem1d,counter_golem2d,counter_golem3d,counter_goblino1,counter_goblino2,counter_goblino3,counter_goblino1d,counter_goblino2d,counter_goblino3d,counter_eye1,counter_eye2,counter_eye3,counter_eye1d,counter_eye2d,counter_eye3d,counter_chevalier1,counter_chevalier2,counter_chevalier3,counter_chevalier1d,counter_chevalier2d,counter_chevalier3d,counter_spider1,counter_spider2,counter_spider3,counter_spider1d,counter_spider2d,counter_spider3,counter_spider1,counter_spider2,counter_spider3,counter_spider1d,counter_spider2d,counter_spi3d,counter_skeleton1,counter_skeleton2,counter_skeleton3,counter_skeleton1d,counter_skeleton2d,counter_skeleton3d,frame_gobin1,frame_gobin2,frame_gobin3,frame_gobin1d,frame_gobin2d,frame_gobin3d,frame_golem1,frame_golem2,frame_golem3,frame_golem1d,frame_golem2d,frame_golem3d,frame_goblino1,frame_goblino2,frame_goblino3,frame_goblino1d,frame_goblino2d,frame_goblino3d,frame_eye1,frame_eye2,frame_eye3,frame_eye1d,frame_eye2d,frame_eye3d,frame_chevalier1,frame_chevalier2,frame_chevalier3,frame_chevalier1d,frame_chevalier2d,frame_chevalier3d,frame_spider1,frame_spider2,frame_spider3,frame_spider1d,frame_spider2d,frame_spider3,counter_spider1,frame_spider2,frame_spider3,frame_spider1d,frame_spider2d,frame_spider3d,frame_skeleton1,frame_skeleton2,frame_skeleton3,frame_skeleton1d,frame_skeleton2d,frame_skeleton3d,frame_number
    if mob==goblin1:
        frame_goblino1=frame_goblino1+1
        if frame_goblino1==13:
            frame_goblino1=0
    if mob==goblin2:
        frame_goblino2=frame_goblino2+1
        if frame_goblino2==13:
            frame_goblino2=0
    if mob==goblin3:
        frame_goblino3=frame_goblino3+1
        if frame_goblino3==13:
            frame_goblino3=0
    if mob==goblin1d:
        frame_goblino1d=frame_goblino1d+1
        if frame_goblino1d==13:
            frame_goblino1d=0
    if mob==goblin2d:
        frame_goblino2d=frame_goblino2d+1
        if frame_goblino2d==13:
            frame_goblino2d=0
    if mob==goblin3d:
        frame_goblino3d=frame_goblino3d+1
        if frame_goblino3d==13:
            frame_goblino3d=0
            
    if mob==goblino1:
        frame_goblino1=frame_goblino1+1
        if frame_goblino1==13:
            frame_goblino1=0
    if mob==goblino2:
        frame_goblino2=frame_goblino2+1
        if frame_goblino2==13:
            frame_goblino2=0
    if mob==goblino3:
        frame_goblino3=frame_goblino3+1
        if frame_goblino3==13:
            frame_goblino3=0
    if mob==goblino1d:
        frame_goblino1d=frame_goblino1d+1
        if frame_goblino1d==13:
            frame_goblino1d=0
    if mob==goblino2d:
        frame_goblino2d=frame_goblino2d+1
        if frame_goblino2d==13:
            frame_goblino2d=0
    if mob==goblino3d:
        frame_goblino3d=frame_goblino3d+1
        if frame_goblino3d==13:
            frame_goblino3d=0

    
    if mob==eye1:
        frame_eye1=frame_eye1+1
        if frame_eye1==13:
            frame_eye1=0
    if mob==eye2:
        frame_eye2=frame_eye2+1
        if frame_eye2==13:
            frame_eye2=0
    if mob==eye3:
        frame_eye3=frame_eye3+1
        if frame_eye3==13:
            frame_eye3=0
    if mob==eye1d:
        frame_eye1d=frame_eye1d+1
        if frame_eye1d==13:
            frame_eye1d=0
    if mob==eye2d:
        frame_eye2d=frame_eye2d+1
        if frame_eye2d==13:
            frame_eye2d=0
    if mob==eye3d:
        frame_eye3d=frame_eye3d+1
        if frame_eye3d==13:
            frame_eye3d=0

    if mob==spider1:
        frame_spider1=frame_spider1+1
        if frame_spider1==13:
            frame_spider1=0
    if mob==spider2:
        frame_spider2=frame_spider2+1
        if frame_spider2==13:
            frame_spider2=0
    if mob==spider3:
        frame_spider3=frame_spider3+1
        if frame_spider3==13:
            frame_spider3=0
    if mob==spider1d:
        frame_spider1d=frame_spider1d+1
        if frame_spider1d==13:
            frame_spider1d=0
    if mob==spider2d:
        frame_spider2d=frame_spider2d+1
        if frame_spider2d==13:
            frame_spider2d=0
    if mob==spider3d:
        frame_spider3d=frame_spider3d+1
        if frame_spider3d==13:
            frame_spider3d=0

    if mob==skeleton1:
        frame_skeleton1=frame_eye1+1
        if frame_skeleton1==13:
            frame_skeleton1=0
    if mob==skeleton2:
        frame_skeleton2=frame_skeleton2+1
        if frame_skeleton2==13:
            frame_skeleton2=0
    if mob==skeleton3:
        frame_skeleton3=frame_skeleton3+1
        if frame_skeleton3==13:
            frame_skeleton3=0
    if mob==skeleton1d:
        frame_skeleton1d=frame_skeleton1d+1
        if frame_skeleton1d==13:
            frame_skeleton1d=0
    if mob==skeleton2d:
        frame_skeleton2d=frame_skeleton2d+1
        if frame_skeleton2d==13:
            frame_skeleton2d=0
    if mob==skeleton3d:
        frame_skeleton3d=frame_skeleton3d+1
        if frame_skeleton3d==13:
            frame_skeleton3d=0

    if mob==skeleton1:
        frame_skeleton1=frame_eye1+1
        if frame_skeleton1==13:
            frame_skeleton1=0
    if mob==skeleton2:
        frame_skeleton2=frame_skeleton2+1
        if frame_skeleton2==13:
            frame_skeleton2=0
    if mob==skeleton3:
        frame_skeleton3=frame_skeleton3+1
        if frame_skeleton3==13:
            frame_skeleton3=0
    if mob==skeleton1d:
        frame_skeleton1d=frame_skeleton1d+1
        if frame_skeleton1d==13:
            frame_skeleton1d=0
    if mob==skeleton2d:
        frame_skeleton2d=frame_skeleton2d+1
        if frame_skeleton2d==13:
            frame_skeleton2d=0
    if mob==skeleton3d:
        frame_skeleton3d=frame_skeleton3d+1
        if frame_skeleton3d==13:
            frame_skeleton3d=0

    if mob==chev1:
        frame_skeleton1=frame_chev1+1
        if frame_chev1==5:
            frame_chev1=0
    if mob==chev2:
        frame_chev2=framechev2+1
        if frame_chev2==5:
            frame_chev2=0
    if mob==chev3:
        frame_chev3=frame_chev3+1
        if frame_chev3==5:
            frame_chev3=0
    if mob==chev1d:
        frame_chev1d=frame_skeleton1d+1
        if frame_chev1d==5:
            frame_chev1d=0
    if mob==chev2d:
        frame_chev2d=frame_skeleton2d+1
        if frame_chev2d==5:
            frame_chev2d=0
    if mob==chev3d:
        frame_chev3d=frame_chev3d+1
        if frame_chev3d==5:
            frame_chev3d=0

            
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
            

def level_1():
    global active_gob1,active_gob2,active_gob3,active_gob1d,active_gob2d,active_gob3d,active_gol1,active_gol2,active_gol3,active_gol1d,active_gol2d,active_gol3d,active_go1,active_go2,active_go3,active_go1d,active_go2d,active_go3d,active_eye1,active_eye2,active_eye3,active_eye1d,active_eye2d,active_eye3d,active_chev1,active_chev2,active_chev3,active_chev1d,active_chev2d,active_chev3d,active_spider1,active_spider2,active_spider3,active_spider1d,active_spider2d,active_spider3d,active_ske1,active_ske2,active_ske3,active_ske1d,active_ske2d,active_ske3d
    global wave_1,wave_2,wave_3,wave_4,wave_5,timer

    if wave_1==1:
        
        timer=timer+1
        
        if timer==15:
            active_eye1=1
            active_eye1d=1
        if timer==45:
            active_eye2=1
            active_eye2d=1
        if timer==75:
            active_eye3=1
            active_eye3d=1

        if timer==15:
            active_go1=1
            active_go1d=1
        if timer==45:
            active_go2=1
            active_go2d=1
        if timer==75:
            active_go3=1
            active_go3d=1

        if timer==15:
            active_gob1=1
            active_gob1d=1
        if timer==45:
            active_gob2=1
            active_gob2d=1
        if timer==75:
            active_gob3=1
            active_gob3d=1

        if timer==15:
            active_spider1=1
            active_spider1d=1
        if timer==45:
            active_spider2=1
            active_spider2d=1
        if timer==75:
            active_spider3=1
            active_spider3d=1

        
        if timer==15:
            active_chev1=1
            active_chev1d=1
        if timer==45:
            active_chev2=1
            active_chev2d=1
        if timer==75:
            active_chev3=1
            active_chev3d=1

        if timer==15:
            active_ske1=1
            active_ske1d=1
        if timer==45:
            active_ske2=1
            active_ske2d=1
        if timer==75:
            active_ske3=1
            active_ske3d=1

        if timer==15:
            active_gol1=1
            active_gol1d=1
        if timer==45:
            active_gol2=1
            active_ske2d=1
        if timer==75:
            active_gol3=1
            active_gol3d=1
            
       
    
frame_number=0
cycle_r_old=0
cycle_l_old=0
active_r1,active_r2,active_r3,active_r4,active_l1,active_l2,active_l3,active_l4=0,0,0,0,0,0,0,0
cycle_r=0
cycle_l=0 
playing=1

counter_gobin1,counter_gobin2,counter_gobin3,counter_gobin1d,counter_gobin2d,counter_gobin3d,counter_golem1,counter_golem2,counter_golem3,counter_golem1d,counter_golem2d,counter_golem3d,counter_goblino1,counter_goblino2,counter_goblino3,counter_goblino1d,counter_goblino2d,counter_goblino3d,counter_eye1,counter_eye2,counter_eye3,counter_eye1d,counter_eye2d,counter_eye3d,counter_chevalier1,counter_chevalier2,counter_chevalier3,counter_chevalier1d,counter_chevalier2d,counter_chevalier3d,counter_spider1,counter_spider2,counter_spider3,counter_spider1d,counter_spider2d,counter_spider3,counter_spider1,counter_spider2,counter_spider3,counter_spider1d,counter_spider2d,counter_spi3d,counter_skeleton1,counter_skeleton2,counter_skeleton3,counter_skeleton1d,counter_skeleton2d,counter_skeleton3dframe_gobin1,frame_gobin2,frame_gobin3,frame_gobin1d,frame_gobin2d,frame_gobin3d,frame_golem1,frame_golem2,frame_golem3,frame_golem1d,frame_golem2d,frame_golem3d,frame_goblino1,frame_goblino2,frame_goblino3,frame_goblino1d,frame_goblino2d,frame_goblino3d,frame_eye1,frame_eye2,frame_eye3,frame_eye1d,frame_eye2d,frame_eye3d,frame_chevalier1,frame_chevalier2,frame_chevalier3,frame_chevalier1d,frame_chevalier2d,frame_chevalier3d,frame_spider1,frame_spider2,frame_spider3,frame_spider1d,frame_spider2d,frame_spider3,counter_spider1,frame_spider2,frame_spider3,frame_spider1d,frame_spider2d,frame_spider3d,frame_skeleton1,frame_skeleton2,frame_skeleton3,frame_skeleton1d,frame_skeleton2d,frame_skeleton3d,frame_number=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

timer,wave_1,wave_2,wave_3,wave_4,wave_5=0,0,0,0,0,0
paused=0
vitesser_x=0
vitesser_y=0
vitessel_x=0
vitessel_y=0
tower_health=1
"Mob health and active stats"
gob1_health,gob2_health,gob3_health,gob1d_health,gob2d_health,gob3d_health,go2_health,go3_health,go1d_health,go2d_health,go3d_health,eye1_health,eye2_health,eye3_health,eye1d_health,eye2d_health,eye3d_health,chev1_health,chev2_health,chev3_health,chev1d_health,chev2d_health,chev3d_health,spi1_health,spi2_health,spi3_health,spi1d_health,active_spi2d_health,spi3d_health,ske1_health,ske2_health,ske3_health,ske1d_health,active_ske2d_health,ske3d_health=1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
active_gob1,active_gob2,active_gob3,active_gob1d,active_gob2d,active_gob3d,active_gol1,active_gol2,active_gol3,active_gol1d,active_gol2d,active_gol3d,active_go1,active_go2,active_go3,active_go1d,active_go2d,active_go3d,active_eye1,active_eye2,active_eye3,active_eye1d,active_eye2d,active_eye3d,active_chev1,active_chev2,active_chev3,active_chev1d,active_chev2d,active_chev3d,active_spider1,active_spider2,active_spider3,active_spider1d,active_spider2d,active_spider3d,active_ske1,active_ske2,active_ske3,active_ske1d,active_ske2d,active_ske3d=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
gol1_health,gol2_health,gol3_health,gol1d_health,gol2d_health,gol3_health,go1_health,=10,10,10,10,10,10,10


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

        
        frame.tag_bind(menu,"<Button 1>",menuclick)
        frame.tag_bind(exito,"<Button 1>",leave)
        frame.tag_bind(wave1,"<Button 1>",test)
        gol1_health,gol2_health,gol3_health,gol1d_health,gol2d_health,gol3_health,go1_health,=10,10,10,10,10,10,10
        root.bind("<Escape>",menuclick)
        frame.update()
        t.sleep(0.016666)

    
    root.mainloop()

        
except KeyboardInterrupt:
    root.destroy()
