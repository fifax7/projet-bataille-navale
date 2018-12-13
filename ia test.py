# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 17:39:08 2018

@author: 235489
"""
bat11=[]
bat12=[]
bat13=[]
bat14=[]
bat15=[]
bat16=[]
bat21=[]
bat22=[]
bat23=[]
bat24=[]
bat25=[]
bat26=[]
P = [['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10'],
     ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10'],
     ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10'],
     ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10'],
     ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10'],
     ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10'],
     ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'g10'],
     ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10'],
     ['i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9', 'i10'],
     ['j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'j8', 'j9', 'j10']]

installer=[]
direction=[]

def placezbateau(P):
    aleatoirebateau(P,5)
    aleatoirebateau(P,4)
    aleatoirebateau(P,4)
    aleatoirebateau(P,3)
    aleatoirebateau(P,3)
    aleatoirebateau(P,3)
    
def aleatoirebateau(P,bateau2):
    import random
    k=1
    l=1
    direction=[]
    while l==1:
        j=0
        lignebat= random.randint(0,9)
        colonnebat= random.randint(0,9)
        if installer.count(P[lignebat][colonnebat])==1:
            j='erreur'
        if j!='erreur':
            if 0+bateau2<=lignebat:
                k=0
                ligne=lignebat
                for i in range (1,bateau2):
                    lignes=ligne-1
                    if installer.count(P[lignes][colonnebat])==1:
                        k='erreur'
                if k!='erreur':
                    direction.append('gauche')
                    l=2
                    
            if 10-bateau2>=lignebat:
                k=0
                ligne=lignebat
                for i in range (1,bateau2):
                    lignes=ligne+1
                    if installer.count(P[lignes][colonnebat])==1:
                        k='erreur'
                if k!='erreur':
                    direction.append('droite')
                    
            if 0+bateau2<=colonnebat:
                k=0
                colonne=colonnebat
                for i in range (1,bateau2):
                    colonnes=colonne-1
                    if installer.count(P[lignebat][colonnes])==1:
                        k='erreur'
                if k!='erreur':
                    direction.append('haut')
                    l=2
            if 10-bateau2>=colonnebat:
                k=0
                colonne=colonnebat
                for i in range (1,bateau2):
                    colonnes=colonne+1
                    if installer.count(P[lignebat][colonnes])==1:
                        k='erreur'
                if k!='erreur':
                    direction.append('bas')
                    l=2

    import random
        
    n= random.choice(direction)
    print(n)
    if n=='gauche':
        ligne=lignebat
        for i in range (0,bateau2):
            lignes=ligne-i
            print(lignes)
            installer.append(P[lignes][colonnebat])
            
    if n=='droite':
        ligne=lignebat
        for i in range (0,bateau2):
            lignes=ligne+i
            print(lignes)
            installer.append(P[lignes][colonnebat])
            
    if n=='haut':
        colonne=colonnebat
        for i in range (0,bateau2):
            colonnes=colonne-i
            installer.append(P[lignebat][colonnes])
            
    if n=='bas':
        colonne=colonnebat
        for i in range (0,bateau2):
            colonnes=colonne+i
            installer.append(P[lignebat][colonnes])
            
   
def positionbateaujoueur(installer,a):
    if a==1:
        bat11.append(installer[0:5])
        bat12.append(installer[5:9])
        bat13.append(installer[9:13])
        bat14.append(installer[13:16])
        bat15.append(installer[16:19])
        bat16.append(installer[19:22])
        installer=[]
    if a==2:
        bat21.append(installer[0:5])
        bat22.append(installer[5:9])
        bat23.append(installer[9:13])
        bat24.append(installer[13:16])
        bat25.append(installer[16:19])
        bat26.append(installer[19:22])
        installer=[]

placezbateau(P)
positionbateaujoueur(installer,1)
placezbateau(P)
positionbateaujoueur(installer,2)
print(bat11,bat12,bat13,bat14,bat15,bat16,bat21,bat22,bat23,bat24,bat25,bat26)

bateau11 = 5
bateau12 = 4
bateau13 = 4
bateau14 = 3
bateau15 = 3
bateau16 = 3
bateau21 = 5
bateau22 = 4
bateau23 = 4
bateau24 = 3
bateau25 = 3
bateau26 = 3
import random
player2= random.choice(P)
if player2 in bat11:
        bateau11 = bateau11 - 1
        if bateau11 == 0:
            print('ton bateau1 a été coulé')
elif player2 in bat12:
        bateau12 = bateau12 - 1
        if bateau12 == 0:
            print('ton bateau2 a été coulé')
elif player2 in bat13:
        bateau13 = bateau13 - 1
        if bateau13 == 0:
            print('ton bateau3 a été coulé')
elif player2 in bat14:
        bateau14 = bateau14 - 1
        if bateau14 == 0:
            print('ton bateau4 a été coulé')
elif player2 in bat15:
        bateau15 = bateau15 - 1
        if bateau15 == 0:
            print('ton bateau5 a été coulé')
elif player2 in bat16:
        bateau16 = bateau16 - 1
        if bateau16 == 0:
            print('ton bateau6 a été coulé')
elif bat11 == 0 and bat12 == 0 and bat13 == 0 and bat14 == 0 and bat15 == 0 and bat16 == 0:
        print('game over')
        sys.exit(0)
else:
        print('plouf')

