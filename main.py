from pygame import *


clock = time.Clock()

window = display.set_mode((700,500))

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed, widht, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (widht, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

        if key_pressed[K_RIGHT] and self.rect.x < 600:
            self.rect.x += self.speed

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((50, 20, 100))

    display.update()
    clock.tick(60)
