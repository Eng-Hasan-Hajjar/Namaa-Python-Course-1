import pygame
import random

# تهيئة pygame
pygame.init()

# إعدادات الشاشة
screen_width, screen_height = 300, 600
block_size = 30
grid_width, grid_height = screen_width // block_size, screen_height // block_size

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tetris')

# الألوان
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# تعريف الكائن Block
class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((block_size, block_size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
     # داخل كلاس القطعة (Block)
    def move_left(self):
        self.rect.x -= block_size

    def move_right(self):
        self.rect.x += block_size

    def move_down(self):
        self.rect.y += block_size

    def rotate(self):
        # حفظ الموقع الحالي
        old_center = self.rect.center

        # دوران الصورة
        self.image = pygame.transform.rotate(self.image, 90)

        # إعادة تعيين موقع الصورة بناءً على المركز القديم
        self.rect = self.image.get_rect()
        self.rect.center = old_center


    def drop(self):
        # إسقاط الصورة بشكل فوري
        self.rect.y += block_size

# إنشاء قطعة الأرضية (اللون الأسود)
ground = Block(BLACK)
ground.rect.y = screen_height - block_size

# إعداد المربعات الفارغة (اللون الأبيض)
empty_block = Block(WHITE)

# إعداد الشبكة (مصفوفة لتخزين الألوان)
grid = [[empty_block for _ in range(grid_width)] for _ in range(grid_height)]

# دالة لرسم الشبكة على الشاشة
def draw_grid():
    for row in range(grid_height):
        for col in range(grid_width):
            block = grid[row][col]
            block.rect.x = col * block_size
            block.rect.y = row * block_size
            screen.blit(block.image, block.rect)

# دالة لحذف السطور الكاملة
def delete_full_rows():
    global grid
    full_rows = []
    for row in range(grid_height):
        if all(block.image.get_at((0, 0)) != WHITE for block in grid[row]):
            full_rows.append(row)

    for row in sorted(full_rows, reverse=True):
        del grid[row]
        grid.insert(0, [empty_block for _ in range(grid_width)])

# إعداد الساعة والمجموعة الكلية للسبرايتات
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
all_sprites.add(ground)

# حلقة اللعبة الرئيسية
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # معالجة الحركة والإدخالات هنا...
    # داخل حلقة اللعب الرئيسية

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_block.move_left()
            elif event.key == pygame.K_RIGHT:
                current_block.move_right()
            elif event.key == pygame.K_DOWN:
                current_block.move_down()
            elif event.key == pygame.K_UP:
                current_block.rotate()
            elif event.key == pygame.K_SPACE:
                current_block.drop()

   

    # مسح الشاشة
    screen.fill(WHITE)

    # رسم الشبكة والأرضية
    draw_grid()
    screen.blit(ground.image, ground.rect)

    # حذف السطور الكاملة وتحديث الشبكة
    delete_full_rows()

    # تحديث الشاشة
    pygame.display.flip()

    # ضبط سرعة اللعبة
    clock.tick(10)

# إنهاء pygame
pygame.quit()
