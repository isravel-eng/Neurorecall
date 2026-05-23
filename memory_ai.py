class MemoryAI:
 def evaluate(self,target,user):
  score=0
  for i,v in enumerate(user):
   if i<len(target) and target[i]==v:
    score+=10
  return score
 def reaction(self,score):
  if score>80:return 'Photographic Memory'
  if score>60:return 'Excellent'
  return 'Keep Training'
