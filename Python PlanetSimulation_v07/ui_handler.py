import pygame

class UIHandler:
    def __init__(self, renderer):
        self.renderer = renderer

    def handle_events(self, planets):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    self.check_planet_click(planets, mouse_pos)
        return True

    def check_planet_click(self, planets, mouse_pos):
        for planet in planets:
            planet_x = planet.x * planet.SCALE + self.renderer.width / 2
            planet_y = planet.y * planet.SCALE + self.renderer.height / 2
            if (planet_x - planet.radius <= mouse_pos[0] <= planet_x + planet.radius) and \
               (planet_y - planet.radius <= mouse_pos[1] <= planet_y + planet.radius):
                planets.remove(planet)  # Remove planet on click
                break
