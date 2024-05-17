import pygame
import random
from personagem import Personagem
from obstaculo import Obstaculo

pygame.init()

#Constrindo a tela
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Homem aranha")
tela.fill((129,245,66))

FUNDO = pygame.image.load("imagens/nova_york.png")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

#Criando mais personagens
jogador1 = Personagem("imagens/duende_verde.png",80,50,300,450)
#jogador2 = Personagem("imagens/aranha.png",50,50,450,450)

lista_aranha = lista_aranha = [Obstaculo("imagens/aranha.png", 20, 20, random.randint(0, 750), random.randint(-500, 0)) for _ in range(18)]
lista_bombinha = [Obstaculo("imagens/bombinha.png", 20, 20, random.randint(0, 750), random.randint(-500, 0)) for _ in range(10)]


#Configurando a fonte
fonte = pygame.font.SysFont("Castellar",14)


#Criando um relogio para controlar o FPS
clock = pygame.time.Clock()



rodando = True
while rodando:
    #Tratando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Você clicou!!")
        if evento.type == pygame.QUIT:
            rodando = False

    tela.blit(FUNDO,(0,0))
    #Desenhando as imagens
    jogador1.movimentar_via_controle(pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT)
    jogador1.desenhar(tela)
    
    for aranha in lista_aranha:
        aranha.movimenta()
        aranha.desenhar(tela)
        
    for bombinha in lista_bombinha:
        bombinha.movimenta()
        bombinha.desenhar(tela)



    #Atualizando a tela
    pygame.display.update()

    #Regulando o FPS
    clock.tick(60)