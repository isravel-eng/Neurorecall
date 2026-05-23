import random
OBJECTS=['APPLE','CAR','MOON','GAME','CAT','BALL','ROBOT','STAR']
class Sequence:
    def generate(self,round_no):
        size=min(3+round_no,8)
        return random.sample(OBJECTS,size)
