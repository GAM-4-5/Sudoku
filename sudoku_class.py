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
        self.state = 'playing'
        self.gotovo = False
        self.promjena_celije = False
        self.zakljucana_celija = []
        self.netocna_celija = []
        self.font = pygame.font.SysFont("arial", 50//2)
        self.load()
        
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
                    
            #kada upisemo broj
            if pokusaj.type == pygame.KEYDOWN:
                if self.odabrano != None and self.odabrano not in self.zakljucana_celija:
                    if self.isInt(pokusaj.unicode):
                        self.resetka[self.odabrano[1]][self.odabrano[0]] = int(pokusaj.unicode)
                        self.promjena_celije = True
                    
                
#moguce odabrati celiju samo unutar resetke
                    
    def update(self):
        self.pozicija = pygame.mouse.get_pos()
        if self.promjena_celije:
            self.netocna_celija = []
            if self.sve_celije():
                self.provjeri_sve_celije()


    def nacrtaj(self):
        self.prozor.fill(bijelo)
        if self.odabrano:
            self.nacrtajOdabir(self.prozor, self.odabrano)
        self.boja_zakljucane_celije(self.prozor, self.zakljucana_celija)
        self.boja_netocne_celije(self.prozor, self.netocna_celija)
        self.brojevi(self.prozor)
        self.nacrtajResetku(self.prozor)
        pygame.display.update()
        self.promjena_celije = False
        
#popunjava prozor bijelom bojom i smjesta resetku u prozor

    def sve_celije(self):
        for red in self.resetka:
            for broj in red:
                if broj == 0:
                    return False
        return True
    
    def provjeri_sve_celije(self):
        self.provjeri_redove()
        self.provjeri_stupce()
        self.provjeri_male_resetke()


    def provjeri_male_resetke(self):
        for a in range(3):
            for b in range(3):
                mogucnosti = [1,2,3,4,5,6,7,8,9]
                for i in range(3):
                    for j in range(3):
                        x = a * 3 + i
                        y = b * 3 + j
                        if self.resetka[y][x] in mogucnosti:
                            mogucnosti.remove(self.resetka[y][x])
                        else:
                            if [x, y] not in self.zakljucana_celija and [x, y] not in self.netocna_celija:
                                self.netocna_celija.append([x, y])
                            if [x, y] in self.zakljucana_celija:
                                for k in range(3):
                                    for l in range(3):
                                        x2 = a * 3 + k
                                        y2 = b * 3 + l
                                        if self.resetka[y2][x2] == self.resetka[y][x] and [x2, y2] not in self.zakljucana_celija:
                                            self.netocna_celija.append([x2, y2])
                                
 #provjerava ako se broj ponavlja u maloj resetki (3x3)                               
                        
    def provjeri_redove(self):
        for x in range(9):
            mogucnosti = [1,2,3,4,5,6,7,8,9]
            for y, red in enumerate(self.resetka):
                if self.resetka[y][x] in mogucnosti:
                    mogucnosti.remove(self.resetka[y][x])
                else:
                    if [x, y] not in self.zakljucana_celija and [x, y] not in self.netocna_celija:
                        self.netocna_celija.append([x, y])
                    if [x, y] in self.zakljucana_celija:
                        for i in range (9):
                            if self.resetka[y][i] == self.resetka[y][x] and [i, y] not in self.zakljucana_celija:
                                self.netocna_celija.append([i, y])

                        
#provjerava ako se broj ponavlja u redu

    def provjeri_stupce(self):
        for y, red in enumerate(self.resetka):
            mogucnosti = [1,2,3,4,5,6,7,8,9]
            for x in range(9):
                if self.resetka[y][x] in mogucnosti:
                    mogucnosti.remove(self.resetka[y][x])
                else:
                    if [x, y] not in self.zakljucana_celija and [x, y] not in self.netocna_celija:
                        self.netocna_celija.append([x, y])
                    if [x, y] in self.zakljucana_celija:
                        for i, red in enumerate(self.resetka):
                            if self.resetka[i][x] == self.resetka[y][x] and [x, i] not in self.zakljucana_celija:
                                self.netocna_celija.append([x, i])
               
#provjerava ako se broj ponavlja u stupcu
               
    def boja_netocne_celije(self, prozor, netocno):
        for celija in netocno:
            pygame.draw.rect(prozor, crveno, (celija[0] * 50 + poz_re[0], celija[1] * 50 + poz_re[1], 50, 50))

    def boja_zakljucane_celije(self, prozor, zakljucano):
        for celija in zakljucano:
            pygame.draw.rect(prozor, sivo, (celija[0] * 50 + poz_re[0], celija[1] * 50 + poz_re[1], 50, 50))

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
        

    def load(self):
        for y, red in enumerate(self.resetka):
            for x, br in enumerate(red):
                if br != 0:
                    self.zakljucana_celija.append([x, y])
        
    def isInt(self, string):
        try:
            int(string)
            return True
        except:
            return False
