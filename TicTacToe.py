import pygame
import random


pygame.init()
font=pygame.font.Font("freesansbold.ttf",50)
fontSmall=pygame.font.Font("freesansbold.ttf",10)

screen = pygame.display.set_mode((400, 500))
lis=[0,1,2,3,4,5,6,7,8,9]
x_img = pygame.image.load("x.png")
o_img = pygame.image.load("o.png")
board = pygame.image.load("board.png")


# Locations for each square to show to "X" or "O"
s=[0,(10,110),(150,110),(285,110),(10,250),(150,250),(285,250),(10,385),(150,385),(285,385)]
def showBoard():
    screen.fill((153, 153, 255))
    screen.blit(board, (0, 100))
    pygame.draw.line(screen,(0,0,0),(0,95),(400,95),15)
    for i in range(1,10):
        if lis[i]=="X":
            screen.blit(x_img,s[i])
        elif lis[i]=="O":
            screen.blit(o_img,s[i])

def compMove():
    # checking straight lines
    for i in range(1,10,3):
        if lis[i]==lis[i+1] and (lis[i+2]!="O"and lis[i+2]!="X"):
            lis[i+2]="O"
            return 1
        elif lis[i] == lis[i + 2] and (lis[i + 1] != "O" and lis[i + 1] != "X"):
            lis[i + 1] = "O"
            return 1
        elif lis[i+1] == lis[i + 2] and (lis[i] != "O" and lis[i] != "X"):
            lis[i] = "O"
            return 1
    for i in range(1,4,1):
        if lis[i]==lis[i+3] and (lis[i+6]!="O"and lis[i+6]!="X"):
            lis[i+6]="O"
            return 1
        elif lis[i] == lis[i + 6] and (lis[i + 3] != "O" and lis[i + 3] != "X"):
            lis[i + 3] = "O"
            return 1
        elif lis[i+3] == lis[i + 6] and (lis[i] != "O" and lis[i] != "X"):
            lis[i] = "O"
            return 1
    # checking diagonals
    if lis[1]==lis[5] and (lis[9]!="O"and lis[9]!="X"):
        lis[9]="O"
        return 1
    elif lis[1] == lis[9] and (lis[5] != "O" and lis[5] != "X"):
        lis[5] = "O"
        return 1
    elif lis[5] == lis[9] and (lis[1] != "O" and lis[1] != "X"):
        lis[1] = "O"
        return 1

    if lis[3] == lis[5] and (lis[7] != "O" and lis[7] != "X"):
        lis[7] = "O"
        return 1
    elif lis[3] == lis[7] and (lis[5] != "O" and lis[5] != "X"):
        lis[5] = "O"
        return 1
    elif lis[5] == lis[7] and (lis[3] != "O" and lis[3] != "X"):
        lis[3] = "O"
        return 1
    # corners
    if lis[1]!="X" and lis[1]!="O":
        lis[1]="O"
        return 1
    if lis[3]!="X" and lis[3]!="O":
        lis[3]="O"
        return 1
    if lis[7]!="X" and lis[7]!="O":
        lis[7]="O"
        return 1
    if lis[9]!="X" and lis[9]!="O":
        lis[9]="O"
        return 1
    # center
    if lis[5]!="X" and lis[5]!="O":
        lis[3]="O"
        return 1
    # sides
    if lis[2]!="X" and lis[2]!="O":
        lis[2]="O"
        return 1

    if lis[4]!="X" and lis[4]!="O":
        lis[4]="O"
        return 1

    if lis[6]!="X" and lis[6]!="O":
        lis[6]="O"
        return 1

    if lis[8]!="X" and lis[8]!="O":
        lis[8]="O"
        return 1

def playerMove(x,y):
    if 0 < x < 134:
        if 110 < y < 235:
            if lis[1]!="O"and lis[1]!="X":
                lis[1]="X"
                return 0
        elif 235 < y < 365:
            if lis[4]!="O"and lis[4]!="X":
                lis[4]="X"
                return 0
        elif 365 < y < 490:
            if lis[7]!="O"and lis[7]!="X" :
                lis[7]="X"
                return 0
    elif 134 < x < 270:
        if 110 < y < 235:
            if lis[2]!="O"and lis[2]!="X" :
                lis[2]="X"
                return 0
        elif 235 < y < 365:
            if lis[5]!="O"and lis[5]!="X":
                lis[5]="X"
                return 0
        elif 365 < y < 490:
            if lis[8]!="O"and lis[8]!="X":
                lis[8]="X"
                return 0
    elif 270 < x < 394:
        if 110 < y < 235:
            if lis[3]!="O"and lis[3]!="X":
                lis[3]="X"
                return 0
        elif 235 < y < 365:
            if lis[6]!="O"and lis[6]!="X":
                lis[6]="X"
                return 0
        elif 365 < y < 490:
            if lis[9]!="O"and lis[9]!="X":
                lis[9]="X"
                return 0
    return 1

def checkWin(t):
    if lis[1]==lis[2]==lis[3]:
        pygame.draw.line(screen,(245, 5, 5),(10,150),(390,150),25)
        if t:
            compWon=font.render("Computer Won",True,(0,0,0),(240, 53, 50))
            screen.blit(compWon,(20,20))
            return True
        else:
            youWon=font.render("Player Won",True,(0,0,0),(240, 53, 50))
            screen.blit(youWon,(50,20))
            return True
    if lis[4]==lis[5]==lis[6]:
        pygame.draw.line(screen,(245, 5, 5),(10,300),(390,300),25)
        if t:
            compWon=font.render("Computer Won",True,(0,0,0),(240, 53, 50))
            screen.blit(compWon,(20,20))
            return True
        else:
            youWon=font.render("Player Won",True,(0,0,0),(240, 53, 50))
            screen.blit(youWon,(50,20))
            return True
    if lis[7]==lis[8]==lis[9]:
        pygame.draw.line(screen,(245, 5, 5),(10,430),(390,430),25)
        if t:
            compWon=font.render("Computer Won",True,(0,0,0),(240, 53, 50))
            screen.blit(compWon,(20,20))
            return True
        else:
            youWon=font.render("Player Won",True,(0,0,0),(240, 53, 50))
            screen.blit(youWon,(50,20))
            return True
    if lis[1]==lis[4]==lis[7]:
        pygame.draw.line(screen,(245, 5, 5),(60,100),(60,490),25)
        if t:
            compWon=font.render("Computer Won",True,(0,0,0),(240, 53, 50))
            screen.blit(compWon,(20,20))
            return True
        else:
            youWon=font.render("Player Won",True,(0,0,0),(240, 53, 50))
            screen.blit(youWon,(50,20))
            return True
    if lis[2]==lis[5]==lis[8]:
        pygame.draw.line(screen,(245, 5, 5),(200,100),(200,490),25)
        if t:
            compWon=font.render("Computer Won",True,(0,0,0),(240, 53, 50))
            screen.blit(compWon,(20,20))
            return True
        else:
            youWon=font.render("Player Won",True,(0,0,0),(240, 53, 50))
            screen.blit(youWon,(50,20))
            return True
    if lis[3]==lis[6]==lis[9]:
        pygame.draw.line(screen,(245, 5, 5),(335,100),(335,490),25)
        if t:
            compWon=font.render("Computer Won",True,(0,0,0),(240, 53, 50))
            screen.blit(compWon,(20,20))
            return True
        else:
            youWon=font.render("Player Won",True,(0,0,0),(240, 53, 50))
            screen.blit(youWon,(50,20))
            return True
    if lis[1]==lis[5]==lis[9]:
        pygame.draw.line(screen,(245, 5, 5),(0,100),(400,500),25)
        if t:
            compWon=font.render("Computer Won",True,(0,0,0),(240, 53, 50))
            screen.blit(compWon,(20,20))
            return True
        else:
            youWon=font.render("Player Won",True,(0,0,0),(240, 53, 50))
            screen.blit(youWon,(50,20))
            return True
    if lis[3]==lis[5]==lis[7]:
        pygame.draw.line(screen,(245, 5, 5),(400,100),(0,500),25)
        if t:
            compWon=font.render("Computer Won",True,(0,0,0),(240, 53, 50))
            screen.blit(compWon,(20,20))
            return True
        else:
            youWon=font.render("Player Won",True,(0,0,0),(240, 53, 50))
            screen.blit(youWon,(50,20))
            return True


def main():
    won = False
    turn = random.randint(0, 1)
    # 0 is computer's move and 1 is users move.
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Tic Tac Toe")
    running = True
    resetText = fontSmall.render("Press R to reset the board.", True, (0, 0, 0))
    while running:
        global lis
        showBoard()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.MOUSEBUTTONDOWN and turn==1 and not won:
                x,y=pygame.mouse.get_pos()
                turn=playerMove(x,y)
                won=checkWin(turn)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    lis=[0,1,2,3,4,5,6,7,8,9]
                    turn=random.randint(0,1)
                    won=False
        if turn==0 and not won:
            turn=compMove()

        won=checkWin(turn)
        if lis.count("X")+lis.count("O")==9 and not won:
            tie=font.render("TIE",True,(0,0,0),(240, 53, 50))
            screen.blit(tie,(165,20))
            screen.blit(resetText,(150,75))
        if won:
            screen.blit(resetText, (150, 75))
        pygame.display.update()
    pygame.display.quit()

if __name__=="__main__":
    main()
