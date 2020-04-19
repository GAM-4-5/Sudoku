import pygame, sys

class Sudoku:
    def __init__(self):
        pygame.init()
        self.prozor = pygame.display.set_mode((600, 600))
        self.pokrenuto = True
        self.resetka = [[0 for i in range(9)] for i in range(9)]
        self.odabrano = None
        self.pozicija = None
        
    def pokreni(self):
        while self.pokrenuto:
            self.pokusaji()
            self.update()
            self.nacrtaj()
        pygame.quit()
        sys.exit()
        
    def pokusaji(self):
        for pokusaj in pygame.event.get():
            if pokusaj.type == pygame.QUIT:
                self.pokrenuto = False
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
        self.prozor.fill((255, 255, 255))
        if self.odabrano:
            self.nacrtajOdabir(self.prozor, self.odabrano)
        self.nacrtajResetku(self.prozor)
        pygame.display.update()
#popunjava prozor bijelom bojom i smjesta resetku u prozor
        
    def nacrtajOdabir(self, prozor, poz):
        pygame.draw.rect(prozor, (204, 255, 255), ((poz[0] * 50) + (75, 100)[0], (poz[1] * 50) + (75, 100)[1], 50, 50))
#istice odabranu celiju plavom bojom
        
    def nacrtajResetku(self, prozor):
        pygame.draw.rect(prozor, (0, 0, 0), ((75, 100)[0], (75, 100)[1], 450, 450), 2)
        for i in range(9):
            if i % 3 != 0:
                pygame.draw.line(prozor, (0, 0, 0),((75, 100)[0] + (i * 50), (75, 100)[1]), ((75, 100)[0] + (i * 50), (75, 100)[1] + 450))
                pygame.draw.line(prozor, (0, 0, 0),((75, 100)[0], (75, 100)[1] + (i * 50)), ((75, 100)[0] + 450, (75, 100)[1] + (i * 50)))
            else:
                pygame.draw.line(prozor, (0, 0, 0),((75, 100)[0] + (i * 50), (75, 100)[1]), ((75, 100)[0] + (i * 50), (75, 100)[1] + 450), 2)
                pygame.draw.line(prozor, (0, 0, 0),((75, 100)[0], (75, 100)[1] + (i * 50)), ((75, 100)[0] + 450, (75, 100)[1] + (i * 50)), 2)
#crta resetku
                
    def unutarResetke(self):
        if self.pozicija[0] < (75, 100)[0] or self.pozicija[1] < (75, 100)[1]:
            return False
        if self.pozicija[0] > (75, 100)[0] + 450 or self.pozicija[1] > (75, 100)[1] + 450:
            return False
        return ((self.pozicija[0] - (75, 100)[0]) // 50, (self.pozicija[1] - (75, 100)[1]) // 50)
#provjerava je li pozicija strelice (miša) unutar resetke           
