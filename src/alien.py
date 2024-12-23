import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, speed):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('assets/images/alien.png')  # Путь к изображению инопланетянина
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.x += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def reset_position(self):
        self.rect.x = 0  # Сброс позиции инопланетянина на левую сторону экрана
        self.rect.y += 50  # Сдвиг вниз на 50 пикселей после сброса позиции