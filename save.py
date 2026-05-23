import json
class Save:
 def write(self,data):
  json.dump(data,open('save.json','w'))
