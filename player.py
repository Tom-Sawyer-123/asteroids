import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):

    
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(dt, -1)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt, 1)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(dt)
        if self.timer > 0:
            self.timer -= dt
        elif keys[pygame.K_SPACE]:
            Player.shoot(self)
            self.timer = PLAYER_SHOOT_COOLDOWN
                
                

    def rotate(self, dt, direction):
        self.rotation += PLAYER_TURN_SPEED * dt * direction

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)
        new_shot.velocity = pygame.Vector2(0, 1)
        rotated = new_shot.velocity.rotate(self.rotation)
        new_shot.velocity = rotated
        new_shot.velocity *= PLAYER_SHOOT_SPEED