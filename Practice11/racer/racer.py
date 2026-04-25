import pygame
import random
import time
import sys

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dodge & Coin Collector")

image_background = pygame.image.load('AnimatedStreet.png')

image_player = pygame.image.load('harry.jpg')
image_enemy = pygame.image.load('voloda.jpg')

coin1_img = pygame.image.load('coin1.jpg')
coin2_img = pygame.image.load('coin2.jpg')

image_enemy = pygame.transform.scale(image_enemy, (80, 120))
image_player = pygame.transform.scale(image_player, (80, 120))
coin1_img = pygame.transform.scale(coin1_img, (30, 30))
coin2_img = pygame.transform.scale(coin2_img, (30, 30))

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)
sound_crash = pygame.mixer.Sound('crash.wav')

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

image_game_over = font.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))

SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.generate_random_rect()

    def generate_random_rect(self):
        max_x = WIDTH - self.rect.width
        self.rect.left = random.randint(0, max_x)
        self.rect.bottom = 0

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

        if self.rect.top > HEIGHT:
            SCORE += 1
            self.generate_random_rect()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.value = random.choice([1, 2])

        self.set_image()

        self.rect = self.image.get_rect()
        self.generate_random_rect()

    def set_image(self):
        if self.value == 1:
            self.image = coin1_img
        else:
            self.image = coin2_img

    def generate_random_rect(self):
        self.value = random.choice([1, 2])
        self.set_image()

        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.bottom = random.randint(-100, -20)

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > HEIGHT:
            self.generate_random_rect()

player = Player()
enemy = Enemy()

coins = pygame.sprite.Group()
for _ in range(3):
    coins.add(Coin())

all_sprites = pygame.sprite.Group(player, enemy, *coins)

enemy_sprites = pygame.sprite.Group(enemy)

clock = pygame.time.Clock()
FPS = 60
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == INC_SPEED:
            SPEED += 0.5

    player.move()

    for entity in all_sprites:
        if entity != player:
            entity.move()

    if pygame.sprite.spritecollideany(player, enemy_sprites):
        pygame.mixer.music.stop()
        sound_crash.play()
        time.sleep(0.5)

        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.update()
        time.sleep(2)
        running = False

    collected = pygame.sprite.spritecollide(player, coins, False)

    for coin in collected:
        COINS_COLLECTED += coin.value  
        coin.generate_random_rect()


    screen.blit(image_background, (0, 0))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    score_text = font_small.render(f"Score: {SCORE}", True, "black")
    screen.blit(score_text, (10, 10))

    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, "black")
    screen.blit(coins_text, (WIDTH - coins_text.get_width() - 10, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()