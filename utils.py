import pygame

def center(surface,obj):
 r=obj.get_rect(center=surface.get_rect().center)
 return r

def clamp(v,a,b):
 return max(a,min(v,b))
