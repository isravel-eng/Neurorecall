class Score:
    def __init__(self):
        self.total=0
        self.combo=0
    def update(self,points):
        self.total+=points
        self.combo=self.combo+1 if points>0 else 0
    def value(self):
        return self.total
