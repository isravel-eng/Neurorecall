import random

POOL=['🍎','🚗','🌙','🎮','🐱','⚽']
print('NEURORECALL DEMO')
score=0
for round_no in range(1,4):
 seq=random.sample(POOL,round_no+2)
 print('\nRound',round_no)
 print('Remember:', ' '.join(seq))
 input('Press Enter after memorizing...')
 print('\n'*40)
 ans=input('Enter objects separated by space: ').split()
 pts=sum(1 for a,b in zip(ans,seq) if a==b)
 score+=pts
 print('Correct:',seq)
 print('Round Score:',pts)
print('Final Score:',score)
