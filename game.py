import pygame
from settings import *
class Game:
 def __init__(self):
  self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
  pygame.display.set_caption(TITLE)
  self.clock=pygame.time.Clock()
 def run(self):
  running=True
  while running:
   for e in pygame.event.get():
    if e.type==pygame.QUIT:
      running=False
   self.screen.fill((15,18,35))
   pygame.display.flip()
   self.clock.tick(FPS)
