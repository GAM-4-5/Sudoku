import pygame
from checker import check, valid
import time
from random import *
pygame.font.init()

class Resetka:
    boards = [[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ],
            [
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [6, 8, 0, 4, 7, 0, 0, 2, 0],
        [0, 1, 9, 5, 0, 8, 6, 4, 7],
        [0, 6, 0, 9, 0, 0, 0, 0, 4],
        [3, 4, 2, 6, 8, 0, 0, 0, 0],
        [1, 9, 0, 0, 5, 0, 8, 3, 0],
        [0, 0, 0, 7, 2, 0, 4, 0, 3],
        [0, 0, 6, 0, 0, 5, 0, 1, 0],
        [0, 0, 3, 8, 9, 1, 5, 0, 0]
    ],
            [
        [6, 0, 0, 1, 0, 0, 0, 0, 2],
        [8, 0, 1, 0, 9, 0, 0, 0, 0],
        [0, 7, 5, 0, 8, 4, 0, 0, 0],
        [4, 3, 0, 0, 2, 0, 5, 6, 1],
        [5, 1, 8, 7, 0, 0, 4, 0, 9],
        [0, 9, 6, 4, 1, 0, 3, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 6, 0, 0, 3, 1, 0, 5, 0],
        [7, 0, 2, 5, 4, 0, 6, 0, 3]
    ],
            [
        [0, 0, 6, 0, 3, 1, 0, 7, 0],
        [4, 3, 7, 0, 0, 5, 0, 0, 0],
        [0, 1, 0, 4, 6, 7, 0, 0, 8],
        [0, 2, 9, 1, 7, 8, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 6],
        [3, 0, 0, 0, 5, 0, 0, 0, 0],
        [8, 0, 5, 0, 0, 4, 9, 1, 0],
        [0, 0, 3, 5, 0, 9, 0, 8, 7],
        [7, 9, 0, 0, 8, 6, 0, 0, 4]
    ],
            [
        [0, 0, 0, 0, 0, 5, 4, 0, 9],
        [4, 5, 1, 0, 0, 2, 3, 0, 0],
        [9, 8, 2, 0, 0, 0, 5, 6, 1],
        [6, 0, 7, 0, 0, 0, 9, 8, 0],
        [0, 0, 3, 4, 6, 0, 0, 0, 0],
        [5, 0, 0, 2, 8, 7, 0, 1, 0],
        [0, 4, 0, 0, 7, 0, 0, 9, 6],
        [3, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 5, 9, 4, 6, 8, 0, 2]
    ],
            [
        [0, 0, 1, 9, 8, 4, 7, 6, 0],
        [6, 0, 0, 0, 5, 7, 0, 0, 0],
        [8, 0, 7, 0, 1, 0, 0, 0, 0],
        [9, 6, 0, 3, 0, 8, 1, 0, 5],
        [1, 8, 5, 0, 2, 0, 0, 7, 3],
        [3, 0, 0, 0, 0, 0, 2, 0, 8],
        [2, 1, 0, 0, 0, 0, 0, 3, 6],
        [0, 0, 0, 1, 0, 0, 0, 0, 4],
        [0, 9, 6, 0, 0, 2, 5, 1, 0]
    ],
            [
        [8, 0, 0, 0, 5, 7, 0, 0, 0],
        [0, 0, 6, 0, 8, 0, 0, 0, 0],
        [0, 4, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 5, 2, 6, 0],
        [4, 0, 0, 0, 6, 3, 5, 0, 0],
        [0, 0, 1, 9, 0, 0, 0, 0, 0],
        [9, 0, 4, 6, 0, 0, 1, 3, 0],
        [0, 5, 7, 8, 0, 1, 0, 4, 0],
        [6, 0, 0, 0, 0, 0, 7, 2, 0]
    ],
            [
        [4, 7, 0, 1, 3, 0, 0, 0, 0],
        [0, 0, 2, 0, 9, 0, 0, 0, 0],
        [5, 0, 0, 0, 6, 4, 0, 1, 0],
        [2, 0, 4, 0, 8, 0, 0, 9, 0],
        [0, 8, 0, 0, 0, 5, 0, 4, 0],
        [0, 1, 3, 0, 0, 0, 0, 0, 8],
        [0, 9, 0, 0, 0, 0, 4, 7, 3],
        [7, 0, 0, 0, 4, 0, 8, 5, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 6]
    ],
            [
        [5, 0, 0, 6, 7, 0, 9, 0, 0],
        [0, 4, 0, 8, 0, 0, 0, 0, 0],
        [8, 0, 0, 5, 0, 0, 6, 1, 3],
        [0, 6, 2, 4, 0, 0, 0, 7, 0],
        [1, 0, 0, 0, 0, 3, 0, 2, 0],
        [3, 7, 4, 9, 0, 8, 0, 0, 0],
        [0, 9, 6, 1, 0, 7, 8, 0, 2],
        [2, 1, 8, 0, 0, 6, 0, 4, 5],
        [0, 5, 0, 0, 8, 0, 0, 9, 0]
    ]]

# nasumicno se biraju ploce iz liste boards    
    board = boards[randint(0, 8)]

    def __init__(self, redovi, stupci, sirina, visina):
        self.redovi = redovi
        self.stupci = stupci
        self.celije = [[Celija(self.board[i][j], i, j, sirina, visina) for j in range(stupci)] for i in range(redovi)]
        self.sirina = sirina
        self.visina = visina
        self.model = None
        self.selected = None

    def update_model(self):
        self.model = [[self.celije[i][j].value for j in range(self.stupci)] for i in range(self.redovi)]

# provjerava unesenu vrijednost        
    def place(self, val):
        red, stupac = self.selected
        if self.celije[red][stupac].value == 0:
            self.celije[red][stupac].set(val)
            self.update_model()
            if valid(self.model, val, (red, stupac)) and check(self.model):
                return True
            else:
                self.celije[red][stupac].set(0)
                self.celije[red][stupac].set_temp(0)
                self.update_model()
                return False

 # privremeno rjesenje (nije potvrđeno)           
    def skica(self, val):
        red, stupac = self.selected
        self.celije[red][stupac].set_temp(val)

# crta resetku        
    def draw(self, prozor):
        # linije
        g = self.sirina // 9
        for i in range(self.redovi + 1):
            if i % 3 == 0:
                d = 3
            else:
                d = 1
            pygame.draw.line(prozor, (0, 0, 0), (0, i * g), (self.sirina, i * g), d)
            pygame.draw.line(prozor, (0, 0, 0), (i * g, 0), (i * g, self.visina), d)
        # celije
        for i in range(self.redovi):
            for j in range(self.stupci):
                self.celije[i][j].draw(prozor)

    def select(self, red, stupac):
        for i in range(self.redovi):
            for j in range(self.stupci):
                self.celije[i][j].selected = False
        self.celije[red][stupac].selected = True
        self.selected = (red, stupac)

# ako zelimo obrisati uneseni broj, a nismo ga jos potvrdili        
    def clear(self):
        red, stupac = self.selected
        if self.celije[red][stupac].value == 0:
            self.celije[red][stupac].set_temp(0)

 # pozicija odabrane celije           
    def click(self, poz):
        if poz[0] < self.sirina and poz[1] < self.visina:
            g = self.visina // 9
            x = poz[0] // g
            y = poz[1] // g
            return (int(y),int(x))
        else:
            return None

# provjerava ako ima praznih celija na ploci        
    def zavrseno(self):
        for i in range(self.redovi):
            for j in range(self.stupci):
                if self.celije[i][j].value == 0:
                    return False
        return True


class Celija:
    redovi = 9
    stupci = 9

    def __init__(self, value, red, stupac, sirina, visina):
        self.value = value
        self.temp = 0
        self.red = red
        self.stupac = stupac
        self.sirina = sirina
        self.visina = visina
        self.selected = False

# oboji odabranu celiju (plavo) i crta broj koji upisujemo (plavo - nepotvrđeni, crno - potvrđeni)       
    def draw(self, prozor):
        font = pygame.font.SysFont("arial", 40)
        font2 = pygame.font.SysFont("arial", 30)
        g = self.sirina // 9
        x = self.stupac * g
        y = self.red * g
        if self.selected:
            pygame.draw.rect(prozor, (240, 248, 255), (x, y, g, g))
        if self.temp != 0 and self.value == 0:
            text = font2.render(str(self.temp), 1, (70, 130, 180))
            prozor.blit(text, (x + 5, y + 5))
        elif not(self.value == 0):
            text = font.render(str(self.value), 1, (0, 0, 0))
            prozor.blit(text, (x + (g // 2 - text.get_width() // 2), y + (g // 2 - text.get_height() // 2)))

# uneseno (potvrđeno) rjesenje          
    def set(self, val):
        self.value = val

# privremeno (neuneseno) rjesenje       
    def set_temp(self, val):
        self.temp = val

# crta pokusaje (X ako je uneseni broj netocan) i vrijeme        
def dodatci(prozor, board, time, pokusaji):
    prozor.fill((255, 255, 255))
    # vrijeme
    font = pygame.font.SysFont("arial", 40)
    text = font.render("Vrijeme: " + vrijeme(time), 1, (25, 25, 112))
    prozor.blit(text, (335, 547))
    # pokusaji
    text = font.render("X " * pokusaji, 1, (255, 0, 0))
    prozor.blit(text, (20, 547))
    board.draw(prozor)

def vrijeme(sek):
    s = sek % 60
    m = sek // 60
    h = m // 60
    v = " " + str(m) + ":" + str(s)
    return v

def main():
    prozor = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    board = Resetka(9, 9, 540, 540)
    k = None
    r = True
    start = time.time()
    pokusaji = 0
    while r:
        play_time = round(time.time() - start)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                r = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    k = 1
                if event.key == pygame.K_2:
                    k = 2
                if event.key == pygame.K_3:
                    k = 3
                if event.key == pygame.K_4:
                    k = 4
                if event.key == pygame.K_5:
                    k = 5
                if event.key == pygame.K_6:
                    k = 6
                if event.key == pygame.K_7:
                    k = 7
                if event.key == pygame.K_8:
                    k = 8
                if event.key == pygame.K_9:
                    k = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    k = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.celije[i][j].temp != 0:
                        if board.place(board.celije[i][j].temp):
                            print("Uspjeh!") # uneseni broj je tocan
                        else:
                            print("Krivo!") # uneseni broj je netocan
                            pokusaji += 1
                        k = None
                        if board.zavrseno():
                            print("Igra je završena!") # ploca je zavrsena
                            r = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                poz = pygame.mouse.get_pos()
                clicked = board.click(poz)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    k = None
        if board.selected and k != None:
            board.skica(k)
        dodatci(prozor, board, play_time, pokusaji)
        pygame.display.update()

main()
pygame.quit()
