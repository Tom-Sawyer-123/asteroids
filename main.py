import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # initialize groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # add containers to objects
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots, updateable, drawable)
    
    # create objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    black = (0, 0, 0)

    # debug statements
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # loop variables
    clock = pygame.time.Clock()
    dt = 0
    lives = PLAYER_LIVES
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)
        for asteroid in asteroids:
            if player.collide(asteroid) == True:
                player.respawn()
                lives -= 1
                if lives == 1:
                    screen.render("WARNING!!! THIS IS YOUR LAST LIFE!!!")
                if lives > 0 and lives != 1:
                    screen.render(f"you have {lives} lives remaining")
            if lives == 0:
                screen.render("Game over LOSER!")
                sys.exit()
                
        for asteroid in asteroids:
            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()
        screen.fill(black)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()