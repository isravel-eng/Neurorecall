import pygame,random,time
from settings import *
POOL=['🍎','🚗','🌙','🎮','🐱','⚽']
class Game:
 def __init__(self):
  self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
  self.clock=pygame.time.Clock()
  self.font=pygame.font.SysFont(None,72)
  self.small=pygame.font.SysFont(None,36)
  self.round=1
  self.score=0
 def draw(self,t):
  self.screen.fill((15,18,35))
  s=self.font.render(t,True,(220,230,255))
  self.screen.blit(s,(100,300))
  pygame.display.flip()
 def sequence(self):
  seq=random.sample(POOL,min(self.round+2,6))
  for x in seq:
   self.draw(x)
   pygame.time.wait(900)
  self.draw('MEMORIZE')
  pygame.time.wait(800)
  return seq
 def run(self):
  running=True
  while running:
   seq=self.sequence()
   typed=''
   while True:
    self.screen.fill((15,18,35))
    msg=self.small.render('Type remembered sequence:',1,(255,255,255))
    inp=self.font.render(typed,1,(0,255,255))
    self.screen.blit(msg,(100,150))
    self.screen.blit(inp,(100,300))
    pygame.display.flip()
    for e in pygame.event.get():
      if e.type==pygame.QUIT:return
      if e.type==pygame.KEYDOWN:
       if e.key==pygame.K_RETURN:
         points=sum(a==b for a,b in zip(list(typed),seq))*10
         self.score+=points
         reaction='Excellent' if points>10 else 'Try Again'
         self.draw(reaction+' '+str(self.score))
         pygame.time.wait(1200)
         self.round+=1
         break
       elif e.key==pygame.K_BACKSPACE:
         typed=typed[:-1]
       else:
         typed+=e.unicode
    else:
      self.clock.tick(60)
      continue
    break
