import pygame
from planet_logic import Planet
from planet_render import Renderer
from ui_handler import UIHandler

def main():
    pygame.init()
    FONT = pygame.font.SysFont("comicsans", 16)

    # Create planets
    planets = [
        Planet(0, 0, 30, (255, 255, 0), 1.98892 * 10 ** 30),  # Sun
        Planet(-1 * Planet.AU, 0, 16, (100, 149, 237), 5.9742 * 10 ** 24),  # Earth
        Planet(-1.524 * Planet.AU, 0, 12, (188, 39, 50), 6.39 * 10 ** 23),  # Mars
        Planet(0.387 * Planet.AU, 0, 8, (80, 78, 81), 0.330 * 10 ** 24),  # Mercury
        Planet(0.723 * Planet.AU, 0, 14, (255, 255, 255), 4.8685 * 10 ** 24),  # Venus
    ]

    # Set the sun property for the first planet
    planets[0].sun = True

    # Set initial velocities for the planets
    planets[1].y_vel = 29.783 * 1000  # Earth velocity
    planets[2].y_vel = 24.077 * 1000  # Mars velocity
    planets[3].y_vel = -47.4 * 1000    # Mercury velocity
    planets[4].y_vel = -35.02 * 1000   # Venus velocity

    # Initialize the renderer
    renderer = Renderer(900, 710, FONT)
    ui_handler = UIHandler(renderer)

    run = True
    while run:
        renderer.clock.tick(60)

        # Handle user input
        run = ui_handler.handle_events(planets)

        # Update positions of planets
        for planet in planets:
            planet.update_position(planets)

        # Draw all planets and distances
        renderer.draw_planets(planets)

    pygame.quit()

if __name__ == "__main__":
    main()
