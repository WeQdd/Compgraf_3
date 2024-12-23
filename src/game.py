import pygame

from settings import Settings
from player import Ship
from alien import Alien
from bullet import Bullet
from graphics import Drawer

class Game:
    def __init__(self):
        import pygame
        from settings import Settings
        from player import Ship
        from alien import Alien
        from bullet import Bullet
        from graphics import Drawer

        pygame.init()
        self.settings = Settings()
        self.drawer = Drawer(self.settings.width, self.settings.height)
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self._create_fleet()
        self.running = True

    def _create_fleet(self):
        for i in range(5):  # Пример создания 5 инопланетян
            alien = Alien(self)
            self.aliens.add(alien)

    def run_game(self):
        while self.running:
            self._check_events()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.ship.check_events(event)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_aliens(self):
        self.aliens.update()

    def _update_screen(self):
        self.drawer.clear()
        self.ship.draw()
        self.aliens.draw(self.drawer.screen)
        self.bullets.draw(self.drawer.screen)
        self.drawer.update()