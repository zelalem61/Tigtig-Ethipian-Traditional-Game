import pygame
import math
import constants as const


class Player:
    def __init__(self, x, y, myname):
        self.x = x
        self.y = y
        self.radius = const.PADDLE_SIZE
        self.speed = const.PADDLE_SPEED
        self.mass = const.PADDLE_MASS
        self.angle = 0
        
        self.image = myname
    

    def check_vertical_bounds(self, height):
        # top
        if self.y - self.radius <= 0:
            self.y = self.radius
        # bottom
        elif self.y + self.radius > height:
            self.y = height - self.radius

    def check_left_boundary(self, width):
        if self.x - self.radius <= 0:
            self.x = self.radius
        elif self.x + self.radius > int(width / 2):
            self.x = int(width / 2) - self.radius

    def check_right_boundary(self, width):
        if self.x + self.radius > width:
            self.x = width - self.radius
        elif self.x - self.radius < int(width / 2):
            self.x = int(width / 2) + self.radius

    def move(self, up, down, left, right, time_delta):
        dx, dy = self.x, self.y
        self.x += (right - left) * self.speed * time_delta
        self.y += (down - up) * self.speed * time_delta

        dx = self.x - dx
        dy = self.y - dy

        self.angle = math.atan2(dy, dx)

    def draw(self, screen, color):
        position = (int(self.x), int(self.y))
        circle_center = (self.x, self.y)

        
        # draw the image here
        image = pygame.transform.scale(self.image,(100,100))
        image_center = (circle_center[0] - image.get_width() / 2, circle_center[1] - image.get_height() / 2)
        screen.blit(image, image_center)

    def get_pos(self):
        return (self.x, self.y)

    def reset(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
