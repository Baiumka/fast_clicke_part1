import pygame

CARD_COUNT = 4

COLOR = (150,150,150)
COLOR_RED = (255,0,0)


pygame.init()
window = pygame.display.set_mode(500, 500)
window.fill(COLOR)
clock = pygame.time.Clock()

card_list = []

class Card():
    def __init__(self, color, w, h, x, y):
        self.color = color
        self.rect = pygame.Rect(x, y, w, h)
        self.border = pygame.Rect(x-5, y-5, w+10, h+10)
        self.text = pygame.font.SysFont('verdana', 15).render('CLICK', True, (0,0,0))


    def show(self):
       pygame.draw.rect(window, (0, 0, 255), self.border)
       pygame.draw.rect(window, self.color, self.rect)
       window.blit(self.text, (self.rect.x + self.rect.w/2-15, self.rect.y + self.rect.h/2))

for i in range(CARD_COUNT):
    myCard = Card(COLOR_RED, 100, 200, 5+i*120, 150)
    card_list.append(myCard)

while True:
    pygame.display.update()

    for card in card_list:
        card.show()

    clock.tick(30)
