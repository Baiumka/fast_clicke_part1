import pygame
from random import *
#1.Сделать двухцветную рамку с случайным цветом.


CARD_COUNT = 4

COLOR = (150,150,150)
COLOR_RED = (255,0,0)
COLOR_GREEN = (0,200,0)


pygame.init()
window = pygame.display.set_mode(500, 500)
window.fill(COLOR)
clock = pygame.time.Clock()

card_list = []

book_list = ["Гарри Поттер", "Буратино", "Незнайка на марсе", "Метематика 11", "Литература 11"]


class Card():
    def __init__(self, color, w, h, x, y):
        self.color = color
        self.color_blink = color
        
        self.rect = pygame.Rect(x, y, w, h)
        self.border = pygame.Rect(x-5, y-5, w+10, h+10)
        self.text = pygame.font.SysFont('verdana', 15).render('CLICK', True, (0,0,0))
        self.is_show = False

    def show_text(self):
        self.is_show = True

    def hide_text(self):
        self.is_show = False

    def show(self):
       pygame.draw.rect(window, (0, 0, 255), self.border)
       pygame.draw.rect(window, self.color_blink, self.rect)
       if self.is_show == True:
            window.blit(self.text, (self.rect.x + self.rect.w/2-15, self.rect.y + self.rect.h/2))

for i in range(CARD_COUNT):
    myCard = Card(COLOR_RED, 100, 200, i*120+25, 150)
    card_list.append(myCard)

fraps_ccount = 0

while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for card in range(len(card_list)):
                if card_list[card].rect.collidepoint(x,y) == True:
                    if card_list[card].is_show == True:
                        card_list[card].color_blink = COLOR_GREEN
                    if card_list[card].is_show == False:
                        card_list[card].color_blink = COLOR





    if fraps_ccount == 5:
        for card in range(len(card_list)):
            card_list[card].color_blink = card_list[card].color

    if fraps_ccount == 10:
        for card in range(len(card_list)):
            card_list[card].hide_text()

        random_card = randint(0, len(card_list)-1)
        card_list[random_card].show_text()
        fraps_ccount = 0

    for card in card_list:
        card.show()

    fraps_ccount += 1
    clock.tick(30)
