import pygame
from checker import check, valid
import time
pygame.font.init()


class Resetka:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

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

    def sketch(self, val):
        red, stupac = self.selected
        self.celije[red][stupac].set_temp(val)

    def draw(self, prozor):
        # linije
        g = self.sirina // 9
        for i in range(self.redovi + 1):
            if i % 3 == 0 and i != 0:
                d = 4
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

    def clear(self):
        red, stupac = self.selected
        if self.celije[red][stupac].value == 0:
            self.celije[red][stupac].set_temp(0)

    def click(self, poz):
        if poz[0] < self.sirina and poz[1] < self.visina:
            g = self.visina // 9
            x = poz[0] // g
            y = poz[1] // g
            return (int(y),int(x))
        else:
            return None

    def is_finished(self):
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

    def draw(self, prozor):
        font = pygame.font.SysFont("arial", 40)

        g = self.sirina // 9
        x = self.stupac * g
        y = self.red * g

        if self.temp != 0 and self.value == 0:
            text = font.render(str(self.temp), 1, (128, 128, 128))
            prozor.blit(text, (x + 5, y + 5))
        elif not(self.value == 0):
            text = font.render(str(self.value), 1, (0, 0, 0))
            prozor.blit(text, (x + (g // 2 - text.get_width() // 2), y + (g // 2 - text.get_height() // 2)))

        if self.selected:
            pygame.draw.rect(prozor, (255, 0, 0), (x, y, g, g), 3)

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val


def redraw_prozor(prozor, board, time, pokusaji):
    prozor.fill((255, 255, 255))
    # vrijeme
    font = pygame.font.SysFont("arial", 40)
    text = font.render("Vrijeme: " + format_time(time), 1, (0, 0, 0))
    prozor.blit(text, (340, 550))
    # pokusaji
    text = font.render("X " * pokusaji, 1, (255, 0, 0))
    prozor.blit(text, (20, 550))
    board.draw(prozor)


def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    v = " " + str(minute) + ":" + str(sec)
    return v


def main():
    prozor = pygame.display.set_mode((540,600))
    pygame.display.set_caption("Sudoku")
    board = Resetka(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()
    pokusaji = 0
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.celije[i][j].temp != 0:
                        if board.place(board.celije[i][j].temp):
                            print("Uspjeh!")
                        else:
                            print("Krivo!")
                            pokusaji += 1
                        key = None

                        if board.is_finished():
                            print("Game over!")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                poz = pygame.mouse.get_pos()
                clicked = board.click(poz)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        redraw_prozor(prozor, board, play_time, pokusaji)
        pygame.display.update()


main()
pygame.quit()
