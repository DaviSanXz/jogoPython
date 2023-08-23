import pygame

pygame.init()


# tamanho e largura da tela 
x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Meu jogo em python')


# imagens do jogo
bgImg = pygame.image.load('img/ceuEstrelado.jpg').convert_alpha()
bg = pygame.transform.scale(bgImg, (x, y))

playerImg = pygame.image.load('img/nave.png').convert_alpha()
player = pygame.transform.scale(playerImg, (100, 100))
player = pygame.transform.rotate(player, -90)

rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        screen.blit(bg, (0,0))

    relativo_x = x % bg.get_rect().width
    screen.blit(bg, (relativo_x, - bg.get_rect().width, 0)) 

    if relativo_x < 1280:
        screen.blit(bg, (relativo_x, 0))

        x -= 1
                

     

    pygame.display.update()        