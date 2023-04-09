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
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if key_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed


    def update2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if key_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed


player1 = Player('rocket.png', 630, 400, 10, 80, 80)
player2 = Player('rocket.png', 0, 400, 10, 80, 80)
ball = Player('ball.png', 200, 400, 0, 80, 60)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((50, 20, 100))

    player1.reset()
    player1.update()

    player2.reset()
    player2.update2()

    ball.reset()


    display.update()
    clock.tick(60)

