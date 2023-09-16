import random
def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    print(f'ROUND NUMBER {round}')
    x = random.randint(1,10)
    y = random.randint(1,10)
    return [x,y], storage