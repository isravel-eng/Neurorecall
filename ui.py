import pygame
class UI:
    def draw_text(self,screen,text,font,pos,color=(255,255,255)):
        img=font.render(text,True,color)
        screen.blit(img,pos)
