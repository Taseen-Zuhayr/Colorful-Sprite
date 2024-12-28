import pygame
import random
pygame.init()

Sprite_ColorChange_Event = pygame.USEREVENT + 1
Background_ColorChange_Event = pygame.USEREVENT + 2

# Background Colors
blue = pygame.Color('blue')
lightblue = pygame.Color('lightblue')
darkblue = pygame.Color('darkblue')

# Sprite Colors
yellow = pygame.Color('yellow')
magenta = pygame.Color('magenta')
orange = pygame.Color('orange')
white = pygame.Color('white')


class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]),
                         random.choice([-1, 1])]
        
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(Sprite_ColorChange_Event))
            pygame.event.post(pygame.event.Event(Background_ColorChange_Event))

    def change_color(self):
        self.image.fill(random.choice([yellow, magenta, orange, white]))

def change_backgroundcolor():
    global bg_color
    bg_color = random.choice([blue, lightblue, darkblue])

All_Sprites_List = pygame.sprite.Group()
sp1 = Sprite(white, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0,370)
All_Sprites_List.add(sp1)
sp2 = Sprite(orange, 20, 30)
sp2.rect.x = random.randint(50, 300)
sp2.rect.y = random.randint(50,300)
All_Sprites_List.add(sp2)
sp3 = Sprite(yellow, 20, 30)
sp3.rect.x = random.randint(75, 350)
sp3.rect.y = random.randint(75,350)
All_Sprites_List.add(sp3)
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colorful Bounce")
bg_color = blue
screen.fill(bg_color)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == Sprite_ColorChange_Event:
            sp1.change_color()
        elif event.type == Background_ColorChange_Event:
            change_backgroundcolor()
    All_Sprites_List.update()
    screen.fill(bg_color)
    All_Sprites_List.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()



