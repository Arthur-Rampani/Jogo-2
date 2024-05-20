import pygame
import random
from personagem import *
from obstaculo import *

pygame.init()
pontuação = 0

#Constrindo a tela
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Homem aranha")
tela.fill((129,245,66))

FUNDO = pygame.image.load("imagens/nova_york.png")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

#Criando mais personagens
jogador1 = Personagem("imagens/duende_verde.png",80,50,300,450)
#jogador2 = Personagem("imagens/aranha.png",50,50,450,450)

lista_aranha = lista_aranha = [Obstaculo("imagens/aranha.png", 20, 20, random.randint(0, 750), random.randint(-500, 0)) for x in range(18)]
lista_bombinha = [Obstaculo("imagens/bombinha.png", 20, 20, random.randint(0, 750), random.randint(-500, 0)) for x in range(10)]


#Configurando a fonte
fonte = pygame.font.SysFont("Arial Black",14)
fonte2 = pygame.font.SysFont("Arial Black",14)


#Criando um relogio para controlar o FPS
clock = pygame.time.Clock()


# Carregar e iniciar música de fundo
pygame.mixer.music.load('musica_homem_aranha.mp3')
pygame.mixer.music.play(-1)

# Carregar som da bombinha
som_bombinha = pygame.mixer.Sound('risada_duende.mp3')

rodando = True
while rodando:
    #Tratando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Você clicou!!")
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jogador1.usar_poder()

    tela.blit(FUNDO,(0,0))
    #Desenhando as imagens
    jogador1.movimentar_via_controle(pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT)
    jogador1.desenhar(tela)
    
    for aranha in lista_aranha:
        aranha.movimenta()
        aranha.desenhar(tela)
        
        if jogador1.mascara.overlap(aranha.mascara, (aranha.pos_x - jogador1.pos_x, aranha.pos_y - jogador1.pos_y)):
            jogador1.pos_x = 300
            jogador1.pos_y = 450
            aranha.pos_y = 500
            jogador1.pontuacao -= 1
            jogador1.vidas -= 1
            if jogador1.vidas == 0:
                exit()
        
    for bombinha in lista_bombinha:
        bombinha.movimenta()
        bombinha.desenhar(tela)
        
        if jogador1.mascara.overlap(bombinha.mascara, (bombinha.pos_x - jogador1.pos_x, bombinha.pos_y - jogador1.pos_y)):
            jogador1.pontuacao += 1
            jogador1.pontuacao += 1
            bombinha.pos_y = 500
            som_bombinha.play()
            if jogador1.pontuacao == 50:
                exit()
        
    texto_pontuacao = fonte.render(f'Chegue nos 50 pontos, sua Pontuação: {jogador1.pontuacao}', True, (245, 7, 7))
    texto_vidas = fonte.render(f'Vidas: {jogador1.vidas}', True, (245, 7, 7))
    texto_poderes = fonte.render(f'Aperte espaço para usar, poderes: {jogador1.poderes}', True, (245, 7, 7))
    tela.blit(texto_poderes, (10, 34))
    tela.blit(texto_pontuacao, (10, 10))
    tela.blit(texto_vidas, (10, 21))



    #Atualizando a tela
    pygame.display.update()

    #Regulando o FPS
    clock.tick(60)