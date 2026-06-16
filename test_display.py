import pygame
import time
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def test_display():
    print("Initializing pygame...")
    pygame.init()
    
    print(f"Creating display: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids - TEST")
    
    print("Window created. Sleeping for 5 seconds...")
    time.sleep(5)
    
    print("Drawing test content...")
    screen.fill("red")
    pygame.display.flip()
    
    print("Window should be RED now. Sleeping for 5 seconds...")
    time.sleep(5)
    
    print("Changing to blue...")
    screen.fill("blue")
    pygame.display.flip()
    
    print("Window should be BLUE now. Sleeping for 5 seconds...")
    time.sleep(5)
    
    pygame.quit()
    print("Done!")

if __name__ == "__main__":
    test_display()
