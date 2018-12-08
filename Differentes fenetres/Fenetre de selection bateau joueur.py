from tkinter import *
####
####
##  DEFINITION DE LA FENETRE DE SELECTION DES BATEAUX DU JOUEUR 
####
####
Mafenetre = Tk()
Mafenetre.title('Sélection des bateaux !')

def Clic(event):
    
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    
    if X < 75:
        if Y<50:
            couleur(75,50)
            installer='a1'
        elif Y>50 and Y<100:
            couleur(75,100)
        elif Y>100 and Y<150:
            couleur(75,150)
        elif Y>150 and Y<200:
            couleur(75,200)
        elif Y>200 and Y<250:
            couleur(75,250)
        elif Y>250 and Y<300:
            couleur(75,300)
        elif Y>300 and Y<350:   
            couleur(75,350)
        elif Y>350 and Y<400:
            couleur(75,400)
        elif Y>400 and Y<450:
            couleur(75,450)
        else:
            couleur(75,500)
    elif X>75 and X<150:
        if Y<50:
            couleur(150,50)
        elif Y>50 and Y<100:
            couleur(150,100)
        elif Y>100 and Y<150:
            couleur(150,150)
        elif Y>150 and Y<200:
            couleur(150,200)
        elif Y>200 and Y<250:
            couleur(150,250)
        elif Y>250 and Y<300:
            couleur(150,300)
        elif Y>300 and Y<350:   
            couleur(150,350)
        elif Y>350 and Y<400:
            couleur(150,400)
        elif Y>400 and Y<450:
            couleur(150,450)
        else:
            couleur(150,500)
    elif X>150 and X<225:
        if Y<50:
            couleur(225,50)
        elif Y>50 and Y<100:
            couleur(225,100)
        elif Y>100 and Y<150:
            couleur(225,150)
        elif Y>150 and Y<200:
            couleur(225,200)
        elif Y>200 and Y<250:
            couleur(225,250)
        elif Y>250 and Y<300:
            couleur(225,300)
        elif Y>300 and Y<350:   
            couleur(225,350)
        elif Y>350 and Y<400:
            couleur(225,400)
        elif Y>400 and Y<450:
            couleur(225,450)
        else:
            couleur(225,500)
    elif X>225 and X<300:
        if Y<50:
            couleur(300,50)
        elif Y>50 and Y<100:
            couleur(300,100)
        elif Y>100 and Y<150:
            couleur(300,150)
        elif Y>150 and Y<200:
            couleur(300,200)
        elif Y>200 and Y<250:
            couleur(300,250)
        elif Y>250 and Y<300:
            couleur(300,300)
        elif Y>300 and Y<350:   
            couleur(300,350)
        elif Y>350 and Y<400:
            couleur(300,400)
        elif Y>400 and Y<450:
            couleur(300,450)
        else:
            couleur(300,500)
    elif X>300 and X<375:
        if Y<50:
            couleur(375,50)
        elif Y>50 and Y<100:
            couleur(375,100)
        elif Y>100 and Y<150:
            couleur(375,150)
        elif Y>150 and Y<200:
            couleur(375,200)
        elif Y>200 and Y<250:
            couleur(375,250)
        elif Y>250 and Y<300:
            couleur(375,300)
        elif Y>300 and Y<350:   
            couleur(375,350)
        elif Y>350 and Y<400:
            couleur(375,400)
        elif Y>400 and Y<450:
            couleur(375,450)
        else:
            couleur(375,500)
    elif X>375 and X<450:
        if Y<50:
            couleur(450,50)
        elif Y>50 and Y<100:
            couleur(450,100)
        elif Y>100 and Y<150:
            couleur(450,150)
        elif Y>150 and Y<200:
            couleur(450,200)
        elif Y>200 and Y<250:
            couleur(450,250)
        elif Y>250 and Y<300:
            couleur(450,300)
        elif Y>300 and Y<350:   
            couleur(450,350)
        elif Y>350 and Y<400:
            couleur(450,400)
        elif Y>400 and Y<450:
            couleur(450,450)
        else:
            couleur(450,500)
    elif X>450 and X<525:
        if Y<50:
            couleur(525,50)
        elif Y>50 and Y<100:
            couleur(525,100)
        elif Y>100 and Y<150:
            couleur(525,150)
        elif Y>150 and Y<200:
            couleur(525,200)
        elif Y>200 and Y<250:
            couleur(525,250)
        elif Y>250 and Y<300:
            couleur(525,300)
        elif Y>300 and Y<350:   
            couleur(525,350)
        elif Y>350 and Y<400:
            couleur(525,400)
        elif Y>400 and Y<450:
            couleur(525,450)
        else:
            couleur(525,500)
    elif X>525 and X<600:
        if Y<50:
            couleur(600,50)
        elif Y>50 and Y<100:
            couleur(600,100)
        elif Y>100 and Y<150:
            couleur(600,150)
        elif Y>150 and Y<200:
            couleur(600,200)
        elif Y>200 and Y<250:
            couleur(600,250)
        elif Y>250 and Y<300:
            couleur(600,300)
        elif Y>300 and Y<350:   
            couleur(600,350)
        elif Y>350 and Y<400:
            couleur(600,400)
        elif Y>400 and Y<450:
            couleur(600,450)
        else:
            couleur(600,500)
    elif X>600 and X<675:
        if Y<50:
            couleur(675,50)
        elif Y>50 and Y<100:
            couleur(675,100)
        elif Y>100 and Y<150:
            couleur(675,150)
        elif Y>150 and Y<200:
            couleur(675,200)
        elif Y>200 and Y<250:
            couleur(675,250)
        elif Y>250 and Y<300:
            couleur(675,300)
        elif Y>300 and Y<350:   
            couleur(675,350)
        elif Y>350 and Y<400:
            couleur(675,400)
        elif Y>400 and Y<450:
            couleur(675,450)
        else:
            couleur(675,500)
    else :
        if Y<50:
            couleur(750,50)
        elif Y>50 and Y<100:
            couleur(750,100)
        elif Y>100 and Y<150:
            couleur(750,150)
        elif Y>150 and Y<200:
            couleur(750,200)
        elif Y>200 and Y<250:
            couleur(750,250)
        elif Y>250 and Y<300:
            couleur(750,300)
        elif Y>300 and Y<350:   
            couleur(750,350)
        elif Y>350 and Y<400:
            couleur(750,400)
        elif Y>400 and Y<450:
            couleur(750,450)
        else:
            couleur(750,500)
def couleur(x1,y1):
    Canevas1.create_line(x1-75,y1-25,x1,y1-25   ,fill="black", width=50)
  

## Interface
Largeur = 750
Hauteur = 500
Canevas1 = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ="lightblue")
Canevas1.bind("<Button-1>", Clic)
Canevas1.pack(padx =5, pady =5)
Canevas1.create_line(0,3,750,3,fill="black",width=4)
Canevas1.create_line(0,50,750,50,fill="black",width=4)
Canevas1.create_line(0,100,750,100,fill="black",width=4)
Canevas1.create_line(0,150,750,150,fill="black",width=4)
Canevas1.create_line(0,200,750,200,fill="black",width=4)
Canevas1.create_line(0,250,750,250,fill="black",width=4)
Canevas1.create_line(0,300,750,300,fill="black",width=4)
Canevas1.create_line(0,350,750,350,fill="black",width=4)
Canevas1.create_line(0,400,750,400,fill="black",width=4)
Canevas1.create_line(0,450,750,450,fill="black",width=4)
Canevas1.create_line(0,500,750,500,fill="black",width=4)

Canevas1.create_line(3,500,300,-100000,fill="black",width=4)
Canevas1.create_line(75,500,300,-100000,fill="black",width=4)
Canevas1.create_line(150,500,300,-100000,fill="black",width=4)
Canevas1.create_line(225,500,300,-100000,fill="black",width=4)
Canevas1.create_line(300,500,300,-100000,fill="black",width=4)
Canevas1.create_line(375,500,300,-100000,fill="black",width=4)
Canevas1.create_line(450,500,300,-100000,fill="black",width=4)
Canevas1.create_line(525,500,300,-100000,fill="black",width=4)
Canevas1.create_line(600,500,300,-100000,fill="black",width=4)
Canevas1.create_line(675,500,300,-100000,fill="black",width=4)
Canevas1.create_line(750,500,300,-100000,fill="black",width=4)


# Création d'un widget Button (bouton Quitter)
Bouton1 = Button(Mafenetre, text = 'Quitter', command = Mafenetre.destroy)
Bouton1.pack()

# Lancement du gestionnaire d'événements
Mafenetre.mainloop() 