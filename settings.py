import pygame
import fonts
from os import walk

def import_folder(path):
	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list


width = 1280
height = 720
fps = 30
relogio = pygame.time.Clock()

fonte = 'verdana'

tela = pygame.display.set_mode((width, height))

