import pygame
import random

# تهيئة pygame
pygame.init()

# إعدادات الشاشة
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Simple Game')

# إعداد ساعة اللعبة
clock = pygame.time.Clock()

# تعريف الكائن Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# إنشاء كائن اللاعب ومجموعة السبريتات
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# حلقة اللعبة الرئيسية
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # تحديث السبريتات
    all_sprites.update()

    # رسم الخلفية والسبريتات على الشاشة
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

    # ضبط سرعة اللعبة
    clock.tick(60)

# إنهاء pygame
pygame.quit()
