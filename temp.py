# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

## 1 bateau 5 / 2 bateau 4 / 3 bateau 3
bateau11=5
bateau12=4
bateau13=4
bateau14=3
bateau15=3
bateau16=3
bateau21=5
bateau22=4
bateau23=4
bateau24=3
bateau25=3
bateau26=3
a=0
installerlast1=0
installerlast2=0
installerlast3=0
installerlast4=0


def placebateau(installer,a):
    bat11=[]
    bat12=[]
    bat13=[]
    bat14=[]
    bat15=[]
    bat16=[]
    
    
    while a<5:
        a=a+1
        bat11.append(installer)
    if 5<=a<9:
        a=a+1
        bat12.append(installer)
    if 9<=a<12:
        a=a+1
        bat13.append(installer)
    if 12<=a<15:
        a=a+1
        bat14.append(installer)
    if 15<=a<18:
        a=a+1
        bat15.append(installer)
    if 18<=a<21:
        a=a+1
        bat16.append(installer)
    return
    
    
def testbateau2(player1,bateau21,bateau22,bateau23,bateau24,bateau25,bateau26,
                bat21,bat22,bat23,bat24,bat25,bat26,):
    
    if player1 in bat21:
        bateau21=bateau21-1
        if bateau21==0:
            print('tu as coulé le bateau1')
    if player1 in bat22:
        bateau22=bateau22-1
        if bateau22==0:
            print('tu as coulé le bateau2')
    if player1 in bat23:
        bateau23=bateau23-1
        if bateau23==0:
            print('tu as coulé le bateau3')
    if player1 in bat24:
        bateau24=bateau24-1
        if bateau24==0:
            print('tu as coulé le bateau4')
    if player1 in bat25:
        bateau25=bateau25-1
        if bateau25==0:
            print('tu as coulé le bateau5')
    if player1 in bat26:
        bateau26=bateau26-1
        if bateau26==0:
            print('tu as coulé le bateau6')
    if bat21==0 and bat22==0 and bat23==0 and bat24==0 and bat25==0 and bat26==0:
        print('tu as gagné!!!)
        sys.exit(0)
    else:
        print('plouf')
    return

def testbateau2(player2,bateau11,bateau12,bateau13,bateau14,bateau15,bateau16,
                bat11,bat12,bat13,bat14,bat15,bat16,):
    
    if player2 in bat11:
        bateau11=bateau11-1
        if bateau11==0:
            print('ton bateau1 a été coulé')
    if player2 in bat12:
        bateau12=bateau12-1
        if bateau12==0:
            print('ton bateau2 a été coulé')
    if player2 in bat13:
        bateau13=bateau13-1
        if bateau13==0:
            print('ton bateau3 a été coulé')
    if player2 in bat14:
        bateau14=bateau14-1
        if bateau14==0:
            print('ton bateau4 a été coulé')
    if player2 in bat15:
        bateau15=bateau15-1
        if bateau15==0:
            print('ton bateau5 a été coulé')
    if player2 in bat16:
        bateau16=bateau16-1
        if bateau16==0:
            print('ton bateau6 a été coulé')
    if bat11==0 and bat12==0 and bat13==0 and bat14==0 and bat15==0 and bat16==0:
        print('tu as gagné!!!)
        sys.exit(0)
    else:
        print('plouf')
    return
