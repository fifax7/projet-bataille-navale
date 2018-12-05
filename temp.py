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

a = 0

lettre = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
chiifre = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
direction = ['bas', 'haut', 'droite', 'gauche']

class position:
    def __init__(self, nocolonne, noligne,noposition):
        self.nocolonne = nocolonne
        self.noligne = noligne
        self.noposition= noposition

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


basecoordonne = {coordonnes('A', '1', 'a1'), coordonnes('A', '2', 'a2'), coordonnes('A', '3', 'a3'),
                 coordonnes('A', '4', 'a4'), coordonnes('A', '5', 'a5'), coordonnes('A', '6', 'a6'),
                 coordonnes('A', '7', 'a7'), coordonnes('A', '8', 'a8'), coordonnes('A', '9', 'a9'),
                 coordonnes('A', '10', 'a10'),
                 coordonnes('B', '1', 'b1'), coordonnes('B', '2', 'b2'), coordonnes('B', '3', 'b3'),
                 coordonnes('B', '4', 'b4'), coordonnes('B', '5', 'b5'), coordonnes('B', '6', 'b6'),
                 coordonnes('B', '7', 'b7'), coordonnes('B', '8', 'b8'), coordonnes('B', '9', 'b9'),
                 coordonnes('B', '10', 'b10'),
                 coordonnes('C', '1', 'c1'), coordonnes('C', '2', 'c2'), coordonnes('C', '3', 'c3'),
                 coordonnes('C', '4', 'c4'), coordonnes('C', '5', 'c5'), coordonnes('C', '6', 'c6'),
                 coordonnes('C', '7', 'c7'), coordonnes('C', '8', 'c8'), coordonnes('C', '9', 'c9'),
                 coordonnes('C', '10', 'c10'),
                 coordonnes('D', '1', 'd1'), coordonnes('D', '2', 'd2'), coordonnes('D', '3', 'd3'),
                 coordonnes('D', '4', 'd4'), coordonnes('D', '5', 'd5'), coordonnes('D', '6', 'd6'),
                 coordonnes('D', '7', 'd7'), coordonnes('D', '8', 'd8'), coordonnes('D', '9', 'd9'),
                 coordonnes('D', '10', 'd10'),
                 coordonnes('E', '1', 'e1'), coordonnes('E', '2', 'e2'), coordonnes('E', '3', 'e3'),
                 coordonnes('E', '4', 'e4'), coordonnes('E', '5', 'e5'), coordonnes('E', '6', 'e6'),
                 coordonnes('E', '7', 'e7'), coordonnes('E', '8', 'e8'), coordonnes('E', '9', 'e9'),
                 coordonnes('E', '10', 'e10'),
                 coordonnes('F', '1', 'f1'), coordonnes('F', '2', 'f2'), coordonnes('F', '3', 'f3'),
                 coordonnes('F', '4', 'f4'), coordonnes('F', '5', 'f5'), coordonnes('F', '6', 'f6'),
                 coordonnes('F', '7', 'f7'), coordonnes('F', '8', 'f8'), coordonnes('F', '9', 'f9'),
                 coordonnes('F', '10', 'f10'),
                 coordonnes('G', '1', 'g1'), coordonnes('G', '2', 'g2'), coordonnes('G', '3', 'g3'),
                 coordonnes('G', '4', 'g4'), coordonnes('G', '5', 'g5'), coordonnes('G', '6', 'g6'),
                 coordonnes('G', '7', 'g7'), coordonnes('G', '8', 'g8'), coordonnes('G', '9', 'g9'),
                 coordonnes('G', '10', 'g10'),
                 coordonnes('H', '1', 'h1'), coordonnes('H', '2', 'h2'), coordonnes('H', '3', 'h3'),
                 coordonnes('H', '4', 'h4'), coordonnes('H', '5', 'h5'), coordonnes('H', '6', 'h6'),
                 coordonnes('H', '7', 'h7'), coordonnes('H', '8', 'h8'), coordonnes('H', '9', 'h9'),
                 coordonnes('F', '10', 'h10'),
                 coordonnes('I', '1', 'i1'), coordonnes('I', '2', 'i2'), coordonnes('I', '3', 'i3'),
                 coordonnes('I', '4', 'i4'), coordonnes('I', '5', 'i5'), coordonnes('I', '6', 'i6'),
                 coordonnes('I', '7', 'i7'), coordonnes('I', '8', 'i8'), coordonnes('I', '9', 'i9'),
                 coordonnes('I', '10', 'i10'),
                 coordonnes('J', '1', 'j1'), coordonnes('J', '2', 'j2'), coordonnes('J', '3', 'j3'),
                 coordonnes('J', '4', 'j4'), coordonnes('J', '5', 'j5'), coordonnes('J', '6', 'j6'),
                 coordonnes('J', '7', 'j7'), coordonnes('J', '8', 'j8'), coordonnes('J', '9', 'j9'),
                 coordonnes('J', '10', 'j10')},


def positionbateaujoeur(installer, a):
    bat11 = []
    bat12 = []
    bat13 = []
    bat14 = []
    bat15 = []
    bat16 = []

    while a < 5:
        a = a + 1
        bat11.append(installer)
    if 5 <= a < 9:
        a = a + 1
        bat12.append(installer)
    if 9 <= a < 12:
        a = a + 1
        bat13.append(installer)
    if 12 <= a < 15:
        a = a + 1
        bat14.append(installer)
    if 15 <= a < 18:
        a = a + 1
        bat15.append(installer)
    if 18 <= a < 21:
        a = a + 1
        bat16.append(installer)
    return


def testbateau2(player1, bateau21, bateau22, bateau23, bateau24, bateau25, bateau26,
                bat21, bat22, bat23, bat24, bat25, bat26, ):
    if player1 in bat21:
        bateau21 = bateau21 - 1
        if bateau21 == 0:
            print('tu as coulé le bateau1')
    if player1 in bat22:
        bateau22 = bateau22 - 1
        if bateau22 == 0:
            print('tu as coulé le bateau2')
    if player1 in bat23:
        bateau23 = bateau23 - 1
        if bateau23 == 0:
            print('tu as coulé le bateau3')
    if player1 in bat24:
        bateau24 = bateau24 - 1
        if bateau24 == 0:
            print('tu as coulé le bateau4')
    if player1 in bat25:
        bateau25 = bateau25 - 1
        if bateau25 == 0:
            print('tu as coulé le bateau5')
    if player1 in bat26:
        bateau26 = bateau26 - 1
        if bateau26 == 0:
            print('tu as coulé le bateau6')
    if bat21 == 0 and bat22 == 0 and bat23 == 0 and bat24 == 0 and bat25 == 0 and bat26 == 0:
        print('tu as gagné!!!')
        sys.exit(0)
    else:
        print('plouf')
    return


def testbateau1(player2, bateau11, bateau12, bateau13, bateau14, bateau15, bateau16,
                bat11, bat12, bat13, bat14, bat15, bat16, ):
    if player2 in bat11:
        bateau11 = bateau11 - 1
        if bateau11 == 0:
            print('ton bateau1 a été coulé')
    if player2 in bat12:
        bateau12 = bateau12 - 1
        if bateau12 == 0:
            print('ton bateau2 a été coulé')
    if player2 in bat13:
        bateau13 = bateau13 - 1
        if bateau13 == 0:
            print('ton bateau3 a été coulé')
    if player2 in bat14:
        bateau14 = bateau14 - 1
        if bateau14 == 0:
            print('ton bateau4 a été coulé')
    if player2 in bat15:
        bateau15 = bateau15 - 1
        if bateau15 == 0:
            print('ton bateau5 a été coulé')
    if player2 in bat16:
        bateau16 = bateau16 - 1
        if bateau16 == 0:
            print('ton bateau6 a été coulé')
    if bat11 == 0 and bat12 == 0 and bat13 == 0 and bat14 == 0 and bat15 == 0 and bat16 == 0:
        print('tu as gagné!!!')
        sys.exit(0)
    else:
        print('plouf')
    return



def aleatoirebateau(P):
    lignebat=radint(0,10)
    colonnebat= radint(0,10)
    
