import pygame, sys

s = 600
v = 600
bijelo = (255, 255, 255)
crno = (0, 0, 0)
plavo = (204, 255, 255)
sivo = (189, 189, 189)
crveno = (195, 121, 121)
poz_re = (75, 100)
test = [[0,6,0,2,0,0,8,3,1],
        [0,0,0,0,8,4,0,0,0],
        [0,0,7,6,0,3,0,4,9],
        [0,4,6,8,0,2,1,0,0],
        [0,0,3,0,9,6,0,0,0],
        [1,2,0,7,0,5,0,0,6],
        [7,3,0,0,0,1,0,2,0],
        [8,1,5,0,2,9,7,0,0],
        [0,0,0,0,7,0,0,1,5]]


class Sudoku:
    def __init__(self):
        pygame.init()
        self.prozor = pygame.display.set_mode((s, v))
        self.pokrenuto = True
        self.resetka = test
        self.odabrano = None
        self.pozicija = None
        self.font = pygame.font.SysFont("arial", 50//2)

        
    def pokreni(self):
        while self.pokrenuto:
            if self.state == 'playing':
                self.pokusaji()
                self.update()
                self.nacrtaj()
        pygame.quit()
        sys.exit()
        
    def pokusaji(self):
        for pokusaj in pygame.event.get():
            if pokusaj.type == pygame.QUIT:
                self.pokrenuto = False

            #kada kliknemo
            if pokusaj.type == pygame.MOUSEBUTTONDOWN:
                odabrano = self.unutarResetke()
                if odabrano:
                    self.odabrano = odabrano
                else:
                    self.odabrano = None
                    
                
#moguce odabrati celiju samo unutar resetke
                    
    def update(self):
        self.pozicija = pygame.mouse.get_pos()



    def nacrtaj(self):
        self.prozor.fill(bijelo)
        if self.odabrano:
            self.nacrtajOdabir(self.prozor, self.odabrano)
        self.brojevi(self.prozor)
        self.nacrtajResetku(self.prozor)
        pygame.display.update()

                  
               


    def brojevi(self, prozor):
        for y, red in enumerate(self.resetka):
            for x, br in enumerate(red):
                if br != 0:
                    poz = [x * 50 + poz_re[0], y * 50 + poz_re[1]]
                    self.textToScreen(prozor, str(br), poz)

        
    def nacrtajOdabir(self, prozor, poz):
        pygame.draw.rect(prozor, plavo, ((poz[0] * 50) + poz_re[0], (poz[1] * 50) + poz_re[1], 50, 50))
#istice odabranu celiju plavom bojom
        
    def nacrtajResetku(self, prozor):
        pygame.draw.rect(prozor, crno, (poz_re[0], poz_re[1], 450, 450), 2)
        for i in range(9):
            if i % 3 != 0:
                pygame.draw.line(prozor, crno,(poz_re[0] + (i * 50), poz_re[1]), (poz_re[0] + (i * 50), poz_re[1] + 450))
                pygame.draw.line(prozor, crno,(poz_re[0], poz_re[1] + (i * 50)), (poz_re[0] + 450, poz_re[1] + (i * 50)))
            else:
                pygame.draw.line(prozor, crno,(poz_re[0] + (i * 50), poz_re[1]), (poz_re[0] + (i * 50), poz_re[1] + 450), 2)
                pygame.draw.line(prozor, crno,(poz_re[0], poz_re[1] + (i * 50)), (poz_re[0] + 450, poz_re[1] + (i * 50)), 2)
#crta resetku
                
    def unutarResetke(self):
        if self.pozicija[0] < poz_re[0] or self.pozicija[1] < poz_re[1]:
            return False
        if self.pozicija[0] > poz_re[0] + 450 or self.pozicija[1] > poz_re[1] + 450:
            return False
        return ((self.pozicija[0] - poz_re[0]) // 50, (self.pozicija[1] - poz_re[1]) // 50)
#provjerava je li pozicija strelice (miša) unutar resetke


    def textToScreen(self, prozor, text, poz):
        font = self.font.render(text, False, crno)
        fontW = font.get_width()
        fontH = font.get_height()
        poz[0] += (50 - fontW) // 2
        poz[1] += (50 - fontH) // 2
        prozor.blit(font, poz)
        

  
