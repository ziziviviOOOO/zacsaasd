import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Встановлення розмірів вікна та фонового кольору
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
BACKGROUND_COLOR = ('deeppink')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BACKGROUND_COLOR)
# icon = pygame.image.load('click.webp')
# pygame.display.set_icon(icon)
# Налаштування гри
clock = pygame.time.Clock()
FPS = 40
score = 0
time_remaining = 10  # Секунди
target_score = 10
card_color = ('purple')  # Задати початковий колір картки

# Ініціалізація таймера
change_position_time = pygame.USEREVENT + 1
pygame.time.set_timer(change_position_time, 1000)  # Зміна положення кожну секунду
pygame.display.set_caption('Clicker')


# Функція відображення тексту
def display_text(text, x, y, size=30, color=(0, 0, 0)):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


# Генеруємо випадкові координати для розміщення квадрата перед початком циклу
card_x = random.randint(0, SCREEN_WIDTH - 100)  # ширина екрану мінус ширина картки
card_y = random.randint(0, SCREEN_HEIGHT - 100)  # висота екрану мінус висота картки

# Встановлюємо координати та розміри квадрата
card_rect = pygame.Rect(card_x, card_y, 100, 100)

# Основний цикл гри
running = True
while running:
    clock.tick(FPS)

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if card_rect.collidepoint(mouse_x, mouse_y):
                score += 1
                card_color = ('pink')
            else:
                score -= 1
                card_color = ('darksalmon')
        elif event.type == change_position_time:  # Якщо час змінити положення
            card_x = random.randint(0, SCREEN_WIDTH - 100)
            card_y = random.randint(0, SCREEN_HEIGHT - 100)
            card_rect.topleft = (card_x, card_y)

            # Оновлення відображення
    screen.fill(BACKGROUND_COLOR)

    # Відображення картки з написом CLICK
    pygame.draw.rect(screen, card_color, card_rect)
    display_text("CLICK", card_rect.centerx, card_rect.centery)

    # Відображення статистики
    display_text(f"Score: {score}/{target_score}", 250, 50)
    display_text(f"Time: {time_remaining:.1f}", 250, 100)

    # Перевірка на перемогу або програш
    if score >= target_score or time_remaining <= 0:
        running = False

        # Оновлення графіки
    pygame.display.update()

    # Зменшення часу
    time_remaining -= 1 / FPS

# Виведення повідомлення про результат
if score >= target_score:
    print("You win!")
else:
    print("Game over!")

# Завершення гри
pygame.quit()
