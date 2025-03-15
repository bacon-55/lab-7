#импортируем библеотику пайгейм 
import pygame

#Инициализируем все импортированные модули Pygame
pygame.init()

#Устанавливаем размеры окна нашего приложения , первое значение ширина , второе высота 
screen = pygame.display.set_mode((800, 600))


running = True

while running:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
