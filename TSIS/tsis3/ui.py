import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

class Button:
    def __init__(self, text, x, y, w, h, color=GRAY):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        txt = font.render(self.text, True, BLACK)
        screen.blit(txt, (self.rect.x + (self.rect.w - txt.get_width())//2, 
                          self.rect.y + (self.rect.h - txt.get_height())//2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def draw_text(screen, text, size, x, y, color=WHITE):
    font = pygame.font.SysFont("Arial", size)
    img = font.render(text, True, color)
    screen.blit(img, (x - img.get_width()//2, y))