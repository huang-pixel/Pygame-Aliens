import pygame

pygame.init()

class Bluesky:
    """A pygame window with Bluesky background"""

    def __init__(self):
        """Create a simple Bluesky window"""

        # window: 1000 pixels wide, 800 pixels high
        self.window = pygame.display.set_mode((1000, 800))
        # set window title name
        pygame.display.set_caption('Blue sky')
        # clock for tracking time
        self.clock = pygame.time.Clock()
        
    def main(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
            self.window.fill('blue')
            pygame.display.flip()

            self.clock.tick(60)
        
        pygame.quit()

if __name__ == '__main__':
    bluesky = Bluesky()
    bluesky.main()
        
       
       









