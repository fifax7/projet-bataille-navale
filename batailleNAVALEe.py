import sys

def affichageplateau (plateau):
    for i in range (0,11):
        print(plateau[i])


def lettrenombre (a1) :
    c=0
    if(a1=='A'):
        c=1
    elif(a1=='B'):
        c=2
    elif(a1=='C'):
        c=3
    elif(a1=='D'):
        c=4
    elif(a1=='E'):
        c=5
    elif(a1=='F'):
        c=6
        
    elif(a1=='G'):
        c=7
    elif(a1=='H'):
        c=8
    elif(a1=='I'):
        c=9
    elif(a1=='J'):
        c=10
    else:#(c==0):
        print("ERREUR, APPREND A LIRE RECOMMENCE TOUT")
        sys.exit(0)
    print(c)
    return c


def bateausuite (taille,c,a2,plateau):
    s=input("DROITE GAUCHE HAUT BAS")
    if(s=='DROITE'):
        for i in range(1,taille):
            c+1
            plateau[a2][c]='='
    return plateau


        
plateau=[ ['/','A','B','C','D','E','F','G','H','I','J'],
          ['1', '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
          ['2', '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
          ['3', '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
          ['4', '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
          ['5', '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
          ['6', '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
          ['7', '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
          ['8', '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
          ['9', '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
          ['10', '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0']]

affichageplateau(plateau)

## 1 bateau 5 / 2 bateau 4 / 3 bateau 3

print("Placer le bateau de taille 5")
a1=str(input("Choisir la colonne (A,B,C,..,J="))
a2=int(input("Choisir la ligne(1,2,...10)"))
c=lettrenombre(a1)
print(c,a2)
plateau[a2][c]='='
affichageplateau(plateau)
bateausuite (5,c,a2,plateau)
affichageplateau(plateau)
