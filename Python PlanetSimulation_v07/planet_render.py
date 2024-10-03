import pygame

class Renderer:
    def __init__(self, width, height, font):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Planet Simulation")
        self.clock = pygame.time.Clock()
        self.FONT = font

    def draw_planets(self, planets):
        self.win.fill((0, 0, 0))  # Clear the screen

        # Draw planets and their trajectories
        for planet in planets:
            x = planet.x * planet.SCALE + self.width / 2
            y = planet.y * planet.SCALE + self.height / 2

            # Draw trajectory
            if len(planet.trajectory) > 1:
                trajectory_points = [
                    (px * planet.SCALE + self.width / 2, py * planet.SCALE + self.height / 2)
                    for px, py in planet.trajectory
                ]
                pygame.draw.lines(self.win, planet.color, False, trajectory_points, 2)

            pygame.draw.circle(self.win, planet.color, (int(x), int(y)), planet.radius)

        # Draw distances in the top right corner
        distance_y = 10  # Starting position for the distance text
        for planet in planets:
            if not planet.sun:  # Skip the sun
                distance_text = self.FONT.render(f"{round(planet.distance_to_sun / 1000, 1)} km", 1, planet.color)
                self.win.blit(distance_text, (self.width - distance_text.get_width() - 10, distance_y))
                distance_y += 20  # Move down for the next distance

        pygame.display.update()  # Update the display
