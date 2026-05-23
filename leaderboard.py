import json
class Leaderboard:
 def save(self,name,score):
  with open('scores.json','a') as f:
   f.write(json.dumps({'name':name,'score':score})+'\n')
