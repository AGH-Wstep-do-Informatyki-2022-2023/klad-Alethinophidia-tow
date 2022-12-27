import pygame

pygame.init()
window = pygame.display.set_mode((1200, 900))

class Pacman:
    def __init__(self, degree):
        self.x_cord = 0
        self.y_cord = 0
        self.image = pygame.image.load("assets/images/Pacman.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 4
    
    def rotation(self, degree):
        self.image = pygame.transform.rotate(pygame.image.load("Pacman.png"), degree)
        return self.image

    def move(self, wasd):
        if wasd[pygame.K_w] and self.y_cord >= 0:
            self.rotation(90)
            self.y_cord -= self.speed
        elif wasd[pygame.K_a] and self.x_cord >= 0:
            self.rotation(180)
            self.x_cord -= self.speed
        elif wasd[pygame.K_s]  and self.y_cord <= window.get_height()-self.image.get_height():
            self.rotation(270)
            self.y_cord += self.speed
        elif wasd[pygame.K_d] and self.x_cord <= window.get_width()-self.image.get_width():
            self.rotation(0)
            self.x_cord += self.speed

    def respown(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

def main():
    alive = True
    pacman = Pacman(0)
    while alive:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False

        wasd = pygame.key.get_pressed()
        pacman.move(wasd)
        window.fill((10, 10, 10))
        pacman.respown()
        pygame.display.update()

main()
