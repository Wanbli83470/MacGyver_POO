#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import random
from constantes import *
ether_x = random.randint(0,15)
ether_x = ether_x * 50
ether_y = random.randint(0,15)
ether_y = ether_y * 50
seringue_x = random.randint(0,15)
seringue_x = seringue_x * 50
seringue_y = random.randint(0,15)
seringue_y = seringue_y * 50



position = {'a4':[0,150],
            'a8':[0,400],
            'a9':[0,400],
            'a11':[0,550],
            'a12':[0,550],
            'a13':[0,650],
            "b2":[50,50],
            "b4":[50,150],
            "b5":[50,200],
            "b8":[50,350],
            "b9":[50,400],
            "b10":[50,450],
            "b11":[50,500],
            "b13":[50,600],
            "b14":[50,650],
            "c2":[100,50],
            "c4":[100,150],
            "c8":[100,350],
            "c9":[100,400],
            "c11":[100,500],
            "c13":[100,600],
            "c14":[100,650],
            "d1" :[150,0],
            "d2":[150,50],
            "d3":[150,100],
            "d4":[150,150],
            "d6":[150,250],
            "d7":[150,300],
            "d8":[150,350],
            "d9":[150,400],
            "d11":[150,500],
            "d14":[150,650],
            "e4":[200,150],
            "e6":[200,250],
            "e14":[200,650],
            "f1" :[250,0],
            "f2":[250,50],
            "f4":[250,150],
            "f9":[250,400],
            "f12":[250,550],
            "f13":[250,600],
            "f14":[250,650],
            "g1" :[300,0],
            "g2":[300,50],
            "g4":[300,150],
            "g6":[300,250],
            "g9":[300,400],
            "g14":[300,650],
            "h1" :[350,0],
            "h2":[350,50],
            "h4":[350,150],
            "h6":[350,250],
            "h8":[350,350],
            "h9":[350,400],
            "h10":[350,450],
            "h11":[350,500],
            "h12":[350,550],
            "h14":[350,650],
            "i1" :[400,0],
            "i2":[400,50],
            "i4":[400,150],
            "i6":[400,250],
            "i8":[400,350],
            "i12":[400,550],
            "i13":[400,600],
            "i14":[400,650],
            "i15":[400,700],
            "j1" :[450,0],
            "j2":[450,50],
            "j3":[450,100],
            "j4":[450,150],
            "j5":[450,200],
            "j6":[450,250],
            "j8":[450,350],
            "j9":[450,400],
            "j10":[450,450],
            "j11":[450,500],
            "j15":[450,700],
            "k1" :[500,0],
            "k6":[500,250],
            "k7":[500,300],
            "k11":[500,550],
            "k15":[500,700],
            "l1" :[550,0],
            "l3":[550,100],
            "l4":[550,150],
            "l7":[550,300],
            "l9":[550,400],
            "l12":[550,550],
            "m1" :[600,0],
            "m3":[600,100],
            "m4":[600,150],
            "m5":[600,200],
            "m6":[600,250],
            "m7":[600,300],
            "m9":[600,400],
            "m12":[600,550],
            "n1" :[650,0],
            "n9":[650,400],
            "n12":[650,550],
            "o1" :[700,0],
            "p1" :[700,0],
            "p2":[700,50],
            "p3":[700,100],
            "p4":[700,150],
            "p5":[700,200],
            "p6":[700,250],
            "p7":[700,300],
            "p8":[700,350],
            "p9":[700,400],
            }
liste_auto = [[0,50],
            [0,150],
            [0,400],
            [0,400],
            [0,550],
            [0,550],
            [0,650],
            [0,700],
            [50,50],
            [50,150],
            [50,200],
            [50,350],
            [50,400],
            [50,450],
            [50,500],
            [50,600],
            [50,650],
            [100,50],
            [100,150],
            [100,300],
            [100,350],
            [100,400],
            [100,500],
            [100,550],
            [100,600],
            [100,650],
            [150,0],
            [150,50],
            [150,100],
            [150,150],
            [150,250],
            [150,300],
            [150,350],
            [150,450],
            [150,550],
            [150,650],
            [200,150],
            [200,250],
            [200,650],
            [250,0],
            [250,50],
            [250,150],
            [250,250],
            [250,350],
            [250,400],
            [250,500],
            [250,550],
            [250,600],
            [250,650],
            [300,0],
            [300,50],
            [300,150],
            [300,250],
            [300,400],
            [300,650],
            [350,0],
            [350,50],
            [350,150],
            [350,250],
            [350,350],
            [350,400],
            [350,450],
            [350,500],
            [350,550],
            [350,650],
            [400,0],
            [400,50],
            [400,150],
            [400,250],
            [400,350],
            [400,550],
            [400,600],
            [400,650],
            [400,700],
            [450,0],
            [450,50],
            [450,100],
            [450,150],
            [450,200],
            [450,250],
            [450,350],
            [450,400],
            [450,450],
            [450,500],
            [450,700],
            [500,0],
            [500,250],
            [500,300],
            [500,550],
            [500,600],
            [500,700],
            [550,0],
            [550,100],
            [550,150],
            [550,200],
            [550,250],
            [550,300],
            [550,400],
            [550,550],
            [600,0],
            [600,100],
            [600,150],
            [600,200],
            [600,250],
            [600,300],
            [600,400],
            [600,550],
            [600,600],
            [600,650],
            [650,0],
            [650,100],
            [650,150],
            [650,200],
            [650,250],
            [650,300],
            [650,350],
            [650,400],
            [650,550],
            [700,0],
            [700,400],
            [700,450],
            [700,500],
            [700,550],
            [700,600],
            [700,650],
            [700,0],
            [700,50],
            [700,100],
            [700,150],
            [700,200],
            [700,250],
            [700,300],
            [700,350],
            [700,400],
            [700,550]],
coordonnees = [[0,50],
[0,150],
[0,350],
[0,400],
[0,500],
[0,550],
[0,600],
[0,650],
[50,50],
[50,150],
[50,200],
[50,350],
[50,400],
[50,450],
[50,500],
[50,600],
[50,650],
[100,50],
[100,150],
[100,300],
[100,350],
[100,400],
[100,500],
[100,600],
[100,650],
[150,0],
[150,50],
[150,100],
[150,150],
[150,250],
[150,300],
[150,350],
[150,400],
[150,500],
[150,600],
[150,650],
[200,150],
[200,250],
[200,650],
[250,0],
[250,50],
[250,150],
[250,250],
[250,400],
[250,550],
[250,600],
[250,650],
[300,0],
[300,50],
[300,150],
[300,250],
[300,400],
[300,650],
[350,0],
[350,50],
[350,150],
[350,250],
[350,350],
[350,400],
[350,450],
[350,500],
[350,550],
[350,650],
[400,0],
[400,50],
[400,150],
[400,250],
[400,350],
[400,550],
[400,600],
[400,650],
[400,700],
[450,0],
[450,50],
[450,100],
[450,150],
[450,200],
[450,250],
[450,350],
[450,400],
[450,450],
[450,500],
[450,700],
[500,0],
[500,250],
[500,300],
[500,500],
[500,550],
[500,700],
[550,0],
[550,100],
[550,150],
[550,200],
[550,250],
[550,300],
[550,400],
[550,550],
[600,0],
[600,100],
[600,150],
[600,200],
[600,250],
[600,300],
[600,400],
[600,550],
[650,0],
[650,400],
[650,550],
[700,0],
[700,0],
[700,50],
[700,100],
[700,150],
[700,200],
[700,250],
[700,300],
[700,350],
[700,400],
[700,550]]
chemin = "n.txt"
f = open(chemin, 'a')

            

recup2 = position.get(random.choice(position.keys()))
recup3 = position.get(random.choice(position.keys()))
recup4 = position.get(random.choice(position.keys()))
recup5 = position.get(random.choice(position.keys()))

pygame.init()
#couleur
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

#compteur
counter = 0
# coordonnées case_dangers
C7=[100,300]
C14=[100,650]
L6=[550,250]
N12=[650,550]
#vie
vie = 11
position_seringue=(750,750)
appartion_seringue=(650,750)
#Opening PyGame windows
windows = pygame.display.set_mode((size_windows,size_windows))
#name windows
pygame.display.set_caption(titre_fenetre)
#loading background
fond = pygame.image.load(image_fond)
windows.blit(fond, (0,0))
#loading MacGyver
class perso:
	def __init(self,image):
		self.image=MacGyver = pygame.image.load(image_MacGyver).convert_alpha()
		#position en pixel
		self.position_perso.y= (50)

MacGyver = pygame.image.load(image_MacGyver).convert_alpha()
position_perso = MacGyver.get_rect()
windows.blit(MacGyver, position_perso)
position_perso.y = (50)
#loading Gardien
Gardien = pygame.image.load(image_Gardien).convert_alpha()
windows.blit(Gardien, (712,555))
#loading ether
seringue = pygame.image.load(image_seringue).convert_alpha()
windows.blit(seringue, (position_seringue))
#loading seringue
ether = pygame.image.load(image_ether).convert_alpha()
windows.blit(ether, (recup2))
#loading aiguille
aiguille = pygame.image.load(image_aiguille).convert_alpha()
windows.blit(aiguille, (recup4))
#loading boussole
boussole = pygame.image.load(image_boussole).convert_alpha()
windows.blit(boussole, (recup5))
#loading Game over
over = pygame.image.load(image_gameover).convert_alpha()
windows.blit(over, (0,0))
position_over = (750,750)
#loading WIN
win = pygame.image.load(image_win).convert_alpha()
windows.blit(win, (0,0))
position_win = (750,750)
#case_danger
case_danger = pygame.image.load(image_casedanger).convert_alpha()
windows.blit(case_danger, (C7))
#case_danger2
case_danger2 = pygame.image.load(image_casedanger).convert_alpha()
windows.blit(case_danger2, (C14))
#case_danger3
case_danger3 = pygame.image.load(image_casedanger).convert_alpha()
windows.blit(case_danger3, (L6))
# objets ramasses
font=pygame.font.Font(None,50)
text=font.render("objets ramasses : " + str(counter),True,(255,255,255))
rect_text = text.get_rect()
#compteur point de vie
points_de_vies = pygame.font.Font(None,50)
text2=font.render("SANTE : " + str(vie),True,(255,255,255))
rect_text2 = text2.get_rect()
#texte defaite
defaite=font.render("defaite",True,(255,255,255))
rect_text = defaite.get_rect()
position_texte = (750,750)
windows.blit(text,(20,715))
windows.blit(defaite,(750,750))
pygame.display.flip()










continuer = 1

while continuer:

 
    for event in pygame.event.get():

        if event.type == QUIT:
            continuer = 0

        if event.type == KEYDOWN :
            
            if event.key == K_LEFT:
                if position_x > 0:
                    if valeur_suivante_gauche in coordonnees:
                        position_perso = position_perso.move(-50,0)

            elif event.key == K_RIGHT:
                if position_x < 700:
                    if valeur_suivante_droite in coordonnees:
                        position_perso = position_perso.move(50,0)
                    
            elif event.key == K_UP:
                if position_y > 0:
                    if valeur_suivante_haut in coordonnees:
                        position_perso = position_perso.move(0,-50)
            elif event.key == K_DOWN:
                if position_y < 700:
                    if valeur_suivante_bas in coordonnees:
                        position_perso = position_perso.move(0,50)
    



    #Re-collage
    windows.blit(fond, (0,0))   
    windows.blit(MacGyver, position_perso)
    windows.blit(Gardien, (700,550))
    windows.blit(ether, (recup2))
    windows.blit(seringue, (position_seringue))
    windows.blit(text,(20,715))
    windows.blit(text2,(550,715))
    windows.blit(aiguille, (recup4))
    windows.blit(boussole, (recup5))
    windows.blit(defaite,(position_texte))
    windows.blit(over, (position_over))
    windows.blit(win, (position_win))
    windows.blit(case_danger, (C7))
    windows.blit(case_danger2, (C14))
    windows.blit(case_danger3, (L6))
        #refresh
    pygame.display.flip()
    #print(position_perso)

    position_precise = (position_perso[0:2])
    position_x = position_precise[0]
    position_y = position_precise[1]
    case_x = position_precise[0]/50
    case_y = position_precise[1]/50
    tuple_case = [case_x,case_y]

    #case_total = str(case_x)+ ";" +str(case_y)
    #print("case x :" + str(case_x))
    #print("case y :" + str(case_y))
    #print(case_total)
    print(position_precise)
    if position_precise == recup2:
        recup2 = (750,750)
    	counter += 1
        text=font.render("objets ramasses : " + str(counter),True,(255,255,255))
        rect_text = text.get_rect()
    elif position_precise == recup4:
        recup4 = (750,750)
        counter += 1
        text=font.render("objets ramasses : " + str(counter),True,(255,255,255))
        rect_text = text.get_rect()
    elif position_precise == recup5 :
        print("detection")
        recup5 = (750,750)
        counter += 1
        text=font.render("objets ramasses : " + str(counter),True,(255,255,255))
        rect_text = text.get_rect()
    	print(counter)
    elif position_precise == [700,550] and counter >= 3:
        print("fin du jeu")
        position_win = (0,0)
    elif position_precise == [700,550] and counter < 3:
        print("perdu")
        defaite=font.render("GAME OVER",True,(255,0,0))
        rect_text = defaite.get_rect().center
        position_over = (0,0)
    elif position_precise == C7:
        vie = vie -4
        C7=[750,750]
        text2=font.render("SANTE : " + str(vie),True,(255,255,255))
    elif position_precise == C14:
        vie = vie -4
        C14=[750,750]
        text2=font.render("SANTE : " + str(vie),True,(255,255,255))
    elif position_precise == L6:
        vie = vie -4
        L6=[750,750]
        text2=font.render("SANTE : " + str(vie),True,(255,255,255))
    elif counter == 3:
        position_seringue=(650,550)
    if counter == 3 :
    	print("objets tous recuperes")
    else:
    	print("pas de détéction")
        print("tout les objets ne sont pas rammasses")   
    if vie <=0:
        print("perdu")
        position_over = (0,0)




    #collision
    y50=(position_precise[1]+50)
    y_moins50=(position_precise[1]-50)
    y=(position_precise[1])



    x50=(position_precise[0]+50)
    x_moins50=(position_precise[0]-50)
    x=(position_precise[0])

    valeur_suivante_bas = [x,y50]
    valeur_suivante_haut = [x,y_moins50]
    valeur_suivante_droite = [x50,y]
    valeur_suivante_gauche = [x_moins50,y]