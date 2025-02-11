import sys

import pygame
from constants import *
from player import *
from asteroid import *
from asteroid_field import *


def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	game_clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	dt = 0

	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)

	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.is_colliding(player):
				print("Game over!")
				sys.exit()
		for item in drawable:
			item.draw(screen)
		pygame.display.flip()
		dt = game_clock.tick(60) / 1_000


if __name__ == "__main__":
	main()
