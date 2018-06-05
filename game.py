#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import*
from constantes import*

pygame.init()

windows = pygame.display.set_mode((size_windows, size_windows))
pygame.display.set_caption(title_windows)


#loading wall
mur = pygame.image.load(wall).convert()
windows.blit(mur,(0,0))
#loading background
background = pygame.image.load(background).convert()
windows.blit(background,(0,0))
pygame.display.flip()
#test


continuer = 0

while continuer == 0:
		for event in pygame.event.get():
		
			if event.type == QUIT:
				continuer = 1
		

		windows.blit(background,(0,0))
		chemin = "n.txt"

		ouverture = open(chemin, 'r')
		case_x = 0
		case_y = 0

		case = [case_x, case_y]

		x = case_x * 50
		y = case_y * 50

		xy = [x,y]

		position_depart = []
		position_arrivee = []
		coor = []
		coor_mur = []

		for ligne in ouverture.read():
			x = case_x * 50
			y = case_y * 50

			case_x = case_x +1

			if case_x > 15 :
				case_x = 0
				case_y = case_y + 1

			case = [case_x, case_y]
			xy = [x,y]

			print("x =  " + str(case_x) + "   y =  " + str(case_y))
			if ligne == "d":
				position_depart.append(case)
			elif ligne == "a":
				position_arrivee.append(case)
			elif ligne == "o":
				coor.append(case)
			elif ligne == "m":
				coor_mur.append(xy)
				windows.blit(mur,(x,y))

		print("la postion de depart est " + str(position_depart))
		print("la postion d'arrivee est " + str(position_arrivee))
		print("")
		print(coor)
		print(coor_mur)

		pygame.display.flip()