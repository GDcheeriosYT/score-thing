import random
import time

combo = 0
score = 0

def hit():
  global score
  global combo
  object_types = [0, 1]
  object_type = object_types[random.randint(0, 1)]
  if object_type == 0:
    hit_point_range = [0, 50, 100, 300]
    just_hit = hit_point_range[random.randint(0, 3)]
    if just_hit == 0:
      combo = 0
      return(0)
    else:
      combo += 1
      return(just_hit)
  else:
    hit_point_range = [0, 50, 100, 300]
    just_hit = hit_point_range[random.randint(0, 3)]
    if just_hit == 0:
      combo = 0
      return(0)
    else:
      object_length = random.randint(2, 10)
      score += just_hit + (object_length * 10)
      combo += object_length
      return(just_hit)
    
    




def new_score(score_multiplier):
  global score
  if combo == 0:
    score += hit()
  else:
    score += int((hit() * (combo * score_multiplier)))
  print(f'''------------
hit a: {hit()}
combo: {("{:,}".format(combo))}x * {score_multiplier}x
score: {("{:,}".format(score))}
------------''')
  return new_score

while True:
  new_score(1)
  input("new hit!")