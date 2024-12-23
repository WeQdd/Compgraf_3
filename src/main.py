import pygame
from settings import Settings
from player import Ship
from alien import Alien
from bullet import Bullet
from graphics import Drawer

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Инопланетное вторжение")
        self.drawer = Drawer(self.settings.screen_width, self.settings.screen_height)
        self.ship = Ship(self, self.settings)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self._create_fleet()
        self.clock = pygame.time.Clock()
        self.running = True

        self.background_music = pygame.mixer.Sound("assets/sounds/theme.mp3")
        self.background_music.play(-1)

    def _create_fleet(self):
        # Создание флота инопланетян
        for i in range(5):  # Пример создания 5 инопланетян
            alien = Alien(self.screen, i * 100, 0, self.settings.alien_speed)  # Передаем необходимые аргументы
            self.aliens.add(alien)

    def run_game(self):
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.settings, self.screen, self.ship)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_aliens(self):
        self.aliens.update()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.draw()
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.aliens.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run_game()