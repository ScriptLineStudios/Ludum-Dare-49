import pygame
import math
import random

pygame.font.init()

particles = []

def load_font(font_name, font_size):
    return pygame.font.Font(font_name, font_size)

def get_text_rect(text):
    return text.get_rect()

def render_text(display, text, font, bold, color, position):
    text = font.render(text, bold, color)
    display.blit(text, position)

def render_button(display, text, font, bold, color, position, clicking):
    text = font.render(text, bold, color)
    text_rect = get_text_rect(text)
    text_rect.center = (position[0]+text_rect.width/2, position[1]+text_rect.height/2)

    display.blit(text, position)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pos = (mouse_x, mouse_y)

    if text_rect.collidepoint(mouse_pos):
        pygame.draw.rect(display, color, text_rect, 1)
        if clicking:
            pass


def get_angle(x, y):
    rel_x, rel_y = mouse_x - x, mouse_y - y
    radians = math.atan2(rel_y,rel_x)
    angle = math.degrees(radians)
    return angle

class Particle:
    def __init__(self, x, y, x_vel, y_vel, radius, color, gravity_scale):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.gravity = 1
        self.radius = radius
        self.color = color
        self.lifetime = random.randrange(15, 20)
        self.gravity_scale = gravity_scale

    def draw(self, display):
        self.lifetime -= 1
        self.gravity -= self.gravity_scale
        self.x += self.x_vel
        self.y += self.y_vel * self.gravity
        self.radius -= 0.01

        pygame.draw.rect(display, self.color, (int(self.x), int(self.y), self.radius, self.radius))

def particle_burst():
    for x in range(1):
        particles.append(Particle(random.randrange(0, 400), -15, random.randrange(-1, 1), -0.05, 4, (163, 167, 194), 1))

def handle_particles(display):
    for particle in particles:
        particle.draw(display)

def animate(image_list, animation_index, time_to_show_image_on_screen):
    if animation_index+1 >= len(image_list)*time_to_show_image_on_screen:
        animation_index = 0
    animation_index += 1


    return animation_index
