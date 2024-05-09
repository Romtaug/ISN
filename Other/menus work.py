from tkinter import *
import time as t
import math as m
from PIL import Image

root=Tk()

ext=".png"
cannon_l=PhotoImage(file="cannon.png")
cannon_r=PhotoImage(file="cannon.png")
imageFile="menu-1.png"
menu_file="menu-1.png"
sky_file = "sky.png"
background_file = "NewBG.png"
gob1_file = "goblin1.gif"
gob2_file= "goblin2.gif"
bulletf=PhotoImage(file="bullet.png")
game_over=PhotoImage(file="menu-1.png")
menu_image=PhotoImage(file=menu_file)
sky = PhotoImage(file=sky_file)
background = PhotoImage(file=background_file)
golem1_image = PhotoImage(file="Golem.gif")
gob1_image=PhotoImage(file=gob1_file)
gob2_image=PhotoImage(file=gob1_file)
width1 = sky.width()
height1 = sky.height()
wave1_image=PhotoImage(file="wave1.png")
exit_image=PhotoImage(file="exit.png")

 
frame = Canvas(root,width=width1,height=height1-2)
frame.pack(expand=1)

layer0=frame.create_image(width1/2,height1/2,image=sky)

goblin1=frame.create_image(0,height1-55,image=gob1_image)

golem1=frame.create_image(0,height1-95,image=golem1_image)

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
    global active_gob1,active_gol1
    active_gol1=1
    active_gob1=1
    print("lol")

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

        global active_l2,cycle_l,cycle_l_old
        active_l2=0
        cycle_l_old=cycle_l
        cycle_l=0
        reset_x=490-xL2
        reset_y=70-yL2
        frame.move(bullet_l2,reset_x,reset_y)


    if xL3<0 or yL3>230 or yL3<0:

        global active_l3,cycle_l,cycle_l_old
        active_l3=0
        cycle_l_old=cycle_l
        cycle_l=0
        reset_x=490-xL3
        reset_y=70-yL3
        frame.move(bullet_l3,reset_x,reset_y)


    if xL4<0 or yL4>230 or yL4<0:

        global active_l4,cycle_l,cycle_l_old
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

        global active_r2,cycle_r,cycle_r_old
        active_r2=0
        cycle_r_old=cycle_r
        cycle_r=0
        reset_x=545-xR2
        reset_y=70-yR2
        frame.move(bullet_r2,reset_x,reset_y)


    if xR3>1036 or yR3>230 or yR3<0:

        global active_r3,cycle_r,cycle_r_old
        active_r3=0
        cycle_r_old=cycle_r
        cycle_r=0
        reset_x=545-xR3
        reset_y=70-yR3
        frame.move(bullet_r3,reset_x,reset_y)

    if xR4>1036 or yR4>230 or yR4<0:

        global active_r4,cycle_r,cycle_r_old
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
    #CS=[]#liste avec les coordonnÃ©es de l'object 
    #CS.append(frame.coords(obiectum))
    x1,y1=frame.coords(obiectum)
    #print(CS)
    OC=[]#liste avec les Ã©lÃ©ments qui sont en contact avec l'objet
    OC.append(frame.find_overlapping(x1,y1,x1+8,y1+8))
    #print(OC)
    if any(2 in code for code in OC):
        print('he ded')
        reset_bullet(obiectum)
        goblin(goblin1)
       
    if any(3 in code for code in OC):
        print('we gonna do stuff')
        reset_bullet(obiectum)
        golem(golem1)
        
def reset_mob(mob):
    """Arrete le mouvement du mob et le remet en attente pour une nouvelle spawn"""
    global active_gob1,gob1_health,active_gol1,gol1_health
    if mob==goblin1:
        active_gob1=0
        gob1_health=1
        print("i need to stop")
    if mob==golem1:
        active_gol1=0
        gol1_health=10
        
    x,y=frame.coords(mob)
    if x<490:
                reset_x=-x
                frame.move(mob,reset_x,0)
    if x>545:
                reset_x=x+(1036-x)
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
        reset_mob(golem1)
        tower_health=tower_health-3

    
    if tower_health <= 0:
        lost=frame.create_image(width1/2,height1/2,image=game_over)
        
def goblin(goblino):
    "s'occupe des PV de monstres de types goblin et les stop"
    global gob1_health
    if goblino==goblin1:
        gob1_health=gob1_health-1
        if gob1_health==0:
            reset_mob(goblino)
            
def golem(golemo):
    "s'occupe des PV de monstres de types golems et les stop avec la fonction reset_mob"
    global gol1_health
    if golemo==golem1:
        gol1_health=gol1_health-1
        if gol1_health==0:
            reset_mob(golemo)
            
def animation():
    global active_gob1,active_gol1
    global frame_golem1,counter_golem1,frame_goblin1,frame_goblin2

    if active_gol1==1:
        frame_counter(golem1)
        i=str(frame_golem1)
        golem1_image.configure(format="gif -index "+i)
        if i=="0" or i=="4":
            frame.move(golem1,0.2,0)
        else:
            frame.move(golem1,0.5,0)
            
    if active_gob1==1:
        frame_counter(goblin1)
        i=str(frame_goblin1)
        gob1_image.configure(format="gif -index "+i)
        frame.move(goblin1,3,0)

def frame_counter(mob):
    global counter_golem1,frame_golem1,frame_goblin1,frame_golbin2
    
    if mob==golem1:
        counter_golem1+=1
        if counter_golem1==8:
            frame_golem1=frame_golem1+1
            counter_golem1=0
        if frame_golem1==9:
            frame_golem1=0

    if mob==goblin1:
        frame_goblin1=frame_goblin1+1
        if frame_goblin1==13:
            frame_goblin1=0
        
    

cycle_r_old=0
cycle_l_old=0
active_r1,active_r2,active_r3,active_r4,active_l1,active_l2,active_l3,active_l4=0,0,0,0,0,0,0,0
cycle_r=0
cycle_l=0 
playing=1

counter_golem1=0
frame_golem1=0
frame_goblin1=0
frame_goblin2=0

paused=0
vitesser_x=0
vitesser_y=0
vitessel_x=0
vitessel_y=0
tower_health=1
"Mob health and active stats"
gob1_health=1
active_gob1=0
gol1_health=10
active_gol1=0

try:
    root.resizable(width=False,height=False)
    while playing==1:
        if paused==0:
            
            animation()
            bullet(vitesser_x,vitesser_y,vitessel_x,vitessel_y)
            tower()    
            cannon_rotation()
            root.bind("<Button 1>",cannon_shoot_coords)
            frame.bind("<Button 1>",cycle)

        
        frame.tag_bind(menu,"<Button 1>",menuclick)
        frame.tag_bind(exito,"<Button 1>",leave)
        frame.tag_bind(wave1,"<Button 1>",test)
        root.bind("<Escape>",menuclick)
        frame.update()
        t.sleep(0.016666)

    
    root.mainloop()

        
except KeyboardInterrupt:
    root.destroy()
