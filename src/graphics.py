class Drawer:
    def __init__(self, width, height):
        import pygame
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

    def clear(self):
        self.screen.fill((255, 255, 255))

    def draw_line(self, start_pos, end_pos, color=(0, 0, 0), width=1):
        import pygame
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)

    def draw_circle(self, center, radius, color=(0, 0, 0), width=0):
        import pygame
        pygame.draw.circle(self.screen, color, center, radius, width)

    def draw_text(self, text, position, color=(0, 0, 0)):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, position)

    def draw_polygon(self, points, color=(0, 0, 0), width=0):
        import pygame
        pygame.draw.polygon(self.screen, color, points, width)

    def draw_axes(self):
        self.draw_line((self.width // 2, 0), (self.width // 2, self.height), color=(0, 0, 0), width=2)  # Y-axis
        self.draw_line((0, self.height // 2), (self.width, self.height // 2), color=(0, 0, 0), width=2)  # X-axis

    def update(self):
        import pygame
        pygame.display.flip()
        self.clock.tick(60)