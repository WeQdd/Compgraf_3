import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 15)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = (60, 60, 60)
        self.speed = settings.bullet_speed

        # Инициализация звука выстрела
        self.shoot_sound = pygame.mixer.Sound("assets/sounds/hit.mp3")
        self.shoot_sound.play()

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)