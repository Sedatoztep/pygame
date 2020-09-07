import pygame, sys

pygame.init()
boyut = (800, 600)

python=pygame.image.load("icon.png")

yazininBoyutuX=python.get_size()[0]

print(yazininBoyutuX)
pencere = pygame.display.set_mode(boyut)
x = 0
y = 0
xYon=1
clock = pygame.time.Clock()

while True:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pencere.fill((0, 0, 0))

    if x > 800 - yazininBoyutuX or x < 0:
        xYon *= -1
    x += 5 * xYon

    pencere.blit(python, (x, y))
    pygame.display.update()








