import pygame

class Ball:

    def __init__(self, screen, pos, right, bottom, color, size=10, speed=3):
        self.screen = screen
        self.x, self.y = pos
        self.bottom = bottom
        self.right = right

        self.x_velocity = speed
        self.y_velocity = speed

        self.color = color
        self.size = size


    def draw(self):
        self.move()
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.size)
    
    def move(self):

        self.x -= self.x_velocity
        self.y -= self.y_velocity

        if self.y <= 0 or self.y >= self.bottom:
            self.y_velocity = -self.y_velocity

        if self.x <= 0 or self.x >= self.right:
            self.x_velocity = -self.x_velocity