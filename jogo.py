import pygame
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

lista_aranha = [Obstaculo("imagens/aranha.png",50,50,10,10),
               Obstaculo("imagens/aranha.png",50,50,850,120),
               Obstaculo("imagens/aranha.png",50,50,850,185),
               Obstaculo("imagens/aranha.png",50,50,850,265),
               Obstaculo("imagens/aranha.png",50,50,850,330),
               Obstaculo("imagens/aranha.png",50,50,850,400),
               Obstaculo("imagens/aranha.png",50,50,850,60),
               Obstaculo("imagens/aranha.png",50,50,850,120),
               Obstaculo("imagens/aranha.png",50,50,850,185),
               Obstaculo("imagens/aranha.png",50,50,850,265),
               Obstaculo("imagens/aranha.png",50,50,850,330),
               Obstaculo("imagens/aranha.png",50,50,850,400),
               Obstaculo("imagens/aranha.png",50,50,850,60),
               Obstaculo("imagens/aranha.png",50,50,850,120),
               Obstaculo("imagens/aranha.png",50,50,850,185),
               Obstaculo("imagens/aranha.png",50,50,850,265),
               Obstaculo("imagens/aranha.png",50,50,850,330),
               Obstaculo("imagens/aranha.png",50,50,850,400)]



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



    #Atualizando a tela
    pygame.display.update()

    #Regulando o FPS
    clock.tick(60)